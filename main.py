from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import datetime

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
    return render_template('design.html')


@app.route('/entry_level_1')
def entry_level_1():
    episodes = queries.entry_level_1()
    for episode in episodes:
        if episode['episodes'] > 99:
            episode['is_long'] = True
        else:
            episode['is_long'] = False
    return render_template('entry_level_1.html', episodes=episodes)


@app.route('/entry_level_2')
def entry_level_2():
    data = queries.entry_level_2()
    data[0]['name'] = data[0]['name'] + " 🥇"
    data[1]['name'] = data[1]['name'] + " 🥈"
    data[2]['name'] = data[2]['name'] + " 🥉"
    all_count = 0
    for person in data:
        all_count = all_count + person['counts']
    return render_template('entry_level_2.html', data=data, roles=all_count)


@app.route('/entry_level_3', methods=['GET', 'POST'])
def entry_level_3():
    if request.method == 'POST':
        data = ""
        season = request.form['season']
        episode = request.form['episode']
        print(season, episode)
        data = queries.entry_level_3(season, episode)
        return render_template('entry_level_3.html', data=data)
    return render_template('entry_level_3.html', data=None)


@app.route('/pa_1', methods=['GET', 'POST'])
def pa_1():
    if request.method == 'POST':
        genre = request.form['genre']
        data = queries.pa_1(genre)
        return render_template('pa_1.html', data=data)
    return render_template('pa_1.html', data=None)


@app.route('/pa_2')
def pa_2():
    data = queries.pa_2()
    return render_template('pa_2.html', data=data)


@app.route('/pa_3')
def pa_3():
    datas = {}
    data = queries.pa_3()
    for item in data:
        names = []
        title = item['title']
        data_list = queries.pa_3_2(item['title'])
        for i in data_list:
            names.append(i['name'])
        datas[title] = names
    return render_template('pa_3.html', data=data, datas=datas)


@app.route('/pa_9')
def pa_9():  # search actor name
    return render_template('pa_9.html')


@app.route('/pa_9_2', methods=['GET'])
def pa_9_2():
    result = []
    search = request.args.get('input-text')
    words = search.split(' ')
    for word in words:
        result = queries.pa_9('%' + word + '%')
    return jsonify(result)


@app.route('/pa_11')
def pa_11():
    data = queries.pa_11()
    return render_template('pa_11.html', data=data)


@app.route('/pa_11_2', methods=['GET'])
def pa_11_2():
    ids = request.args.get('input-text')
    result = queries.pa_11_2(ids)
    return jsonify(result)


# authentication -----------------------------------------------------------------------------------
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     return render_template("register.html")
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')
#
#
# @app.route('/logout')
# def logout():
#     pass


def main():
    app.run(debug=True,
            port=5000)


if __name__ == '__main__':
    main()
