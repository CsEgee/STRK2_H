# Feladat: Alfanumerikus mező validálása

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be az Alfanumerikus mezőapp-ot a http://selenium.oktwebs.training360.com/5201_kepesitovizsga/alfanum.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az Alfanumerikus mező app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat!

A cél a mező validáció tesztelése:

### TC_001: Helyes kitöltés esete:
    * Beviteli mező: abcd1234
    * Hibaüzenet: Nincs

### TC_002: Illegális karakterek esete:
    * Beviteli mező: teszt233@
    * Hibaüzenet: Only a-z and 0-9 characters allowed.

### TC_003: Túl rövid bemenet esete:
    * Beviteli mező: 12cd
    * Hibaüzenet: Login should be at least 8 characters; you entered 4
	
### TC_004: Üres beviteli mező esete (csak kitöltés és törlés esetén jön elő):
    * Beviteli mező: 12cd, majd törlés:
    * Hibaüzenet: Cannot be empty

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `alfanum.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `kepesitovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írjál kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(