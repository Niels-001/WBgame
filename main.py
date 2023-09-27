def je_moeder ():
    if input("Wie wordt er geneukt? Mijn...") == "Moeder" or "moeder":
        print("Daar heb je helemaal gelijk in")
    else:
        print("Nope, probeer het eens opnieuw.")
        je_moeder()

je_moeder()