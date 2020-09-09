elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        print("element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind,"kogus":kogus})


#lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

#loeme kongreetne element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("element {} ei eksisteeri".format(nimetus))
    else:
        return elemendid[nimetused.index(nimetus)]

#uuendame KONGREETSE elemendi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("element {} ei saa uuendada, kuna ta ei eksisteeri".format(nimetus))
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

#kustutame KONGREETSET elementi
def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        print("element {} ei saa kustutada, kuna ta ei eksisteeri".format(nimetus))
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])

#kustutame täielikult köik ära
def kustuta_elemendid():
    global elemendid
    elemendid.clear()

def main():
    #loome katseandmestik
    katse_elemendid = [
        {"nimetus": "leib", "hind":0.80, "kogus": 20},
        {"nimetus": "piim", "hind":0.50, "kogus": 15},
        {"nimetus": "vein", "hind":5.60, "kogus": 5},
    ]

    #testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    #testime üksiku elemendi lisamist
    lisa_element("kohupiim", 0.90, 15)
    lisa_element("vein", 5.60, 5)

    print(loe_element("leib"))
    print(loe_element("limonaad"))
    
    #testime uuendamist
    
    uuenda_element("vein", 10.0, 10)
    print(loe_element("vein"))

    #testime kustutamist
    kustuta_element("vein")
    print(loe_element("vein"))

    #testime kõikide elementide kustutamist
    kustuta_elemendid()
    print(loe_elemendid())

if __name__ == "__main__":
    main()