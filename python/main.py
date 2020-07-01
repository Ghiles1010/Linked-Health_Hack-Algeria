from flask import Flask, render_template, request, Response
import Edit_Ontologie
import cv2

app = Flask(__name__,static_folder="..//static",template_folder="..//html")


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/form", methods = ['GET', 'POST'])
def form():
	if request.method == "POST":
		# récupérer les inputs
		nom = request.form['name']
		prenom = request.form['Fname']
		email = request.form['email']
		tel = request.form['phone']
		adresse = request.form['adresse']
		dateNaiss = request.form['date']
		antPerso = request.form['antecedantsP']
		antFamille = request.form['antecedantsF']
		profession = request.form['profession']
		autreMentions = request.form['autre']
		sexe = request.form['sexe']
		#maladie = request.form['divselected'].div.getlist('maladie')

		# formulaire correct
		Edit_Ontologie.create_patient("1", nom, prenom,email, tel, dateNaiss, sexe, adresse,profession,antPerso,antFamille,autreMentions)
		return render_template("form.html")

	else:
		print("GET", flush=True)
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

def get_frame():
	camera_port=0
	camera = cv2.VideoCapture(camera_port) #this makes a web cam object

	while True:
		retval, im = camera.read()
		imgencode=cv2.imencode('.jpg',im)[1]
		stringData=imgencode.tostring()
		yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

	del(camera)

@app.route('/calc')
def calc():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
	
	app.run(debug = True)

