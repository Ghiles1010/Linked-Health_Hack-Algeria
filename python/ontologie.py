from owlready2 import *


default_world.set_backend(filename="file_back3.sqlite3", exclusive=False)

onto = get_ontology("http://linked_health.dz/onto.owl")
Url = "http://linked_health.dz/Covid_ont#"

with onto:
    # Class and Data Property
    class Medecin(Thing):
        pass

    #class Patient(Thing):
    #    pass

    class DossierMedical(Thing):
        pass

    class Pseudo(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class MotDePasse(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical, Medecin]

    class MaladieChronique(DataProperty):
        range = [str]
        domain = [DossierMedical]

    class DossierID(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Commune(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Wilaya(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class GroupeSanguin(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Rhesus(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class AntecedantsPerso(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class AntecedentsFamille(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Taille(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Poids(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class Genre(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class DateNaissance(DataProperty, FunctionalProperty):
        range = [str]
        domain = [DossierMedical]

    class ComptesRendusPrecedents(DataProperty):
        range = [str]
        domain = [DossierMedical]

    class Email(DataProperty, FunctionalProperty):
        range = [str]
        domain = [Medecin]

    class Specialite(DataProperty):
        range = [str]
        domain = [Medecin]

    class Affiliation(DataProperty):
        range = [str]
        domain = [Medecin]

    class Nom (DataProperty):
        range = [str]
        domain = [Medecin]

    #class hasDossierMedical (Patient >> DossierMedical):
    #    pass


onto.save("bdd.owl")