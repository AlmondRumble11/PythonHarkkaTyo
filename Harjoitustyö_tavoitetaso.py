######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jesse Mustonen
# Opiskelijanumero: 0541805
# Päivämäärä: 16.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: Kurssilla ollut apumateriaali ja asssarit harkkaryhmässä
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
#importataan kirjasto
import HT_kirjasto_tavoitetaso
######################################################################

#pääohjelma jossa kaikki suoritetaan
def paaohjelma ():
    
    #listat joita käytetään
    lista = [] 
    tuloslista = []
    ilma_lista = []
    ilma_tuloslista_kk = []
    asemaLista = []
    parametri = True

    #matriisiin tarvittavat 
    KUUKAUSI=0
    TUNTI=0
    matriisi = ((KUUKAUSI, TUNTI), int)
    

    #valikko ohjelmaa varten while loop 
    while (True):

        #käyttäjän valinta valikosta
        toiminto = HT_kirjasto_tavoitetaso.valikko()
        
        if toiminto == 0:

            print("Kiitos ohjelman käytöstä.")
            lista.clear()
            tuloslista.clear()
            asemaLista.clear()
            ilma_lista.clear()
            ilma_tuloslista_kk.clear()

            break

        elif toiminto == 1:
            asemaLista = HT_kirjasto_tavoitetaso.havaintoasema(asemaLista) 

        elif toiminto == 2:
            lista = HT_kirjasto_tavoitetaso.luku(asemaLista, lista)

        elif toiminto == 3:
            tuloslista = HT_kirjasto_tavoitetaso.analysointi(lista, tuloslista)

        elif toiminto == 4:
            HT_kirjasto_tavoitetaso.tallennus(tuloslista,asemaLista)

        elif toiminto == 5:
            ilma_lista = HT_kirjasto_tavoitetaso.luku_ilma(asemaLista, ilma_lista)

        elif toiminto == 6:
            ilma_tuloslista_kk = HT_kirjasto_tavoitetaso.analysointi_kk(ilma_lista, ilma_tuloslista_kk)

        elif toiminto == 7:
            HT_kirjasto_tavoitetaso.tallennnus_kk(ilma_tuloslista_kk, asemaLista, parametri)
            parametri = False #yksisuuntainen lippu

        elif toiminto == 8:
            matriisi = HT_kirjasto_tavoitetaso.analysointi_tk(ilma_lista, matriisi)

        elif toiminto == 9:
            HT_kirjasto_tavoitetaso.tallennus_tk(matriisi, asemaLista)

        else: 
            print("Valintaa ei tunnistettu, yritä uudestaan.") 
            print()

    return None

paaohjelma()
######################################################################
#eof


