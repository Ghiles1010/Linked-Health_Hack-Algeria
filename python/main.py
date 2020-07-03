from flask import Flask, render_template, request, Response, url_for, redirect, send_file
import cv2
from owlready2 import get_ontology
import edit_ontology
import qrcode

app = Flask(__name__,static_folder="..//static",template_folder="..//html")

onto = get_ontology("bdd.owl").load()

@app.route("/")
def home():
	edit_ontology.afficher_individuals()
	return render_template("index.html")

@app.route("/creer_dossier", methods = ['GET', 'POST'])
def creerDossier():
	if request.method == "POST":
		pseudo = request.form['q43_pseudonyme']
		mdp = request.form['q45_motDe']
		date = request.form['q9_dateDe[day]'] + "/" + request.form['q9_dateDe[month]'] + "/" + request.form['q9_dateDe[year]']
		genre = request.form['q22_genre']
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
		edit_ontology.creer_dossier_medical(pseudo, mdp, maladies, rhesus, groupeSanguin, wilaya, commune, antPerso, antFamille, poids, taille, genre, date)
		#edit_ontology.creer_patient(pseudo, mdp, edit_ontology.creer_dossier_medical(maladies, rhesus, groupeSanguin, wilaya, commune, antPerso, antFamille, poids, taille, genre, date))
		edit_ontology.afficher_individuals()
		return render_template("creer_dossier.html")
	else:
		return render_template("creer_dossier.html")

@app.route("/form_doc")
def form_doc():
	return render_template("form_doc.html")

@app.route("/qr")
def qr(path):
	return render_template("qr.html")

@app.route("/dowload")
def download_file():
	p="rafa.png"
	return send_file(p, as_attachment=True)

@app.route("/dossier/<pseudo>")
def dossier():
	return render_template("dossier.html")

@app.route("/auth_patient", methods = ['POST', 'GET'])
def auth_patient():
	if request.method == "POST":
		pseudo = request.form['pseudo']
		mdp = request.form['password']
		a = edit_ontology.authentificationPatient(pseudo, mdp)
		if a:
			# utilisateur trouvé
			qrcode.qrcode(pseudo)
			redirect(url_for("qr", pseudo+".png"))
			pass
		else:
			# pseudo introuvable
			pass
	return render_template("auth_patient.html")

@app.route("/auth_doctor", methods = ['POST', 'GET'])
def auth_doctor():
	if request.method == "POST":
		email = request.form['email']
		mdp = request.form['password']
		a = edit_ontology.authentificationPatient(email, mdp)
		if a:
			# utilisateur trouvé
			pass
		else:
			# pseudo introuvable
			pass
	return render_template("auth_doctor.html")

if __name__ == "__main__":
	
	app.run(debug = True)


