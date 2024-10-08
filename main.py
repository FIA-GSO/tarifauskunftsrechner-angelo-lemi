preis_erwachsene = 5.0
preis_kinder = 2.5
preis_jungendlich = 3.5
preis_premium = 3.0
preis_basis = 4.0

def Tarif():
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
    elif 14 <= alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jungendlich, " Euro ")
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro ")
            if antwort_rabatt == "b":
                print(" ### Eintritt Basis-Mitglied ### ")
                print(" Preis: ", preis_basis, " Euro ")
            else:
                print(" ### Eintritt Erwachsene (voller Preis) ### ")
                print(" Preis: ", preis_erwachsene, " Euro")

Tarif()

print("Wollen sie einen weiteren Tarif abfragen?")
tarif_abfrage = input()
if tarif_abfrage == "y":
    Tarif()
elif tarif_abfrage == "n":
    print("Viel Spaß!")