######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jesse Mustonen
# Opiskelijanumero: 0541805
# Päivämäärä: 16.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: Kurssilla ollut apumateriaali ja asssarit harkkaryhmässä,: rivi 387,149-159  
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
##Importataan tarvittavat kirjastot
import sys
import datetime
import numpy

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
    print("5) Lue Ilmatieteen laitoksen tiedosto")
    print("6) Analysoi kuukausittaiset säätilatiedot")
    print("7) Tallenna kuukausittaiset säätilatiedot")
    print("8) Analysoi tuntikohtaiset säätilatiedot")
    print("9) Tallenna tuntikohtaiset säätilatiedot")    
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
def havaintoasema (asemaLista):
    asemaLista.clear()
    
    #käyttäjä antaa  havaintoaseman nimen
    nimi = input("Anna havaintoaseman nimi: ")
    asemaLista.append(nimi)
    
    #while loop niin pitkään ennen kuin käyttäjä antaa kokonaisluvun
    while True:

        try:
            vuosi = int(input("Anna analysoitava vuosi: "))
            asemaLista.append(vuosi)
            break

        except ValueError: # jos käyttäjä ei anna kokonaislukua
            print("Anna vuosiluku kokonaislukuna.")
    print()
    
    #palautetaan nimi ja vuosi pääohjelmaan
    return asemaLista

