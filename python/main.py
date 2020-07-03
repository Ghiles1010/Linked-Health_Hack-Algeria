from flask import Flask, render_template, request, Response, url_for, redirect
import Edit_Ontologie
import cv2
from owlready2 import get_ontology

app = Flask(__name__,static_folder="..//static",template_folder="..//html")

onto = get_ontology("sortiefinal.owl").load()

@app.route("/")
def home():
	print("hi")
	return render_template("index.html")

@app.route("/creer_dossier", methods = ['GET', 'POST'])
def creerDossier():
	if request.method == "POST":
		pseudo = request.form['q43_pseudonyme']
		mdp = request.form['q45_motDe']
		date = request.form['q9_dateDe[day]'] + "/" + request.form['q9_dateDe[month]'] + "/" + request.form['q9_dateDe[year]']
		wilaya = request.form['q40_wilaya']
		commune = request.form['q39_commune']
		poids = request.form['q41_poidsen']
		taille = request.form['q42_tailleen']
		groupeSanguin = request.form['q37_groupeSanguin']
		rhesus = request.form['q38_rhesus']
		antPerso = request.form['q21_antecedantsPersonnels']
		antFamille = request.form['q27_antecedantsFamiliaux']
		maladies = request.form['q47_maladiesChroniques']
		print(pseudo, mdp, date, wilaya, commune, poids, taille, groupeSanguin, rhesus, antPerso, antFamille, maladies)
		return render_template("creer_dossier.html")

	else:
		return render_template("creer_dossier.html")

@app.route("/form", methods = ['GET', 'POST'])
def form():
	if request.method == "POST":
		# récupérer les inputs
		nom = request.form['name']
		prenom = request.form['Fname']
		email = request.form['email']
		tel = request.form['phone']
		motdepasse = request.form['password']
		confirmmotdepasse = request.form['confirm']
		adresse = request.form['adresse']
		dateNaiss = request.form['date']
		antPerso = request.form['antecedantsP']
		antFamille = request.form['antecedantsF']
		profession = request.form['profession']
		autreMentions = request.form['autre']
		sexe = request.form['sexe']
		groupeSang = request.form['sang']
		rhesus = request.form['rhesus']
		print(groupeSang, rhesus)
		#maladie = request.form['divselected'].div.getlist('maladie')

		if nom == '':
			pass
		if prenom == '':
			pass
		if email == '':
			pass
		if tel == '':
			pass
		if len(motdepasse) < 6:
			pass
		if motdepasse != confirmmotdepasse:
			pass
		if dateNaiss == '':
			pass
		if groupeSang == 'Groupe Sanguin':
			pass



		# formulaire correct
		Edit_Ontologie.create_patient(nom, prenom,email, motdepasse, tel, dateNaiss, sexe, adresse, groupeSang, rhesus, profession,antPerso,antFamille,autreMentions)
		return redirect(url_for("search"))

	else:
		return render_template("form.html")

@app.route("/form_doc")
def form_doc():
	return render_template("form_doc.html")

@app.route("/qr")
def qr():
	return render_template("qr.html")


@app.route("/login", methods = ['GET', 'POST'])
def login():
	if request.method == "POST":
		mail = request.form['email']
		password = request.form['pass']
		print(mail, password, flush = True)
		# il faut checker dans la base de données


	return render_template("login.html")

@app.route("/search")
def search():
	return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.route("/telemed")
def telemed():
	return render_template("telemed.html")

@app.route("/dossier")
def dossier():
	return render_template("dossier.html")

@app.route("/auth_patient")
def auth_patient():
	return render_template("auth_patient.html")

@app.route("/auth_doctor")
def auth_doctor():
	return render_template("auth_doctor.html")


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


