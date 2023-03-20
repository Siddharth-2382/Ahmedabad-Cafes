from flask import Flask, render_template, request, redirect, flash, url_for, abort
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from werkzeug.security import generate_password_hash, check_password_hash
from places import get_places
import base64
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "itismytopsecretkeyforthiswebsite"

login_manager = LoginManager(app)

# Create database if it doesn't exist already
url = "mysql+pymysql://root:23082002@localhost/ahmedabad_cafes"
if not database_exists(url):
    create_database(url)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:23082002@localhost/ahmedabad_cafes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Tables
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))


class Places(db.Model):
    __tablename__ = "places"
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(100))
    p_address = db.Column(db.String(200))
    p_image = db.Column(db.LargeBinary(length=(2**32)-1))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id > 2:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/")
def home():
    places = Places.query.all()
    first_3_places = places[0:3]
    featured_places = []
    for place in places:
        info = {
            "name": place.p_name,
            "address": place.p_address,
            "image": base64.b64encode(place.p_image).decode("utf-8")
        }
        featured_places.append(info)
    return render_template("index.html", featured_places=featured_places)


@app.route("/all-cafes&restaurant")
def all_cafes():
    places = Places.query.all()
    all_places = []
    for place in places:
        info = {
            "id": place.id,
            "name": place.p_name,
            "address": place.p_address,
            "image": base64.b64encode(place.p_image).decode("utf-8")
        }
        all_places.append(info)
    return render_template("cafes.html", places=all_places)


@app.route("/search-cafe-or-restaurant", methods=["GET", "POST"])
def search_cafe():
    if request.method == "POST":
        name = request.form["place_query"]
        all_places = get_places(name)
        return render_template('add_cafe.html', all_places=all_places)
    else:
        return render_template('add_cafe.html', all_places=[])


@app.route("/add-cafe-or-restaurant", methods=["GET", "POST"])
def add_cafe():
    if not current_user.is_authenticated:
        flash("Log-in required!")
        return redirect(url_for('search_cafe'))
    else:
        if request.method == "POST":
            new_place = Places(
                p_name=request.form['name'],
                p_address=request.form['address'],
                p_image=base64.b64decode(request.form['image'])
            )
            db.session.add(new_place)
            db.session.commit()
            return redirect(url_for('home'))


@app.route("/remove-cafe/<int:cafe_id>", methods=["GET", "POST"])
@admin_only
def remove_cafe(cafe_id):
    cafe_to_remove = Places.query.get(cafe_id)
    db.session.delete(cafe_to_remove)
    db.session.commit()
    return redirect(url_for('all_cafes'))


@app.route("/sign-in")
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    return render_template("sign-in.html")


@app.route('/loginuser', methods=["POST"])
def loginuser():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Find user by email entered
        user = User.query.filter_by(email=email).first()

        # If user does not exists
        if not user:
            flash("That email does not exist. Register yourself and Join us now!")
            return redirect(url_for('sign_in'))

        # Check stored password hash against entered password hashed
        elif not check_password_hash(user.password, password):
            flash('Incorrect password, please try again.')
            return redirect(url_for('sign_in'))

        else:
            login_user(user)
            return redirect(url_for('home'))


@app.route('/cafe_info')
def cafe_info():
    return render_template('cafe_info.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first():

            # User already exists
            flash("You've already signed-up with that email, sign-in instead!")
            return redirect(url_for('sign_in'))
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hash_and_salted_password = generate_password_hash(
            password,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=email,
            name=name,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('home'))
    return redirect("login.html")


@app.route('/sign-out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
