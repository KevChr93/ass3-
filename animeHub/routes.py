from animeHub import app, Animes, host
import csv
from animeHub.models import Anime, User
from flask import render_template, flash, url_for, redirect
from animeHub.animeForms import RegForm, LoginForm


@app.route("/")
@app.route("/home")
def home():
    with open('anime.csv', 'r',) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            ani = Anime(line['anime_id'], line['name'], line['genre'],
                        line['type'], line['episodes'], line['rating'], line['members'])
            Animes.append(ani)
            # database.commit()
    return render_template("home.html", records=Animes, host=host)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        msgstr = 'Account created for '+form.username.data+'!'
        flash(msgstr, 'success')
        return redirect(url_for('login'))
    return render_template('reg.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@animehub.com' and form.password.data == 'password':
            flash('You have been logged in as admin!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
