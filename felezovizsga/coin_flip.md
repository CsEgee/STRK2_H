# Feladat: Pénzfeldobás csavarral!

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be a pénzfeldobásos alkalmazást a http://selenium.oktwebs.training360.com/r2d2_felezovizsga/coin_flip.html oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat az appban:

### TC_000: Kezdeti értékek, ellenőrzendők, hogy valóban ezek jelennek meg
* Elvárt eredmény: 
    * Money: `100` - nem változtatható, mindig újra kell tölteni az oldalt!
    * Bet: `<üres>`
    * Result: `-`

### TC_001: 
* Bevitel:
	* Money: `100`
    * Bet: `10`
    * Nyomjuk meg a `Tails` feliratú gombot
* Elvárt eredmény: 
    * Result: `heads` vagy `tails`
    * ha eltaláltuk:
        * Money: `110`
    * ha nem találtuk el:
        * Money: `90`

## Ne gondold túl a dolgot :)
* Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl. a pytest).
* Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat!

## Mindenképpen adj be valamit - tippek
* Selenium webdriverrel megnyitjuk az adott url-t, már jár a pont.
* Kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte.
* Megnyomunk egy gombot, ismét pont jár érte.
* Ellenőrizz `assert` alkalmazásával, vagy `if-else` struktúrával és `print` függvény segítségével, megint csak jár a pont. 

### A megoldás beadása
A megoldást egy `coin_flip.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `felezovizsga` nevű mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`).
* Akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása.
* A megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér. :(