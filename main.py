from flask import Flask, render_template, jsonify
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


# exercise three ------------------------------------------------------------------------------
@app.route('/api/get-trailer/<show_id>')
def get_trailer(show_id):
    return jsonify(queries.get_trailer(show_id))


@app.route('/tv-show/<int:show_id>')
def display_details(show_id):
    details = queries.get_details(show_id)
    return render_template('list-character.html',
                           details=details,
                           show_id=show_id)


# authentication -----------------------------------------------------------------------------------
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
    app.run(debug=True,
            port=5000)


if __name__ == '__main__':
    main()
