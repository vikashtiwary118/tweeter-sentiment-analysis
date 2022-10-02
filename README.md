"# tweeter-sentiment-analysis"<br />
Flask project template contains a working example of a Flask project with features:<br />
Simple setup and make local virtualenv isolated environment and doesn't trash your system python.<br />

Templates use Bootstrap but don't force you to use this UI framework.<br />

You only need to provide consumer_key, consumer_key_s, access_token, access_token_s of tweeter developer API.
Profile the key into config.py.

"#How to start"
The way is to manually clone this repository and change it later by own. Project is ready to run (with some requirements). You need to clone and run:
$ mkdir Project
$ cd Project
$ https://github.com/vikashtiwary118/tweeter-sentiment-analysis.git .

"#Comand to setup project in windows"
$cd tweeter-sentiment-analysis
$ python -m venv env
$ .\env\Script\activate
$pip install -r requirement.text
$python app.py

This time Flask will read configuration this order:
config.py inside the project folder

Also local.cfg is ignored in .gitignore so you will not accidentally put your database passwords to a public repository.


"#URL of tweeter-sentiment-analysis project"
I have deployee the project on heroku
Link: https://tweeter-sentiment-analysis.herokuapp.com/
