"""
1.2 Feladat
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program (amig a felhasználó csak egy ENTER-t nem üt), 
majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!
"""

while True:
    mondat = input("Adj meg egy mondatot (vagy nyomj ENTER-t a kilépéshez): ")
    if mondat == "":
        break  # Kilép a ciklusból, ha csak egy ENTER-t üt a felhasználó

    if mondat[-1] == '.':
        print("A mondat kijelentő.")
    elif mondat[-1] == '?':
        print("A mondat kérdő.")
    elif mondat[-1] == '!':
        print("A mondat felkiáltó / felszólító / óhajtó.")
    else:
        print("A mondat vége nem ismert írásjel.")



# endswith
while True:
    mondat = input("Adj meg egy mondatot (vagy nyomj ENTER-t a kilépéshez): ")
    if mondat == "":
        break  # Kilép a ciklusból, ha csak egy ENTER-t üt a felhasználó

    if mondat.endswith('.'):
        print("A mondat kijelentő.")
    elif mondat.endswith('?'):
        print("A mondat kérdő.")
    elif mondat.endswith('!'):
        print("A mondat felkiáltó / felszólító / óhajtó.")
    else:
        print("A mondat vége nem ismert írásjel.")

