## Feladat: Keressük a kör területét

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a kör terület számító app-ot a http://selenium.oktwebs.training360.com/7709_zarovizsga/kor_terulete.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kör terület számító appban:

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### TC_001: Helyes kitöltés esete:
    * r: 10
    * Eredmény: 314

### TC_002: Negatív számmal történő kitöltés esete:
    * r: -5
    * Eredmény: Alert jelenik meg `A kör sugara nem lehet negatív szám!` üzenettel

### TC_003: Nem számokkal történő kitöltés esete:
    * r: abrakadabra
    * Eredmény: NaN   

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `kor_terulete.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `zarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(