#valikon 2. vaihe
def luku (asemaLista, lista):

    if len(asemaLista) == 0 :
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        print()
        return lista

    tiedosto = asemaLista[0] + str(asemaLista[1]) + ".txt" # tehdään käyttäjän antamista tiedoista tiedosto
    
    #kokeillaan löytyykö tiedosto ja jos löytyy niin suoritetaan toimenpiteet
    try:
        avattu_tiedosto = open(tiedosto, "r", encoding="UTF-8")

    except OSError:
        print("Tiedoston '{}' avaaminen epäonnistui.".format(tiedosto))
        sys.exit(0) #pakko lopetetaan ohjelma
        
    try:

        avattu_tiedosto.readline() # otsikkorivi pois
        rivi_lkm = 1  # on luettu otsikko rivi
        lista.clear() #tyhjennetään lista

        #while loop niin pitkään kun tiedostossa on tietoja
        while (True):

            rivi = avattu_tiedosto.readline() # luetaan rivi kerralla
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
        print("Tiedosto '{}' luettu. Tiedostossa oli {} riviä.".format(tiedosto, rivi_lkm)) 
        print()
        
    except OSError: #jos ei löydy annettua tiedostoa FileNotFoundError
        print("Tiedoston '{}' lukeminen epäonnistui.".format(tiedosto))
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
                #keskiyön lisäys #saatu assarilta harkkaryhmässä
                summa = int(i.maara)
                paiva = i.pvm
            paiva = lista[x].pvm
            x = x + 1
            
        #tallenetaan viimeinenkin päivä tuloslistaan #saatu assarilta harkkaryhmässä
        kirjasto = KIRJASTO()
        kirjasto.pvm = paiva.strftime("%d.%m.%Y")
        kirjasto.maara = summa 
        tuloslista.append(kirjasto)

        print("Data analysoitu ajalta {} - {}.".format(lista[0].pvm.strftime("%d.%m.%Y"), lista[-1].pvm.strftime("%d.%m.%Y"))) 
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
                x = x + lista[i].maara
                minuutti = x/60
                tiedosto.write(";" + str(int(minuutti)))
            tiedosto.write("\n")
            
            tiedosto.close()  #suljetaan tiedosto
            print("Paisteaika tallennettu tiedostoon '{}'.".format(tallennus_tiedosto)) 
            print()

        except OSError:
            print("Tiedoston '{}' kirjoitus epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma

    else: #jos tuloslista on tyhjä
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        print()

    return lista

#valikon 5. vaihe
def luku_ilma (asemaLista, lista):
    
    if len(asemaLista) == 0:
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        print()
        return lista
    
    tiedosto = asemaLista[0] + str(asemaLista[1]) + "_fmi.txt" # tehdään käyttäjän antamista tiedoista tiedosto
    
    #kokeillaan löytyykö tiedosto ja jos löytyy niin suoritetaan toimenpiteet
    try:
        avattu_tiedosto = open(tiedosto, "r", encoding="UTF-8")

    except OSError:
        print("Tiedoston '{}' avaaminen epäonnistui.".format(tiedosto))
        sys.exit(0) #lopetetqaan ohjelman suoritus

    try:

        avattu_tiedosto.readline() 
        rivi_lkm = 1   
        lista.clear() 

        while (True):
            rivi_lkm = rivi_lkm + 1
            rivi = avattu_tiedosto.readline() # luetaan rivi 
            if (len(rivi) == 0):
                break
            rivi = rivi[:-1]
            sarake = rivi.split(',')
            kirjasto = KIRJASTO()
            muunnos = ("{}-{}-{}".format(sarake[0],sarake[1],sarake[2]))
            paivamaara = datetime.datetime.strptime(muunnos, "%Y-%m-%d")
            kirjasto.pvm = paivamaara
            kirjasto.aika = sarake[3]
            
            
            if sarake[5] == "": #jos tulee tyhjä kohta
                kirjasto.maara = 0

            else :
                kirjasto.maara = sarake[5]
            
            if kirjasto.pvm.year == asemaLista[1]: #pitää olla samaa vuotta
                lista.append(kirjasto)
    
        avattu_tiedosto.close() #suljetaan avattu tiedosto
        print("Tiedosto '{}' luettu. Tiedostossa oli {} riviä.".format(tiedosto, rivi_lkm)) 
        print()
        
    except OSError: #jos ei löydy annettua tiedostoa FileNotFoundError
        print("Tiedoston '{}' lukeminen epäonnistui.".format(tiedosto))
        sys.exit(0) #lopetetqaan ohjelman suoritus

    return lista

#valikon 6. vaihe
def analysointi_kk (lista, tuloslista):

    if len(lista) > 0:

        tuloslista.clear()  
        summa = 0
        kk = lista[0].pvm

        for i in lista:

            if kk.month == i.pvm.month :
                summa = summa + int(i.maara)

            else:
                kirjasto = KIRJASTO()
                kirjasto.pvm = kk
                kirjasto.maara = summa 
                tuloslista.append(kirjasto)
                #keskiyön lisäys
                summa = int(i.maara)
                kk = i.pvm

        #lisätään viimeinen alkio
        kirjasto = KIRJASTO()
        kirjasto.pvm = kk
        kirjasto.maara = summa
        tuloslista.append(kirjasto)

        print("Data analysoitu ajalta {} - {}.".format(lista[0].pvm.strftime("%d.%m.%Y"), lista[-1].pvm.strftime("%d.%m.%Y"))) 
        print()

    else: 
        print("Lista on tyhjä. Lue ensin tiedosto.") 
        print()

    return tuloslista

#valikon 7. vaihe
def tallennnus_kk (lista, asemaLista, parametri):

    if len(lista) > 0:

        tallennus_tiedosto = input("Anna kuukausitiedoston nimi: ")# käyttäjä antaa tallenettavan tiedoston nimen
        #jos tiedosto voidan avata

        try:
            tiedosto = open(tallennus_tiedosto, "a", encoding="UTF-8")
        
        except OSError:#jos tiedostoa ei voida avata
            print("Tiedoston '{}' avaaminen epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma

        try:

            if parametri == True:

            #kuukausi otsikkotiedot
                tiedosto.write("Kk") 
                for i in range(len(lista)):
                    kk = datetime.datetime.strftime(lista[i].pvm, "%m")
                    tiedosto.write(";" + str(kk))
                    i = i + 1
                tiedosto.write("\n")

            # kirjataan kuukasitiedot
            tiedosto.write(str(asemaLista[0]) + " " + str(asemaLista[1]))
            for i in range(len(lista)):
                minuutti = lista[i].maara / 60
                tiedosto.write(";" + str(int(minuutti)))
                i = i + 1
            tiedosto.write("\n")
    
            tiedosto.close()  #suljetaan tiedosto
            print("Paisteaika tallennettu tiedostoon '{}'.".format(tallennus_tiedosto)) 
            print()

        except OSError:
            print("Tiedoston '{}' kirjoitus epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma

    else: #jos tuloslista on tyhjä
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        print()
            
    return lista

#valikon 8. vaihe
def analysointi_tk (lista, matriisi):
    
    if len(lista) > 0: #jos lista ei ole thjä niin tehdään toimenpiteitä
        
        KUUKAUSI = 12 #matriisin rivit
        TUNTI = 24 #matriisin sarakkeet

        #matriisin luominen
        matriisi = numpy.zeros((KUUKAUSI, TUNTI), int)

        #matriisiin lisäys
        for i in lista:
            kk = i.pvm.month - 1
            h = i.aika.split(":")
            tunti = int(h[0])
            matriisi[kk][tunti] += int(i.maara)

        
        print("Data analysoitu ajalta {} - {}.".format(lista[0].pvm.strftime("%d.%m.%Y"), lista[-1].pvm.strftime("%d.%m.%Y"))) 
        print()

    else: 

        print("Lista on tyhjä. Lue ensin tiedosto.")
        print()
        return lista

    return matriisi #saatu harkkaryhmässä assarilta

#valikon 9. vaihe
def tallennus_tk (matriisi, asemaLista):
    
    #tarkistetaan että on suorittanut 1. vaiheen eli antaa aseman ja vuoden
    if len(asemaLista) == 0:
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        print()
        return asemaLista

    else:
 
        tallennus_tiedosto = str(asemaLista[0]) + str(asemaLista[1]) + "tunnit.txt"
        KUUKAUSI = 12
        TUNTI = 24

        try:
            tiedosto = open(tallennus_tiedosto, "w", encoding="UTF-8")

        except OSError:#jos tiedostoa ei voida avata
            print("Tiedoston '{}' avaaminen epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma
    
        try:

            tiedosto.write("{} {} tuntipohjainen paisteaika:".format(asemaLista[0],asemaLista[1]))
            tiedosto.write("\n")

            for i in range(TUNTI):
                tiedosto.write(";" + str(i))
                i += 1
            tiedosto.write("\n")

            try: #kokeillaan onko matriisi tyhjä
                
                #kuukausitiedot
                for kk in range (KUUKAUSI):
                    tiedosto.write(str((kk + 1)))
                    for h in range(TUNTI):
                        tiedosto.write(";" + str(int(matriisi[kk][h]/60)))
                    tiedosto.write("\n")

                #sarakkeiden yhteen laskettu summan kirjoitus
                tiedosto.write("Yht.")
                summa = numpy.sum((matriisi/60), axis= 0) #lasketaan yhteen
                for i in range(len(summa)):
                    tiedosto.write(";" + str(int(summa[i])))
                tiedosto.write("\n")   
                tiedosto.close() 

                print("Paisteaika tallennettu tiedostoon '{}'.".format(tallennus_tiedosto)) 
                print()

            except IndexError:
                print("Lista on tyhjä. Analysoi data ennen tallennusta.")
                print("")


        except OSError:
            print("Tiedoston '{}' kirjoitus epäonnistui.".format(tallennus_tiedosto))
            sys.exit(0) #pakko lopetetaan ohjelma

    return matriisi
######################################################################
#eof

