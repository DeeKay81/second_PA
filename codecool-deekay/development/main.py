from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')
SHOWS_PER_PAGE = 15
SHOWN_PAGE_NUMBERS = 5


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/most-rated')
@app.route('/shows/order-by-<column>')
@app.route('/shows/order-by-<column>-<order>')
@app.route('/shows/order-by-<column>/<int:page_number>')
@app.route('/shows/most-rated/page-<int:page_number>')
@app.route('/shows/order-by-<column>-<order>/<int:page_number>')
def most_rated_shows(page_number=1, column='rating', order='desc'):
    count = queries.get_show_count()
    page_count = math.ceil(count[0]['count'] / SHOWS_PER_PAGE)
    shows = queries.get_most_rated_shows(column, order, SHOWS_PER_PAGE,
                                         (page_number - 1) * SHOWS_PER_PAGE)
    shown_pages_start = int(page_number - ((SHOWN_PAGE_NUMBERS - 1) / 2))
    shown_pages_end = int(page_number + ((SHOWN_PAGE_NUMBERS - 1) / 2))
    if shown_pages_start < 1:
        shown_pages_start = 1
        shown_pages_end = SHOWN_PAGE_NUMBERS
    elif shown_pages_end > page_count:
        shown_pages_start = page_count - SHOWN_PAGE_NUMBERS + 1
        shown_pages_end = page_count
    return render_template('most-rated-shows.html',
                           shows=shows,
                           pages=page_count,
                           page_number=page_number,
                           shown_pages_start=shown_pages_start,
                           shown_pages_end=shown_pages_end,
                           order_by=column,
                           order=order)


@app.route('/show/<int:show_id>')
def show_detail(show_id):
    show_details = queries.get_show_details(show_id)
    seasons = queries.get_seasons(show_id)
    return render_template('show-detail.html', details=show_details, seasons=seasons)


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
    app.run(debug=False)


if __name__ == '__main__':
    main()
