**tweeter-sentiment-analysis**<br />

Flask project template contains a working example of a Flask project with features:<br />
Simple setup and make local virtualenv isolated environment and doesn't trash your system python.<br /><br />

Templates use Bootstrap but don't force you to use this UI framework.<br /><br />

You only need to provide consumer_key, consumer_key_s, access_token, access_token_s of tweeter developer API.<br />
Profile the key into config.py.<br /><br /><br />

**How to start**<br />

The way is to manually clone this repository and change it later by own. Project is ready to run (with some requirements). You need to clone and run:<br />
$ mkdir Project<br />
$ cd Project<br />
$ https://github.com/vikashtiwary118/tweeter-sentiment-analysis.git .<br /><br />

**Comand to setup project in windows**<br />

$cd tweeter-sentiment-analysis<br />
$ python -m venv env<br />
$ .\env\Script\activate<br />
$pip install -r requirement.text<br />
$python app.py<br /><br />

This time Flask will read configuration this order:<br />
config.py inside the project folder<br /><br />

Also local.cfg is ignored in .gitignore so you will not accidentally put your database passwords to a public repository.<br /><br />


**URL of tweeter-sentiment-analysis project**<br />

I have deployee the project on heroku<br />
Link: https://tweeter-sentiment-analysis.herokuapp.com/<br />
