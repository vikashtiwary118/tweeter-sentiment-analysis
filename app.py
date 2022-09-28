from flask import Flask, render_template, request, redirect
import sentiment_analysis
import json
app = Flask(__name__)

def fetchDataFromAPI(text):
	list_data=[{'tweet':'Wah modi ji Wah', 'sentiment': 'positive'}, {'tweet':'India loss the match', 'sentiment': 'negative'}, {'tweet':'I am going to delhi with my friend', 'sentiment': 'neutarl'}]
	return list_data

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def searched_tweet():
	if request.method == 'POST':
	    text = request.form['searched']
	    if text:
		    data_list=sentiment_analysis.sentimental_analysis(text)
		    number_of_page=len(data_list)//10
		    list_number_of_page=[i for i in range(1,number_of_page)]
		    return render_template('index1.html', rows=json.dumps(data_list),number_of_page=list_number_of_page)
	return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)