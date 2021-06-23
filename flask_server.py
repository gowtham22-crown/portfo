from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data['email']
		subject=data['subject']
		content=data['content']
		file=database.write(f'\n{email},{subject},{content}')

def write_to_csv(data):
	with open("database2.csv",newline='',mode="a") as database3:
		email=data['email']
		subject=data['subject']
		content=data['content']
		csv_writer=csv.writer(database3,delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,content])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			print(data)
			write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return "did not saved to the database"
	else:
		return "try again"