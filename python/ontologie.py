from owlready2 import *


default_world.set_backend(filename="file_back3.sqlite3", exclusive=False)

onto = get_ontology("http://sararaouf.org/onto.owl")
Url = "http://linked_health.dz/Covid_ont#"

with onto:
    # Class and Data Property
    class Medecin(Thing):
        pass

    class Patient(Thing):
        pass

    class DossierMedical(Thing):
        pass




