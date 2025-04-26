def vaihtaja(ekasana, tokasana):
    #Funktio erottaa annetuista sanoista ensimmäiset morat, vaihtaa ne keskenään
    #ja palauttaa muunnetut sanat tuplena.
    #Funktio ei välitä vokaalisoinnusta, mutta se huomioi pitkät vokaalit
    vokaalit = "aeiouyäö"
    ekapitka = False
    tokapitka = False

    #Ensimmäinen mora on ensimmäinen vokaali ja sitä edeltävät konsonantit
    #Moran etsintä etenee sanassa kunnes törmää vokaaliin.
    #Sitten se tarkastaa onko myös seuraava kirjain sama vokaali.
    #Mikäli on, pituus-boolean merkitään todeksi jotta pituus voidaan huomioida
    #varsinaisen muunnoksen muodostamisvaiheessa.
    #Tämän jälkeen mora ja sanan loppuosa tallennetaan omiin muuttujiinsa
    for indeksi, kirjain in enumerate(ekasana):
        if kirjain in vokaalit and ekasana[indeksi + 1] == kirjain:
            ekamora = ekasana[:indeksi + 1]
            ekaloppu = ekasana[indeksi + 1:]
            ekapitka = True
            break
        elif kirjain in vokaalit:
            ekamora = ekasana[:indeksi + 1]
            ekaloppu = ekasana[indeksi + 1:]
            break

    for indeksi, kirjain in enumerate(tokasana):
        if kirjain in vokaalit and tokasana[indeksi + 1] == kirjain:
            tokamora = tokasana[:indeksi + 1]
            tokaloppu = tokasana[indeksi + 1:]
            tokapitka = True
            break
        elif kirjain in vokaalit:
            tokamora = tokasana[:indeksi + 1]
            tokaloppu = tokasana[indeksi + 1:]
            break

    #Jos alkuperäisessä sanassa on pitkä vokaali,
    #lisättävän moran vokaali, eli viimeinen merkki, kahdennetaan ennen yhdistämistä uuteen loppuun.
    if ekapitka:
        ekatulos = tokamora + tokamora[-1] + ekaloppu[1:]
    else:
        ekatulos = tokamora + ekaloppu

    if tokapitka:
        tokatulos = ekamora + ekamora[-1] + tokaloppu[1:]
    else:
        tokatulos = ekamora + tokaloppu

    return (ekatulos, tokatulos)
