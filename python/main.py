from flask import Flask, render_template, request, url_for, redirect, send_file, session
import cv2
from owlready2 import get_ontology
import edit_ontology
import qrcode

app = Flask(__name__,static_folder="..//static",template_folder="..//html")
app.secret_key = "nous sommes géniaux, signé Rafa, Ghiles, Raouf & Chakib!"

onto = get_ontology("bdd.owl").load()

@app.route("/")
def home():
	edit_ontology.afficher_individuals()
	return render_template("index.html")

@app.route("/creer_dossier", methods = ['GET', 'POST'])
def creer_dossier():
	if "email" in session:
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
			edit_ontology.afficher_individuals()
			return render_template("creer_dossier.html")
		else:
			return render_template("creer_dossier.html")
	else:
		# medecin non connecté
		return redirect(url_for("auth_doctor"))

@app.route("/qr")
def qr():
	#p=request.args.get('path')
	return render_template("qr.html")

@app.route("/download")
def download_file():
	p=request.args.get('path')
	return send_file(p, as_attachment=True)

@app.route("/dossier")
def dossier():
	if "email" in session:
		M = edit_ontology.getMedecinByEmail(session["email"])

		id = request.args.get('id')
		# décrypter le id
		print(id)
		D = edit_ontology.getPatientByPseudo(id)
		pseudo = D.Pseudo
		maladie = ", ".join(D.MaladieChronique)
		rhesus = D.Rhesus
		grpS = D.GroupeSanguin
		wilaya = D.Wilaya
		commune = D.Commune
		antPerso = D.AntecedantsPerso
		antFamille = D.AntecedentsFamille
		poids = D.Poids
		taille = D.Taille
		genre = D.Genre
		dateNaiss = D.DateNaissance
		listeCompteRendu = D.ComptesRendusPrecedents
		print("len" + str(len(listeCompteRendu)))
		#maladie = "test"

		return render_template("dossier.html", lenListe=1, pseudo=pseudo, maladie=maladie, rhesus=rhesus, grpS=grpS, wilaya=wilaya, commune=commune, antFamille=antFamille, antPerso=antPerso, poids=poids, taille=taille, dateNaiss=dateNaiss, genre=genre, listeCompteRendu=listeCompteRendu)
		#return render_template("dossier.html", maladie=maladie)
	else:
		# medecin non connecté
		return redirect(url_for("auth_doctor", dossier=request.args.get('id')))

@app.route("/addCompteRendu")
def ajouterCompteRendu():
	pseudo = request.args.get('id')
	P = edit_ontology.getPatientByPseudo(pseudo)
	P.ComptesRendusPrecedents.append(session["email"], request.form['addCR'])
	onto.save("bdd.owl")


@app.route("/auth_patient", methods = ['POST', 'GET'])
def auth_patient():
	if request.method == "POST":
		pseudo = request.form['pseudo']
		mdp = request.form['password']
		a = edit_ontology.authentificationPatient(pseudo, mdp)
		if a:
			# utilisateur trouvé
			qrcode.qrcode(pseudo)				#creer le QR Code en PDF + PNG
			return redirect(url_for("qr", path=pseudo+".png"))
		else:
			# pseudo introuvable
			pass
	return render_template("auth_patient.html")

@app.route("/auth_doctor", methods = ['POST', 'GET'])
def auth_doctor():
	if len(request.args) != 0:
		dossier = request.args.get('dossier')

	if request.method == "POST":
		email = request.form['email']
		mdp = request.form['password']
		a = edit_ontology.authentificationMedecin(email, mdp)
		if a:
			# utilisateur trouvé
			session["email"] = email
			if len(request.args) != 0:
				return redirect(url_for("dossier", id=dossier))
			else:
				return redirect(url_for("creer_dossier"))
		else:
			# pseudo introuvable
			pass
	return render_template("auth_doctor.html")

if __name__ == "__main__":
	
	app.run(debug = True)


