from Container import app,db
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user
from Container.models import User
from Container.forms import Signup,Login
from werkzeug.security import generate_password_hash,check_password_hash


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/welcome")
@login_required
def welcome_user():
    return render_template("success.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You Logged Out')
    return redirect(url_for('home'))


@app.route("/login", methods=['GET','POST'])
def login():
    form =Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('LOGGED in Succesfully')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form =Signup()
    if form.validate_on_submit():
        user_data = User(email=form.email.data, password=form.password.data)
        db.session.add(user_data)
        db.session.commit()
        flash('Thanks for registering, you can proceed...')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


if __name__=="__main__":
    app.run(debug=True)
