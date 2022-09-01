# Feladat: Lista elemeinek összeszorzása

Adott egy nem üres `numbers` nevű lista Pythonban:
```Python
# for example
numbers = [1, 2, 3, 4]
```

A lista legalább 2 számot tartalmazzon. Nincs felső korlát arra, hogy maximum hány számot tartalmazhat.

írj egy Python függvényt, ami összeszorozza a `numbers` lista elemeit és a függvényt meghívva írd ki az eredményt. Vegyél fel magadnak tesztként egy listát és azzal hajtsd végre a műveleteket. A programod ne csak kiírja a szorzás eredményét (beégetett konstans szövegként), hanem tényleg végezze el a műveletet.

A fenti példára a következő eredménynek kell kiíródnia:
```
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

Ügyelj arra, hogy a kiírás pontosan kövesse a fenti mintát, azaz így nézzen ki:
```
{eredeti lista tartalma} => {a szorzás képlete} = {a művelet eredménye}
```

### Tanácsok a megoldáshoz:
* Nem kell ellenőrizned, hogy a listában csak számok vannak-e.
* Nem kell ellenőrizned, hogy a lista tartalmaz-e legalább 2 számot.
* Nem kell ellenőrizned, hogy csak pozitív számokat tartalmaz-e a lista.
* A fentihez hasonló egyszerű listával teszteld a kódod, ami értelmezhető a feladatra és ami egyértelmű választ ad.
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`.
* Nincs plusz pont ha `kevesebb sorból oldod meg`, (a feladatnak többféle megoldása lehet, mind játszik és mindre lehet sok részpontot adni).


### A megoldás beadása
A megoldást egy `multiply_elements.py` nevű fájlban kell beadnod! 
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `felezovizsga` nevű mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* Akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása.
* A megoldás fájlba írj kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* Nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér. :(
