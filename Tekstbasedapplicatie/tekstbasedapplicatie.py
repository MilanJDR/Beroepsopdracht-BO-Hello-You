# variabelen
Ja = ["Ja"]
Nee = ["Nee"]
Liften = ["Liften"]
Lopen = ["Lopen"]
Haven = ["Haven"]
Centrum = ["Centrum"]
Turkije = ["Turkije"]
Griekenland = ["Griekenland"]
Betalen = ["Betalen"]
Niet Betalen = ["Niet betalen"]


# hier worden de functies gedefined

def verhaal_1():
    keuze = input("pak je zoveel mogelijk spullen? Ja/Nee ")


    if keuze == ("Ja"):
        print("Je pakt zoveel mogelijk spullen")
        verhaal_2()

    elif keuze == ("Nee"):
        print("je pakt niks")
        verhaal_3()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_1()

def verhaal_2():

    print("Je hebt zoveel mogelijk spullen gepakt, Ga je naar je familie toe die toevallig in de buurt wonen ")
    print("Ja/Nee ")
    keuze = input("Ren je naar je familie toe? Ja/Nee ")

    if keuze == ("Ja"):
        print("Je rent naar je familie toe")
        verhaal_4()

    elif keuze == ("Nee"):
        print ("Je gaat niet naar je familie toe")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_2()


def verhaal_3():

    keuze = input("Je rent naar je familie toe je vraagt ze mee om te vluchten wat zegt je familie. Ja/Nee ")

    if keuze == ("Ja"):
        print("Je familie zegt ja")
        verhaal_5()

    elif keuze == ("Nee"):
        print("Je familie zegt nee")
        verhaal_6()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_3()


def verhaal_4():

    keuze = input("Je bent bij je familie je vraagt je familie om mee te vluchten. Wat zegt je familie? Ja/Nee ")

    if keuze == ("Ja"):
        print("Je familie zegt ja")
        verhaal_5()

    elif keuze == ("Nee"):
        print("Je familie zegt nee")
        verhaal_6()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_4()


def verhaal_5():

    print("Je familie zei ja en jullie gaan samen vluchten. Jullie gaan ver weg van jullie huis en zoeken een veilige plek om te overnachten. ")
    keuze = input("Jullie zien een oud verlaten huisje je familie wil daar overnachten wat zeg jij. Ja/Nee ")

    if keuze == ("Ja"):
        print("Je zegt ja en jullie gaan daar overnachten")
        verhaal_7()

    elif keuze == ("Nee"):
        print("je besluit om niet daar te willen overnachten")
        verhaal_8()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_5()




def verhaal_6():

    keuze = input("je loopt al een tijdje ondertussen is het al donker en je ziet een oud verlaten huisje ga je daar overnachten? Ja/Nee ")

    if keuze == ("Ja"):
        print("Je overnacht in het verlaten huisje")
        verhaal_9()

    elif keuze == ("Nee"):
        print("je gaat niet overnachten in het verlaten huisje")
        verhaal_10()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_6()



def verhaal_7():

    print("Jullie overnachten in het Verlaten huisje. Het is weer licht jullie lopen verder en zien een man stil staan naast de weg ")
    keuze = input("Gaan jullie naar hem toe om te vragen waar een stad is? Ja/Nee ")

    if keuze == ("Ja"):
        print("jullie vragen de man waar de stad is")
        verhaal_11()

    elif keuze ==("Nee"):
        print("jullie lopen door")
        verhaal_12()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_7()



def verhaal_8():

    keuze = input("Jullie lopen door en zoeken een andere slaapplek evenlater ziet een automobielist jullie en vraagt of jullie een lift nodig hebben wat zeg je? Ja/Nee ")

    if keuze == ("Ja"):
        print("jullie zeggen dat jullie een lift nodig hebben")
        verhaal_13()
    elif keuze == ("Nee"):
        print("jullie willen geen lift en lopen weer verder")
        verhaal_14()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_8()


def verhaal_9():

    keuze = input("Je word wakker en loopt verder evenlater zie je een man stil staan naast de weg, ga je hem de weg vragen naar de stad? Ja/Nee ")

    if keuze == ("Ja"):
        print("de man weet de weg naar de stad en vraagt of je op de vlucht bent")
        verhaal_15()
    elif keuze == ("Nee"):
        print("Je loopt door en zoekt naar een bord naar de stad")
        verhaal_16()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_9()

def verhaal_10():

    print("Je loopt verder en een tijdje later kom je een automobielist tegen en vraagt of je een lift nodig hebt ")
    keuze = input("zeg je Ja/Nee?")     

    if keuze == ("Ja"):
        print("Je neemt het aanbod aan van de automobielist")
        verhaal_17()
    elif keuze == ("Nee"):
        print("Je weigert de aanbod en loopt verder")
        verhaal_18()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_10()

