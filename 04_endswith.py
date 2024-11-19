# 1. Egy konkrét végződés ellenőrzése
# Ez a kód ellenőrzi, hogy a mondat három ponttal (...) végződik-e:

mondat = "Ez egy példa mondat..."
if mondat.endswith('...'):
    print("A mondat három ponttal végződik.")


# 2. Több végződés együttes ellenőrzése
# Ez a kód ellenőrzi, hogy a mondat kijelentő, kérdő vagy felkiáltó típusú-e:

mondat = "Ez egy kérdés?"
if mondat.endswith(('.', '!', '?')):
    print("A mondat kijelentő, kérdő vagy felkiáltó.")


# 3. Fájlnév ellenőrzése
# Ez a kód azt vizsgálja, hogy a fájlnév .txt kiterjesztéssel végződik-e:


filename = "dokumentum.txt"
if filename.endswith('.txt'):
    print("Ez egy szövegfájl.")

# Az endswith() metódus rendkívül hasznos, ha egyszerű és olvasható módon szeretnéd ellenőrizni egy sztring végződését.
