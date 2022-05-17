import math

from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, redirect, session, jsonify

from data import queries

load_dotenv()
app = Flask('codecool_series')
SHOWS_PER_PAGE = 15
SHOWN_PAGE_NUMBERS = 5


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html',
                           shows=shows)


@app.route('/design')
def design():
    """
    See how it should look like ;-)
    """
    return render_template('design.html')


@app.route('/api/get-most-rated-shows')
def most_rated_shows():
    return jsonify(queries.get_fifteen_highest_rated_shows())


@app.route('/shows/')
@app.route('/shows/most-rated/')
@app.route('/shows/most-rated/<int:page_number>')
def display_fifteen_highest_rated_shows(page_number=1):
    """
    Create a page accessible from the path /shows/most-rated, where the fifteen highest rated shows
    are displayed in a table, showing the highest rated one first. Display the title (make it a
    link to the /show/<id> URL), release year, average runtime length, rating (formatted as "9.2"),
    genres (in alphabetical order, separated by commas), and a link to the trailer and the homepage
    of the show (or the "No URL" string if there is no URL associated).
    """
    count = queries.get_show_count()
    page_count = math.ceil(count[0]['count'] / SHOWS_PER_PAGE)
    shown_pages_start = int(page_number - ((SHOWN_PAGE_NUMBERS - 1) / 2))
    shown_pages_end = int(page_number + ((SHOWN_PAGE_NUMBERS - 1) / 2))
    if shown_pages_start < 1:
        shown_pages_start = 1
        shown_pages_end = SHOWN_PAGE_NUMBERS
    elif shown_pages_end > page_count:
        shown_pages_start = page_count - SHOWN_PAGE_NUMBERS + 1
        shown_pages_end = page_count
    return render_template('highest-rated-shows.html',
                           pages=page_count,
                           page_number=page_number,
                           shown_pages_start=shown_pages_start,
                           shown_pages_end=shown_pages_end)


@app.route('/show/<int:show_id>')
def display_show_details(show_id):
    """
    The contents of the title column are links to the page of the show (/show/<id>).
    """
    show_details = queries.get_show_details(show_id)
    seasons = queries.get_seasons(show_id)
    return render_template('show-detail.html',
                           details=show_details,
                           seasons=seasons)


@app.route('/actors')
def display_hundred_actors():
    actors = queries.get_hundred_actors()
    return render_template('list-actors.html',
                           actors=actors)

@app.route('/api/get-shows-by-title/<name>')
def get_shows_by_the_title(name):
    shows = jsonify(queries.get_shows_by_actor_name(name))
    return shows


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


def main():
    app.run(debug=True)  # set from False to True


if __name__ == '__main__':
    main()
