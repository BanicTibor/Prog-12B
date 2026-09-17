szamok=[]
for i in range(5):
    szamok.append(int(input("Kérek egy számot! ")))
osszeg=0
for szam in szamok:
    osszeg+=szam
print(f"Átlag: {osszeg/len(szamok)}")
index=0
while i < len(szamok) and szamok[index]%2 != 0:
    index+=1
if index<len(szamok):
    print("Van páros szám!")
else:
    print("Nincs páros szám!")
