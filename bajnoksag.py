class Csapat:
    def __init__(self, line):
        self.hely = int(line[0])
        self.csapat = line[1]
        self.gyozelem = int(line[2])
        self.dontetlen = int(line[3])
        self.kapott_gol = int(line[4])
        self.rugott_gol = int(line[5])
        self.pont = int(line[6])

    def __str__(self):
        return f"{self.hely}. hely: {self.csapat} ({self.pont} pont)"
    

def beolvas():
    temp = []
    f = open("bajnoksag.csv", "r", encoding="UTF8").read().split("\n")
    for i in range(len(f)):
        if i != 0:
            if f[i] != "":
                temp.append(Csapat(f[i].split(";")))
    return temp

def feladat2():
    print(f"1. feladat: A bajnokságban {len(beolvas())} csapat vett részt.")

def feladat3():
    csapat = input("3. feladat: Kérem a csapat nevét: ")
    for i in beolvas():
        if i.csapat == csapat:
            print(f"A {csapat} csapat {i.hely} helyen végzett a bajnokságon.")

def feladat4():
    temp = 0
    for i in beolvas():
        temp += i.rugott_gol
    print(f"4. feladat: A bajnokság során {temp} gólt rúgottak.")

def feladat5(csapat_nev):
    for i in beolvas():
        if i.csapat == csapat_nev:
            return 38-(i.gyozelem+i.dontetlen)
        
def feladat6():
    legrosszabb = []
    for i in beolvas():
        if legrosszabb == [] or feladat5(i.csapat) > feladat5(legrosszabb[0].csapat):
            legrosszabb.clear()
            legrosszabb.append(i)

    if legrosszabb[0].hely == 20:
        print(f"6. feladat: A legtöbb vesztett meccset játszó csapat: {legrosszabb[0].csapat} és ők is lettek a 20adikak.")
    else:
        print(f"6. feladat: A legtöbb vesztett meccset játszó csapat: {legrosszabb[0].csapat} de nem ők lettek a huszadikak.")

def feladat7():
    temp = []
    for i in beolvas():
        if abs(i.kapott_gol - i.rugott_gol) < 15:
            temp.append(f"{i.csapat} ==> {abs(i.kapott_gol - i.rugott_gol)}\n")
    f = open("adatok.txt", "w", encoding="UTF8")
    for i in temp:
        f.write(i)
    f.close()

def main():
    feladat2()
    feladat3()
    feladat4()
    feladat6()
    feladat7()

main()