"""
1.1 Feladat
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! 
(kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)
"""
mondat = input("Adj meg egy mondatot: ")

if mondat[-1] == '.':
    print("A mondat kijelentő.")
elif mondat[-1] == '?':
    print("A mondat kérdő.")
elif mondat[-1] == '!':
    print("A mondat felkiáltó / felszólító / óhajtó.")
else:
    print("A mondat vége nem ismert írásjel.")


# Endswith

if mondat.endswith('.'):
    print("A mondat kijelentő.")
elif mondat.endswith('?'):
    print("A mondat kérdő.")
elif mondat.endswith('!'):
    print("A mondat felkiáltó / felszólító / óhajtó.")
else:
    print("A mondat vége nem ismert írásjel.")
