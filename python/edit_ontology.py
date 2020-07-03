from owlready2 import *

onto = get_ontology("bdd.owl").load()
ns = "http://linked_health.dz/Covid_ont#"

for i in onto.classes():
    print(i)

'''
def creer_patient(pseudo, mdp, dossierMedical):
    P = onto.Patient()
    P.iri = ns+pseudo
    P.Pseudo = pseudo
    P.MotDePasse = mdp
    P.hasDossierMedical.append(dossierMedical)'''

def authentificationPatient(pseudo,motdepass):
    if (onto.search(iri="*"+pseudo)[0]== []):
        print("Erreur : Pseudo introuvable")
        return False
    else :
        P = onto.search(iri="*"+pseudo)[0]
        if(P.MotDePasse != motdepass):
            print("Erreur : Mot de passe incorrect")
            return False
        else:
            print("utilisateur trouvé")
            return P

def afficher_individuals():
    print("individuals")
    for i in onto.individuals():
        print(i)

def creer_dossier_medical(pseudo, mdp, maladie, rhesus, groupeSang, wilaya, commune, antPerso, antFamille, poids, taille, genre, dateNaiss):
    D = onto.DossierMedical()
    D.iri = ns + pseudo
    D.Pseudo = pseudo
    D.MotDePasse = mdp
    D.MaladieChronique.append(maladie)
    D.Rhesus = rhesus
    D.GroupeSanguin = groupeSang
    D.Wilaya = wilaya
    D.Commune = commune
    D.AntecedantsPerso = antPerso
    D.AntecedentsFamille = antFamille
    D.Poids = poids
    D.Taille = taille
    D.Genre = genre
    D.DateNaiss = dateNaiss

def creer_medecin(nom, email, mdp, specialite, affiliation):
    M = onto.Medecin()
    M.iri = ns+email
    M.Nom.append(nom)
    M.MotDePasse = mdp
    M.Email = email
    M.Specialite.append(specialite)
    M.Affiliation.append(affiliation)

def authentificationMedecin(email,motdepass):
    if (onto.search(iri="*"+email)[0]== []):
        print("Erreur : Email introuvable")
    else :
        M = onto.search(iri="*"+email)[0]
        if(M.MotDePasse != motdepass):
            print("Erreur : Mot de passe incorrect")
        else:
            print("utilisateur trouvé")
            return M

onto.save("bdd.owl")
