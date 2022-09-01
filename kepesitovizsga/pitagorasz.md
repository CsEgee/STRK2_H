## Feladat: A Pitagorasz-tétel

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be a Pitagorasz tétel app-ot a http://selenium.oktwebs.training360.com/5201_kepesitovizsga/pitagorasz.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Pitagorasz tétel app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat!

### TC_001: Helyes kitöltés esete:
    * a: 3
    * b: 4
    * c: 5

### TC_002: Illegális karakterek esete:
    * a: a
    * b: 4
    * c: NaN	

### TC_003: Illegális karakterek esete:
    * a: 3
    * b: b
    * c: NaN
	
### TC_004: Üres beviteli mezők esete:
    * a: <üres>
    * b: <üres>
    * c: NaN

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `pithagorasz.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `kepesitovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írjál kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(