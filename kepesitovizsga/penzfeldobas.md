## Feladat: Pénzfeldobás randomizáláés ellenőrzése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a pénzfeldobás app-ot a http://selenium.oktwebs.training360.com/5201_kepesitovizsga/penzfeldobas.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
Az alkalmazás akkor működik helyesen ha 100 Pénzfeldobás gombnyomásból legalább a fej-ek száma 45 és 55 között van. Ezt kell ellenőrizned.
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat!


### TC_001: Az utolsó eredmény és a pénzfeldobások historyjának ellenőrzése:
    * Csinálj 20 pénzfeldobást
    * Ellenőrizd, hogy az Utolsó eredmény és a history utolsó eleme ugyanazt adja-e vissza (fej/írás)

### TC_002: A random működés ellenőrzése:
    * Végezz 100 pénzfeldobást
    * Számold össze a history alapján a fej-ek számát
	* Ha jól működik a random függvény, a fej-ek száma 45 és 55 között várható (assert)
	* Végezz 10 kísérletet, és vizsgáld meg, hogy átlagban mi jött ki a fej-ek számára

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `penzfeldobas.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `kepesitovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írjál kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(