# Feladat: Hány másodperces vagy?

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be az életkor kalkulátor app-ot a http://selenium.oktwebs.training360.com/r2d2_felezovizsga/age_calculator.html oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kalkulátorban:

### TC_001:  Vigyázz, a perceket kell ebben a tesztesetben ellenőrizni!
* Bevitel: Enter your age: `39`
* Elvárt eredmény: 
    * Minutes: `20512440`

### TC_002: 
* Bevitel: Enter your age: `<hagyjuk üresen>`
* Elvárt eredmény: 
    * Seconds: `0`

### TC_003: 
* Bevitel: Enter your age: `112`
* Elvárt eredmény: 
    * Seconds: `3534451200`

## Ne gondold túl a dolgot :)
* Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl. a pytest).
* Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
* A TC_001 tesztesetben nem kell feltétlenül kiszedned a táblázat egyes elemeit, van egyszerűbb módja a kért szöveges mező elérésének.
* A többi tesztesetben csak a másodperc szövegmező érdekel minket, a többivel ne foglalkozz!
* Nem kell a megjelenő hibaüzenettel foglalkoznod a TC_002-es esetben.
* Nem kell a kezdeti megjelenést tesztelned, tételezzük fel, hogy ez már tesztelve van egy másik tesztesettel.

## Mindenképpen adj be valamit - tippek
* Selenium webdriverrel megnyitjuk az adott url-t, már jár a pont.
* Kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte.
* Megnyomunk egy gombot, ismét pont jár érte.
* Ellenőrizz `assert` alkalmazásával, vagy `if-else` struktúra és `print` függvény segítségével, megintcsak jár a pont.

### A megoldás beadása
A megoldást egy `age_calculator.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `felezovizsga` mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`).
* Akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása.
* A megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* Nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér. :(