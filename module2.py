sonastik = {'Estonia': 'Tallinn', 'Russia' : 'Moscow', 'Tallinn' : 'Estonia', 'Moscow' : 'Russia', 'Riga': 'Latvia', 'Latvia': 'Riga', 'Finland': 'Helsinki', 'Helsinki': 'Finland', 'Sweden': 'Stockholm', 'Stockholm': 'Sweden', 'Germany': 'Berlin', 'Berlin': 'Germany', 'France': 'Paris', 'Paris': 'France','Italy': 'Rome', 'Rome': 'Italy','Belarus': 'Minsk','Minsk': 'Belarus','China': 'Pekin','Pekin': 'China','Japan': 'Tokyo','Tokyo': 'Japan','USA': 'Washington', 'Wasgington':'USA','Brasilia': 'Brasilia','Portugal': 'Lissabon', 'Lissabon': 'Portugal'}
def lisa_sse(sonastik:dict)->dict:
    """Lisama sõna sõnavarasse
	"""
    riik = input("Lisa riik: ")
    linn = input("Lisa pealinn: ")
    sonastik[riik] = linn
    sonastik[linn] = riik
    return sonastik

while True:
    print("Kas tahad tehingud rikidega teha?\n1-Jah\n2 - Ei")
    valik_=input()
    if valik_=="1":
        l_=input("Kirjutage pealinn või riik inglise keeles: ").title()
        if l_ in sonastik.keys():
            vast=sonastik[l_]
            print(vast)  
        else:
            print("Seda ei ole sõnatikus")
            print("Vali 1 kui tahad lisa seda sõnastikusse")
            print("Vali 2 kui ei taha mitte midagi sellega teha")
            valik=input()
            while True:
                if valik=="1":
                    lisa_sse(sonastik)
                    print(sonastik)
                elif valik=="2":
                    break
                else:
                    print("Vale!")
                    valik=input("Sisestage uuesti: ")
                    break
    else:
        print("Vale!")
        valik_=input("Sisestage uuesti: ")

