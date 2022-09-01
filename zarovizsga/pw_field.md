## 4 Feladat: Password mező validációjának tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be a Password mező app-ot a http://selenium.oktwebs.training360.com/7709_zarovizsga/pw_field.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a password mező tesztelését.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

A cél a password mező validáció tesztelése:

### TC_001: Helyes kitöltés esete:
	* Username mező: admin
    * Password mező: aB12aB12
    * A felbukkanó panelen a jelszó minden feltételnek megfelel. 

### TC_002: Csak kisbetűk a jelszóban:
	* Username mező: admin
    * Password mező: asdfghjk
    * A felbukkanó panelen a jelszó csak a kisbetű és a karakterszám feltételnek felel meg.

### TC_003: Csak nagybetűk a jelszóban:
	* Username mező: admin
    * Password mező: ASDFGHJK
    * A felbukkanó panelen a jelszó csak a nagybetű és a karakterszám feltételnek felel meg.
	
### TC_004: Csak számok a jelszóban:
	* Username mező: admin
    * Password mező: 12345678
    * A felbukkanó panelen a jelszó csak a szám és a karakterszám feltételnek felel meg.

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `pw_field.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `zarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(