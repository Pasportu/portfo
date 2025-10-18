from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index_aerial.html")

@app.route("/home")
def my_home2():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("http://127.0.0.1:5000/thankyou.html#footer")
        except:
            return "Did not save to database."
    else:
        return "something went wrong"

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        fieldnames = ['name', 'email', "message"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)