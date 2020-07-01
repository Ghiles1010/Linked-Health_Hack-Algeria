from flask import Flask, render_template

app = Flask(__name__,static_folder="..//static",template_folder="..//html")


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/form_doc")
def form_doc():
	return render_template("form_doc.html")

@app.route("/search")
def search():
	return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.route("/telemed")
def telemed():
	return render_template("telemed.html")

@app.route("/doctor_profile")
def doctor_profile():
	return render_template("doctor_profile.html")

if __name__ == "__main__":
	
	app.run(debug = True)