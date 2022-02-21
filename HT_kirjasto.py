######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jesse Mustonen
# Opiskelijanumero: 0541805
# Päivämäärä: 16.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: Kurssilla ollut apumateriaali ja asssarit harkkaryhmässä
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
##Importataan tarvittavat kirjastot
import sys
import datetime
######################################################################
##Luokka
class KIRJASTO:
    pvm = ""
    aika = ""
    maara = 0
######################################################################
#valikko aliohjelma
def valikko ():
    
    #valikko
    print("Mitä haluat tehdä:")
    print("1) Anna havaintoasema ja vuosi")
    print("2) Lue säätilatiedosto")
    print("3) Analysoi päivittäiset säätilatiedot")
    print("4) Tallenna päivittäiset säätilatiedot")
    print("0) Lopeta")
  
    #while loop niin pitkään ennen kuin käyttäjä antaa kokonasiluvun
    while True:

        try:
            valinta = int(input("Valintasi: "))
            break

        except ValueError: # jos käyttäjä ei anna kokonaislukua
            print("Anna valinta kokonaislukuna.")
            
    #palautetaan paaohjelmaan käyttäjän antama valinta
    return valinta

#valikon 1. vaihe
def havaintoasema (lista):
    
    #käyttäjä antaa  havaintoaseman nimen
    nimi = input("Anna havaintoaseman nimi: ")
    lista.append(nimi)
    #while loop niin pitkään ennen kuin käyttäjä antaa kokonaisluvun
    while True:

        try:
            vuosi = int(input("Anna analysoitava vuosi: "))
            lista.append(vuosi)
            break

        except ValueError: # jos käyttäjä ei anna kokonaislukua
            print("Anna vuosiluku kokonaislukuna.")
    print()
    
    #palautetaan nimi ja vuosi pääohjelmaan
    return lista

#valikon 2. vaihe
def luku (asemaLista, lista):

    if len(asemaLista) == 0:
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        print()
        return lista

    tiedosto = asemaLista[0] + str(asemaLista[1]) + ".txt" # tehdään käyttäjän antamista tiedoista tiedosto
    
    #kokeillaan löytyykö tiedosto ja jos löytyy niin suoritetaan toimenpiteet
    try:
        avattu_tiedosto = open(tiedosto, "r", encoding="UTF-8")

    except OSError:
        print("Tiedoston '{0}' avaaminen epäonnistui.".format(tiedosto))
        sys.exit(0) #pakko lopetetaan ohjelma
        
    try:
        avattu_tiedosto.readline() # otsikkorivi pois
        rivi_lkm = 1  # on luettu otsikko rivi
        lista.clear() #tyhjennetään lista

        #while loop niin pitkään kun tiedostossa on tietoja
        while (True):
            rivi = avattu_tiedosto.readline() # luetaan riiv kerralla
            rivi_lkm = rivi_lkm + 1
            if (len(rivi) == 0): # leutaan tiedotoa niin pitkään ennen kuin tulee tyhjä rivi
                break
            rivi = rivi[:-1]
            sarake = rivi.split(';')

            #luokka alihjelmaan ja tehdään toimenpiteet
            kirjasto = KIRJASTO()
            muunnos = datetime.datetime.strptime(sarake[0], "%Y-%m-%d")
            kirjasto.pvm = muunnos
            kirjasto.aika = sarake[1]
            kirjasto.maara = sarake[2]
            lista.append(kirjasto) #lisätään kirjaston tiedot listaan
            
        avattu_tiedosto.close() #suljetaan avattu tiedosto
        print("Tiedosto '{0}' luettu. Tiedostossa oli {1} riviä.".format(tiedosto, rivi_lkm)) 
        print()
        
    except OSError: #jos ei löydy annettua tiedostoa FileNotFoundError
        print("Tiedoston '{0}' lukeminen epäonnistui.".format(tiedosto))
        sys.exit(0) #lopetetqaan ohjelman suoritus
        
    #palautetaan lista   
    return lista

#valikon 3. vaihe
def analysointi (lista, tuloslista):
    
    if len(lista) > 0: #jos lista ei ole thjä niin tehdään toimenpiteitä

        tuloslista.clear() #tyhjennetään tuloslista ennen kun sitä aletaan täyttämään
        kirjasto = KIRJASTO()
        paiva = lista[0].pvm
        summa = 0
        x = 0
        #for loop jossa lisätään listan arvoja tuloslistaan halutulla tavalla
        for i in lista:

            if paiva == i.pvm:
                summa = summa + int(i.maara)

            else:
                kirjasto = KIRJASTO()
                kirjasto.pvm = paiva.strftime("%d.%m.%Y") #muunnetaan päivät suomalaiseen muotoon
                kirjasto.maara = summa 
                tuloslista.append(kirjasto)
                #loopissa pois jäänyt päivän vaito
                summa = int(i.maara) 
                paiva = i.pvm
            paiva = lista[x].pvm
            x = x + 1
            
        #tallenetaan viimeinenkin päivä tuloslistaan
        kirjasto = KIRJASTO()
        kirjasto.pvm = paiva.strftime("%d.%m.%Y")
        kirjasto.maara = summa 
        tuloslista.append(kirjasto)

        print("Data analysoitu ajalta {0} - {1}.".format(lista[0].pvm.strftime("%d.%m.%Y"), lista[-1].pvm.strftime("%d.%m.%Y"))) 
        print()
        
    else: # jos lista on tyhjä
        print("Lista on tyhjä. Lue ensin tiedosto.")
        print()
    
    return tuloslista

# valikon 4. vaihe
def tallennus (lista, asemaLista):

    if len(lista) > 0:
        tallennus_tiedosto = input("Anna tulostiedoston nimi: ")# käyttäjä antaa tallenettavan tiedoston nimen

        #jos tiedosto voidan avata
        try:
            tiedosto = open(tallennus_tiedosto, "w", encoding="UTF-8")

        except OSError:#jos tiedostoa ei voida avata
            print("Tiedoston '{}' avaaminen epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma
            
        try:

            #kirjataan päivämäärä tiedot
            tiedosto.write("Pvm") 
            for i in range(len(lista)):
                tiedosto.write(";" + str(lista[i].pvm))
            tiedosto.write("\n")

            #kirjataan paikkakunnan tiedot
            tiedosto.write(str(asemaLista[0]))
            x = 0
            for i in range(len(lista)):
                x = x + lista[i].maara #kumulatiivinen summa
                minuutti = x / 60  
                tiedosto.write(";" + str(int(minuutti)))
            tiedosto.write("\n")
            
            tiedosto.close()  #suljetaan tiedosto
            print("Paisteaika tallennettu tiedostoon '{0}'.".format(tallennus_tiedosto)) 
            print()

        except OSError:
            print("Tiedoston '{0}' kirjoitus epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma

    else: #jos tuloslista on tyhjä
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        print()

    return lista