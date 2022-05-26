import math

from flask import Flask, render_template, url_for
from dotenv import load_dotenv

from data import queries

load_dotenv()
app = Flask('codecool_series')


# main ---------------------------------------------------------------------------------------------
@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('main/design.html')


# actors -------------------------------------------------------------------------------------------
@app.route('/get-all-actors/')
def display_all_actors():
    return render_template('all-actors.html')


# shows --------------------------------------------------------------------------------------------
@app.route('/get-all-shows/')
def display_all_shows():
    return render_template('all-shows.html')


# genres -------------------------------------------------------------------------------------------
@app.route('/get-all-genres/')
def display_all_genres():
    return render_template('all-genres.html')


# episodes -----------------------------------------------------------------------------------------
@app.route('/get-all-episodes/')
def display_all_episodes():
    return render_template('all-episodes.html')


# seasons ------------------------------------------------------------------------------------------
@app.route('/get-all-seasons/')
def display_all_seasons():
    return render_template('all-seasons.html')

# show_characters ----------------------------------------------------------------------------------


# show_genres --------------------------------------------------------------------------------------


# users --------------------------------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


# run ----------------------------------------------------------------------------------------------
def main():
    app.run(debug=True,
            port=5000)


if __name__ == '__main__':
    main()
