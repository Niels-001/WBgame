def je_moeder ():
    moeder = input("Wie wordt er geneukt? Mijn...")
    if  moeder in ["moeder","Moeder"]:
        print("Daar heb je helemaal gelijk in")
    else:
        print("Nope, probeer het eens opnieuw.")
        je_moeder()

while True:
    je_moeder()