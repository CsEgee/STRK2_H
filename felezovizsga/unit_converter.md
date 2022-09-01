# Feladat: Imperial-Metric konverzió

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be az mértékegység konvertáló app-ot a http://selenium.oktwebs.training360.com/r2d2_felezovizsga/unit_converter.html oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a konverterben:

### TC_001: 
* Bevitel: 
    * <első beviteli mező>: `112`
    * <masodik beviteli mező>: `meter`
* Elvárt eredmény: 
    * <harmadik mező>: `367.45 FOOT`

### TC_002: 
* Bevitel: 
    * <első beviteli mező>: `8`
    * <masodik beviteli mező>: `oz`
* Elvárt eredmény: 
    * <harmadik mező>: `236.56 MILLILITER`

### TC_003: 
* Bevitel: 
    * <első beviteli mező>: `1`
    * <masodik beviteli mező>: `gallon`
* Elvárt eredmény: 
    * <harmadik mező>: `3.79 LITER`

## Ne gondold túl a dolgot :)
* Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl. a pytest).
* Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
* Nem kell a kezdeti megjelenést tesztelned, tételezzük fel, hogy ez már tesztelve van egy másik teszt esetttel.

## Mindenképpen adj be valamit - tippek
* Selenium webdriverrel megnyitjuk az adott url-t, már jár a pont.
* Kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte.
* Megnyomunk egy gombot, ismét pont jár érte.
* Ellenőrizz `assert` alkalmazásával, vagy `if-else` struktúra és `print` függvény segítségével, megintcsak jár a pont. 

### A megoldás beadása
A megoldást egy `unit_converter.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `felezovizsga` nevű mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`).
* Akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása.
* A megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* Nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér. :(