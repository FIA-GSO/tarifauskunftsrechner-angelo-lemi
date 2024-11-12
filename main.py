preis_erwachsene = 5.0
preis_kinder = 2.5
preis_jungendlich = 3.5
preis_premium = 3.0
preis_basis = 4.0
preis_sekt = 0.75
hinweis = "Tippen Sie y oder n ein\n"
zwischenerg = 0.0
gesamtsumme = 0.0


def tarif():
    global preis_erwachsene, preis_kinder, preis_jungendlich, preis_premium, preis_basis, zwischenerg
    print(" ### Tarifauskunftsrechner Museum XXX ### ")
    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())
    print("Wollen Sie ein Tagesticket oder Halbtagesticket?")
    antwort_ticket = int(input("1: Tagesticket, 2: Halbtagesticket\n"))
    if antwort_ticket == 1:
        preis_erwachsene *= 2
        preis_kinder *= 2
        preis_jungendlich *= 2
        preis_premium *= 2
        preis_basis *= 2

    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        print(" Preis: ", preis_kinder, " Euro ")
        zwischenerg += preis_kinder
    elif 14 <= alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        print(" Preis: ", preis_jungendlich, " Euro ")
        zwischenerg += preis_jungendlich
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input()
        if antwort_rabatt == "p":
            print(" ### Eintritt Premium-Mitglied ### ")
            print(" Preis: ", preis_premium, " Euro \n")
            print("Möchten Sie zusätzlich für", preis_sekt, "€ aufpreis einen Sekt trinken?")
            zwischenerg += preis_premium
            antwort_sekt = input(hinweis).strip().lower()
            if antwort_sekt == "y":
                print("Cheers")
                zwischenerg += preis_sekt
            elif antwort_sekt != "n":
                print("Fehler bei der antwort: Ihre Antwort", antwort_sekt)
                exit()
        elif antwort_rabatt == "b":
                print(" ### Eintritt Basis-Mitglied ### ")
                print(" Preis: ", preis_basis, " Euro ")
                zwischenerg += preis_basis
        else:
                print(" ### Eintritt Erwachsene (voller Preis) ### ")
                print(" Preis: ", preis_erwachsene, " Euro")
                zwischenerg += preis_erwachsene

tarif()

print("Wollen sie einen weiteren Tarif abfragen?")
tarif_abfrage = input()
if tarif_abfrage == "y":
    tarif()
    preis_erwachsene /= 2
    preis_kinder /= 2
    preis_jungendlich /= 2
    preis_premium /= 2
    preis_basis /= 2
elif tarif_abfrage == "n":
    gesamtsumme = zwischenerg
    print("Gesamtsumme: ", gesamtsumme)
    print("\nViel Spaß!\n")
    print("""\
██████╗ ██╗   ██╗██╗███████╗██████╗ ██╗   ██╗████████╗███████╗   
██╔══██╗██║   ██║██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╗
██║  ██║██║   ██║██║███████╗██████╔╝ ╚████╔╝    ██║   █████╗  ╚═╝
██║  ██║██║   ██║██║╚════██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝  ▄█╗
██████╔╝╚██████╔╝██║███████║██████╔╝   ██║      ██║   ███████╗▀═╝
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝   
                                                                 
""")

