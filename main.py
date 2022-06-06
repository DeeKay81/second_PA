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


# exercise two ------------------------------------------------------------------------------
@app.route('/api/get-shows/')
def get_mystery_horror():
    return jsonify(queries.get_mystery_horror())


@app.route('/mystery-horror/')
def display_mystery_horror():
    mystery_horror = queries.get_mystery_horror()
    return render_template('mystery-horror.html',
                           mystery_horror=mystery_horror)


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