def verhaal_11():
    keuze = input("de man laat zien waar de stad is en vraagt of jullie op de vlucht zijn wat zeg je Ja/Nee ")

    if keuze == ("Ja"):
        print("Jullie zeggen dat jullie op de vlucht zijn en leggen de situatie verder uit")
        verhaal_19()
    elif keuze ==("Nee"):
        print("jullie vertellen niks aan de man en lopen verder naar de stad")
        verhaal_20()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_11()
    

def verhaal_12():
    keuze = input("Jullie zien borden langs de weg en zien de stad. De stad is alleen heel ver weg nog wat ga je doen? Liften/Lopen ")

    if keuze == ("Liften"):
        print("Jullie proberen te liften")
        verhaal_21()
    elif keuze == ("Lopen"):
        print("Jullie gaan lopen")
        verhaal_22
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Lopen/Liften")
        verhaal_12()
    

def verhaal_13():
    print("Jullie krijgen een lift de automobielist moest toevallig naar de stad. ")
    print("Nu jullie in de stad zijn zoeken jullie een man die jullie zou helpen naar een andere land. ")
    keuze = input("waar gaan julle heen? Haven/Centrum")

    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
      else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_13()
        
def verhaal_14():
    print("Jullie besluiten om geen lift te nemen en gaan lopend naar de stad. ")
    print("2 dagen later komen jullie in de stad en gaan jullie zoeken naar de man die jullie zou helpen naar een andere land. ")
    keuze = input("waar gaan julle heen? Haven/Centrum. ")

    
    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
      else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_14()

def verhaal_15():
    keuze = input("Je antwoord op de man met. Ja/Nee ")

    if keuze == ("Ja"):
        print("je zei ja op de man zijn vraag")
        verhaal_25()

    elif keuze == ("Nee"):
        print("Je zei nee op de man zijn vraag")
        verhaal_26()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_15()

def verhaal_16():
   print("Je hebt wat borden gevonden die naar de stad leiden even later kom je in de stad.  ")
   print("Je zoekt naar de man die je uit het land zou halen. ")
   keuze = input("waar ga je zoeken? Haven/Centrum")

   if keuze == ("Haven"):
       print("Je zoekt in de haven")
       verhaal_27()

    elif keuze == ("Centrum"):
        print("Je zoekt in het Centrum")
        verhaal_28()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_16()

def verhaal_17():
    print("Je krijgt een lift naar de stad en gaat opzoek naar de man die je zou helpen vluchten. ")
    keuze = input("waar ga je zoeken? Haven/Centrum. ")

    if keuze == ("Haven"):
       print("Je zoekt in de haven")
       verhaal_27()

    elif keuze == ("Centrum"):
        print("Je zoekt in het Centrum")
        verhaal_28()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_17()


def verhaal_18():
    print("Je bent bij de stad aangekomen en gaat op zoek naar de man die je zou helpen vluchten. ")

    keuze = input("waar ga je zoeken? Haven/Centrum")

    if keuze == ("Haven"):
       print("Je zoekt in de haven")
       verhaal_27()

    elif keuze == ("Centrum"):
        print("Je zoekt in het Centrum")
        verhaal_28()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_18()

def verhaal_19():
    print("Nu jullie de situatie verder hebben uitgelegd vertelt de man jullie dat hij iemand kent die jullie kan helpen. ")
    print("De man vertelt die jullie moeten zoeken naar iemand in de stad die jullie zou helpen uit het land voor 300,- euro. ")
    keuze = input("waar gaan julle zoeken? Haven/Centrum. ")

    
    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
      else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_19()
         
def verhaal_20():
    print("Jullie zijn in de stad aanegekomen en gaan zoeken naar de man die jullie zou helpen vluchten ")
    keuze = input("waar gaan julle zoeken? Haven/Centrum. ")

    
    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
      else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee")
        verhaal_20()

def verhaal_21():
    print("iemand stopt langs de weg en helpt jullie naar de stad toe. ")
    print("nu jullie in de stad zijn moeten jullie de man zoeken die jullie helpt met vluchten. ")
    keuze = input("waar gaan julle zoeken? Haven/Centrum. ")

    
    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
      else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_21()


def verhaal_22():
    print("jullie lopen naar de stad en 2 dagen later zijn jullie in de stad. ")
    keuze = input("waar gaan julle zoeken? Haven/Centrum. ")

    
    if keuze == ("Haven"):
        print("Jullie gaan naar de haven")
        verhaal_23()
    elif keuze == ("Centrum"):
        print("Jullie gaan naar het centrum")
        verhaal_24()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_22()
    
