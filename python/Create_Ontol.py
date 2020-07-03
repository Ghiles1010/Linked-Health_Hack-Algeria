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

    


    class Patient(Humain):
        pass

    class DateDeNaissance(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class Sexe(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class patientID(DataProperty, FunctionalProperty):  # Unicité a questionner
        range = [str]
        domain = [Patient]
        pass

    
    class AutreChose(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class GroupeSanguin(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]
    
    class Rhesus(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Patient]

    class Adresse(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Humain]
    
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


    class Symptomes(Thing):
        pass


    class SymptomesCovid(Symptomes):
        pass

    class nomSymptomes(DataProperty,FunctionalProperty):
        domain = [Symptomes]
        range = [str]

    class aSymptomes(Patient >> Symptomes):
        pass


    class Orientation(Thing):
        pass


    class Hopital(Orientation):
        pass


    class RDV(Orientation):
        pass

    class dateRDV(RDV >> str):
        pass

    #Prise en charge
    class PCDomicile(Orientation):
        pass

    class nomOrientation(Orientation >> str):
        pass

    class Fiche(Thing):
        pass


    class patientConcerne(Fiche >> Patient):
        pass


    class medecinConcerne(Fiche >> Medecin):
        pass





    class estConcerneParOrientation(Patient >> Orientation):
        pass

    class prescritOrientation(Medecin >> Orientation):
        pass

    AllDisjoint([Daira, Wilaya,Specialite,Symptomes,MaladieChronique,Patient,Medecin,Orientation,])


onto.save("sortie.owl", format="ntriples")