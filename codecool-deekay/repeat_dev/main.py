import math

from flask import Flask, render_template, url_for, jsonify
from dotenv import load_dotenv

from data import queries

load_dotenv()
app = Flask('codecool_series')


# main ---------------------------------------------------------------------------------------------
@app.route('/')
def index():
    # shows = queries.get_shows()
    return render_template('main/index.html')
                           # shows=shows)


@app.route('/design')
def design():
    return render_template('main/design.html')


# actors -------------------------------------------------------------------------------------------
@app.route('/get-all-actors/')
def display_all_actors():
    actors = queries.get_actors()
    return render_template('all-lists/all-actors.html',
                           actors=actors)


# shows --------------------------------------------------------------------------------------------
@app.route('/get-all-shows/')
def display_all_shows():
    shows = queries.get_shows()
    return render_template('all-lists/all-shows.html',
                           shows=shows)


@app.route('/api/get-shows-table')
def all_shows():
    return jsonify(queries.get_all_shows_table())


@app.route('/get-shows/table/')  # 15 shows per site missing yet
def display_all_shows_table():
    shows = queries.get_all_shows_table()
    return render_template('tables/shows-table.html',
                           shows=shows)


# genres -------------------------------------------------------------------------------------------
@app.route('/get-all-genres/')
def display_all_genres():
    genres = queries.get_genres()
    return render_template('all-lists/all-genres.html',
                           genres=genres)


# episodes -----------------------------------------------------------------------------------------
@app.route('/get-all-episodes/')
def display_all_episodes():
    episodes = queries.get_episodes()
    return render_template('all-lists/all-episodes.html',
                           episodes=episodes)


@app.route('/api/get-seasons-table')
def all_seasons():
    return jsonify(queries.get_all_seasons_table())


@app.route('/get-seasons/table/')
def display_all_seasons_table():
    seasons = queries.get_all_seasons_table()
    return render_template('tables/seasons-table.html',
                           seasons=seasons)


# seasons ------------------------------------------------------------------------------------------
@app.route('/get-all-seasons/')
def display_all_seasons():
    seasons = queries.get_seasons()
    return render_template('all-lists/all-seasons.html',
                           seasons=seasons)

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