def verhaal_23():
    print("Jullie zijn in de Haven en vinden de man de man vertelt jullie dat de reis 300,- euro kost per persoon. ")
    print("Dat zou al het geld zijn wat jullie hebben wat doe je? Betalen/Niet Betalen. ")

    if keuze == ("Betalen"):
        print("jullie betalen het geld")
        verhaal_29()       
    elif keuze == ("Niet Betalen"):
        print("Jullie betalen het geld niet")
        verhaal_30()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Betalen/Niet Betalen")
        verhaal_23()

def verhaal_24():
    print("Jullie zoeken in het centrum en vinden niemand die op de beschrijvingen van de man lijkt.  ")
    print("Het is avond en de man die jullie zoeken is er van door gegaan omdat het al over tijd was. ")
    keuze = input("Helaas is het je niet gelukt om te vluchten uit je land. Je kan Kiezen om te herstarten of niet. zeg Ja/Nee. ")

    if keuze == ("Ja"):
        print("Je begint weer opnieuw")
        verhaal_1()
        
    elif keuze == ("Nee"):
        print("Je herstart niet en wilt stoppen")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_24()

def verhaal_25():
    print("De man weet iemand die jullie kan helpen maar zegt dat het 350,- euro kost. ")
    print("Hij zegt dat het duurder is maar wel veiliger. ")
    keuze = input("Wat doe je? Betalen/Niet Betalen. ")

    if keuze == ("Betalen"):
        print("Je betaalt")
        verhaal_31()
        
    elif keuze == ("Niet Betalen"):
        print("Je betaalt niet")
        verhaal32()

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Betalen/Niet Betalen")
        verhaal_25()

def verhaal_26():
    print("Je bent bij de stad aangekomen en gaat op zoek naar de man die je zou helpen vluchten. ")
    keuze = input("waar ga je zoeken? Haven/Centrum")

    if keuze == ("Haven"):
       print("Je zoekt in de haven")
       verhaal_27()

    elif keuze == ("Centrum"):
        print("Je zoekt in het Centrum")
        verhaal_28()
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Haven/Centrum")
        verhaal_26()

def verhaal_27():
    print("Je hebt de man gevonden en hij vertelt je dat het 300,- euro kost ")
    keuze = input("Wat ga je doen? Betalen/Niet Betalen. ")

    if keuze == ("Betalen"):
       print("Je betaalt")
       verhaal_33()

    elif keuze == ("Niet Betalen"):
        print("Je betaalt niet")
        verhaal_34()
        
    else:
        print("dit is geen geldige keuze je kunt kiezen voor Betalen/Niet Betalen")
        verhaal_27()

def verhaal_28():
    print("Je zoekt in het centrum en vind niemand die op de beschrijvingen van de man lijkt.  ")
    print("Het is avond en de man die je zoekt is er van door gegaan omdat het al over tijd was. ")
    keuze = input("Helaas is het je niet gelukt om te vluchten uit je land. Je kan Kiezen om te herstarten of niet. zeg Ja/Nee. ")

    if keuze == ("Ja"):
        print("Je begint weer opnieuw")
        verhaal_1()
        
    elif keuze == ("Nee"):
        print("Je herstart niet en wilt stoppen")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_28()

def verhaal_29():
    print("Jullie hebben het geld betaalt en zijn nu aan het vluchten. ")


def verhaal_30():
    keuze = input("Helaas is het je niet gelukt om te vluchten uit je land. Je kan Kiezen om te herstarten of niet. zeg Ja/Nee. ")

    if keuze == ("Ja"):
        print("Je begint weer opnieuw")
        verhaal_1()
        
    elif keuze == ("Nee"):
        print("Je herstart niet en wilt stoppen")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_29()
        
def verhaal_31(): 
    print("Je betaalt de man en bent gevlucht ")

def verhaal_32():
    keuze = input("Helaas is het je niet gelukt om te vluchten uit je land. Je kan Kiezen om te herstarten of niet. zeg Ja/Nee. ")

    if keuze == ("Ja"):
        print("Je begint weer opnieuw")
        verhaal_1()
        
    elif keuze == ("Nee"):
        print("Je herstart niet en wilt stoppen")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_32()

def verhaal_33():
    print("Je betaalt en je bent gevlucht uit het land. ")

def verhaal_34():
    keuze = input("Helaas is het je niet gelukt om te vluchten uit je land. Je kan Kiezen om te herstarten of niet. zeg Ja/Nee. ")

    if keuze == ("Ja"):
        print("Je begint weer opnieuw")
        verhaal_1()
        
    elif keuze == ("Nee"):
        print("Je herstart niet en wilt stoppen")

    else:
        print("dit is geen geldige keuze je kunt kiezen voor Ja/Nee ")
        verhaal_34()




# hier start de main
keuze = input("Druk op enter om te beginnen.")

print("Je hoort een hard geluid je kijkt uit het raam en ziet Bommen vallen.")
print("in de verte hoor je mensen gillen en je hoort geweerschoten.")
verhaal_1()



