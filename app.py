from flask import Flask, render_template, request, url_for, redirect
import pickle as pkl
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():

	toss_winner1 = 3
	team1 = int(request.args.get('team1'))
	team2 = int(request.args.get('team2'))
	toss_winner = int(request.args.get('Toss Winner'))
	choose = int(request.args.get('Toss Decision'))

	if team1 == team2:
		return redirect(url_for('index'))
	if toss_winner == 0:
		toss_winner1 = team1
	elif toss_winner == 1:
		toss_winner1 = team2
	


	print(team1, team2, toss_winner1, choose)

	with open('model.pkl', 'rb') as f:
		model = pkl.load(f)

		arr = np.array([team1,team2,toss_winner1]).reshape(1,-1)

		predict = model.predict(arr)

		if predict == 1:
			return render_template('result.html', data="Royal Challengers Bangalore")
		elif predict == 2:
			return render_template('result.html', data="Kings XI Punjab")
		elif predict == 3:
			return render_template('result.html', data="Delhi Daredevils")
		elif predict == 4:
			return render_template('result.html', data="Mumbai Indians")
		elif predict == 5:
			return render_template('result.html', data="Kolkata Knight Riders")
		elif predict == 6:
			return render_template('result.html', data="Rajasthan Royals")
		elif predict == 7:
			return render_template('result.html', data="Deccan Chargers")
		elif predict == 8:
			return render_template('result.html', data="Chennai Super Kings")
		elif predict == 9:
			return render_template('result.html', data="Kochi Tuskers Kerala")
		elif predict == 10:
			return render_template('result.html', data="Pune Warriors")
		elif predict == 11:
			return render_template('result.html', data="Sunrisers Hyderabad", data1=predict)
		elif predict == 12:
			return render_template('result.html', data="Gujarat Lions")
		elif predict == 13:
			return render_template('result.html', data="Rising Pune Supergiants")
		elif predict == 14:
			return render_template('result.html', data="Delhi Capitals")
		

	

if __name__ == '__main__':
	app.run(debug=True)