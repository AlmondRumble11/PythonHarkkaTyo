######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jesse Mustonen
# Opiskelijanumero: 0541805
# Päivämäärä: 16.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: Kurssilla ollut apumateriaali ja asssarit harkkaryhmässä
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
#importataan kirjasto
import HT_kirjasto
######################################################################

#pääohjelma jossa kaikki suoritetaan
def paaohjelma ():

    #listat joita käytetään
    lista = [] 
    tuloslista = []
    asemaLista = []
    
    #valikko ohjelmaa varten while loop 
    while (True):

        #käyttäjän valinta valikosta
        toiminto = HT_kirjasto.valikko()
        
        if toiminto == 0:
            print("Kiitos ohjelman käytöstä.")
            lista.clear()
            tuloslista.clear()
            break

        elif toiminto == 1:
            asemaLista = HT_kirjasto.havaintoasema(asemaLista) 

        elif toiminto == 2:
            lista = HT_kirjasto.luku(asemaLista, lista)

        elif toiminto == 3:
            tuloslista = HT_kirjasto.analysointi(lista, tuloslista)

        elif toiminto == 4:
            HT_kirjasto.tallennus(tuloslista,asemaLista)

        else: 
            print("Valintaa ei tunnistettu, yritä uudestaan.") 
            print()

    return None

paaohjelma()
######################################################################
#eof