from flask import Flask, render_template, request, redirect
import sentiment_analysis
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html", rows=json.dumps([]))

@app.route('/tweeter', methods=['POST'])
def searched_tweet():
	if request.method == 'POST':
	    text = request.json['searched']
	    if text:
		    data_list=sentiment_analysis.sentimental_analysis(text)
		    number_of_page=len(data_list)//10
		    list_number_of_page=[i for i in range(1,number_of_page)]
		    return json.dumps(data_list)
	return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)