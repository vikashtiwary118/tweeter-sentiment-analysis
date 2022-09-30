from wtforms import Form, StringField

class searchForm(Form):
	searchField=StringField('search')