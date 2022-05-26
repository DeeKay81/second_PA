<h1>This is how we do it ...</h1>
<h2>Task 1 - set up environment</h2>
<h3>1. Create virtual environment:</h3>
<ul>
    <li>project folder</li>
    <li>python3 -m virtualenv venv</li>
    <li>make sure that the correct folder and interpreter is selected</li>
</ul>

<h3>2. Activate environment:</h3>
<ul>
    <li>source venv/bin/activate</li>
</ul>

<h3>3. Install requirements:</h3>
<ul>
    <li>requirements.txt file</li>
    <li>install the uninstalled (pip3 install -r requirements.txt)</li>
</ul>

<h3>4. Copy .env.template file and name ist .env</h3>

<h3>5. Fill in the missing parts:</h3>
<ul>
    <li>if pw is empty, a random word can be set (mine is "random")</li>
    <li>TRAKT_API_KEY can be left empty (what is this: https://www.addictivetips.com/media-streaming/kodi/create-implement-trakt-api-key-kodi-addons/)</li>
</ul>

<h3>6. Run main.py:</h3>
<ul>
	<li>make sure you've set up the right configuration (folder and venv) for main/server.py or sth like that</li>
</ul>

<h3>7. Create db (mine is called "ccseries)"</h3>
<ul>
	<li>Data Source PostgreSQL</li>
	<li>type to console: python3 data/data_inserter.py</li>
    <li>run (execute) db_schema/01_create_schema.sql</li>
</ul>

<h3>8. Write in command line (output see under command):</h3>

which python3

	/home/deekay81/PycharmProjects/week_pair_6/codecool-series-python-DeeKay81/venv/bin/python3

pip3 install -r requirements.txt

	Requirement already satisfied: certifi==2021.10.8 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (2021.10.8)
	Requirement already satisfied: chardet==3.0.4 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.0.4)
	Requirement already satisfied: charset-normalizer==2.0.12 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 3)) (2.0.12)
	Requirement already satisfied: click==8.0.4 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (8.0.4)
	Requirement already satisfied: Flask==2.0.3 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 5)) (2.0.3)
	Requirement already satisfied: idna==2.7 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 6)) (2.7)
	Requirement already satisfied: itsdangerous==2.1.1 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (2.1.1)
	Requirement already satisfied: Jinja2==3.0.3 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 8)) (3.0.3)
	Requirement already satisfied: MarkupSafe==2.1.0 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 9)) (2.1.0)
	Requirement already satisfied: psycopg2-binary==2.9.3 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 10)) (2.9.3)
	Requirement already satisfied: python-dotenv==0.13.0 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 11)) (0.13.0)
	Requirement already satisfied: requests==2.19.1 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 12)) (2.19.1)
	Requirement already satisfied: urllib3==1.23 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 13)) (1.23)
	Requirement already satisfied: Werkzeug==2.1.2 in ./venv/lib/python3.9/site-packages (from -r requirements.txt (line 14)) (2.1.2)

psql -d ccseries -c "SELECT relname, n_live_tup FROM pg_stat_user_tables;"

	     relname     | n_live_tup 
	-----------------+------------
	 show_characters |       8178
	 genres          |         34
	 seasons         |       5350
	 show_genres     |       2550
	 actors          |       6015
	 shows           |       1011
	 episodes        |      95694
	(7 rows)

python3 main.py

	(venv) deekay81@DeeKay81:~/PycharmProjects/week_pair_6/codecool-series-python-DeeKay81$ python3 main.py
	Serving Flask app 'codecool_series' (lazy loading)
	Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
	Debug mode: off
	Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

<h2>Task 2 - most rated shows</h2>

<h3>1. Change footer</h3>
<ul>
    <li>index.html, Copyright, DeeKay 2022</li>
</ul>

<h3>2. Split .html</h3>
<ul>
    <li>create layout.html</li>
    <li>copy index.html content to layout.html</li>
    <li>layout.html changes (block content, endblock):</li>

    <div id="body-wrapper">
        <header class="clearfix">
            <img id="header-logo" src="{{ url_for('static', filename='assets/codecool-logo.png') }}" alt="Codecool Logo">
            <span id="header-title" class="title">Codecool Series DB</span>
            <div id="header-auth">
                <button type="button" id="bt-register">Register</button>
                <button type="button" id="bt-login">Login</button>
            </div>
        </header>
        <h1 class="title text-center">Welcome page</h1>
    
        {% block content %}
        {% endblock %}
    
        <footer>
            Copyright, DeeKay 2022
        </footer>
    </div>
    <div class="background">
        <div class="dark-blue-layer"></div>
        <div class="light-blue-layer"></div>
    </div>
    </body>
    </html>


<li>index.html:</li>

    {% extends 'layout.html' %}
    {% block content %}

        <section>
            <div class="card">
                <h2>Welcome TV show lovers!</h2>
                <p>This great site is happy to bring you your favourite TV show's <i>details</i>.</p>
                <p></p>
                <p>Okay, actually this is a designed dumb page without any logic.</p>
                <p>You can find a navigational element, the so called "breadcrumb" above the page's title. Use it for
                    in-depth
                    navigation.
                </p>
            </div>
            <div class="card">
                <ul>
                    {% for show in shows %}
                        <li>
                            <a href="{{ '/tv-show/' + (show['id'] | string) }}">{{ show['title'] }}</a>
                        </li>
                    {% endfor %}
                </ul>
            </div>
        </section>
    
    {% endblock %}

</ul>

