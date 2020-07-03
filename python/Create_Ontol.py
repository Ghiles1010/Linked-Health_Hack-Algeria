from owlready2 import *
import rdflib


default_world.set_backend(filename="file_back3.sqlite3", exclusive=False)

onto = get_ontology("http://sararaouf.org/onto.owl")
Url = "http://sararaouf.oms/Covid_ont#"

with onto:
    # Class and Data Property
    class Humain(Thing):
        pass


    class Nom(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]


    class Prenom(DataProperty):
        range = [str]
        domain = [Humain]

    class Email(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class Telephone(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class Password(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class Pseudo(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]



    class Patient(Humain):
        pass

    class patientID(DataProperty,FunctionalProperty):
        range = [str]
        domain = [Patient]

    class Taille(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class Poids(DataProperty, FunctionalProperty):
      range = [str]
      domain = [Patient]

    class DateDeNaissance(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class Genre(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]



    class GroupeSanguin(DataProperty):
        range = [str]
        domain = [Patient]
    
    class Rhesus(DataProperty):
        range = [str]
        domain = [Patient]

    
    class Profession(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]

    class AntecedentPerso(DataProperty):
        range = [str]
        domain = [Humain]
    
    class AntecedentFamille(DataProperty):
        range=[str]
        domain=[Humain]



    class MaladieChronique(Thing):
        pass

    class nomMaladie(DataProperty,FunctionalProperty):
        domain = [MaladieChronique]
        range = [str]
        pass

    class estMaladeDe(Patient >> MaladieChronique):
        pass



    class CompteRendu(Thing):
        pass

    class contenuCompteRendu(CompteRendu >> str):
        pass







    class Medecin(Humain):
        pass


    class medecinID(DataProperty, FunctionalProperty):
        domain = [Medecin]
        range = [str]
        pass



    class Specialite(Thing):
        pass

    class nomSpecialite(DataProperty, FunctionalProperty):
        domain = [Specialite]
        range = [str]
        pass

    class estSpecialise(Medecin >> Specialite):
        pass



    class Localisation(Thing):
        pass


    class Wilaya(Localisation):
        pass

    class nomWilaya(DataProperty,FunctionalProperty):
        domain = [Wilaya]
        range = [str]

    class idWilaya(DataProperty,FunctionalProperty):
        domain = [Wilaya]
        range = [str]
        pass


    class Daira(Localisation):
        pass

    class nomDaira(DataProperty,FunctionalProperty):
        domain = [Daira]
        range = [str]

    class communeDe(Daira >> Wilaya):
        pass

    class estLocalise(Thing >> Localisation):
        pass

    estLocalise.max(1,Localisation)


    class aredigeCR(Medecin >> CompteRendu):
        pass

    class concerneparCR(Patient >> CompteRendu):
        pass


    class Hopital(Thing):
        pass


    class nomHopital(Hopital >> str):
        pass


    class adresseHopital(Hopital >> str):
        pass

    class estAffilié(Medecin >> Hopital):
        pass

    estAffilié.max(1,Hopital)





    AllDisjoint([Daira, Wilaya,Specialite,MaladieChronique,Patient,Medecin,Hopital])


onto.save("sortie.owl", format="ntriples")
