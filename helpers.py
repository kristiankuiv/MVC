elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    elemendid.append({"nimetus":nimetus, "hind":hind,"kogus":kogus})

#lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#loome katseandmestik
katse_elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "vein", "hind":5.60, "kogus": 5},
]
#testime elementide lisamist
lisa_elemendid(katse_elemendid)
print(elemendid)

#testime üksiku elemendi lisamist
lisa_element("kohupiim", 0.90, 15)