# Feladat: Matek app tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 

A program töltse be a Matek app-ot a http://selenium.oktwebs.training360.com/7709_zarovizsga/matek_app.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Matek app tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

A feladatod, hogy a random számokkal és random operátorokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a három operandust (számot) és a két operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban. 

### TC_001: Teszteld le, hogy helyesen jelenik-e meg az applikáció:
    * Egy matematikai képletet látsz, aminek a jobb oldalán egy kérdőjellel jelöltük a keresett eredményt, pl 3866-5434*160 = ?    
    * Az eredmény kezdetben üres, nincs érték mellette.
	* A kalkuláció gomb klikkelhető.	

### TC_002: Ellenőrizd a Kalkuláció gomb működését:
	* Az oldalt megnyitva, majd többször egymás után (legalább 3-szor) megnyomva a Kalkuláció gombot, mindig ugyanaz az eredmény. (Tehát a gombnyomások között itt nem frissítjük az oldalt.)
	
### TC_003: Az alkalmazás újratöltése és a kalkuláció elvégzése
    * Frissítsd 10-szer az oldalt, és minden alkalommal végezd el a random képlet műveletét a Kalkuláció gomb megnyomásával.
	* Ellenőrizd, hogy a számítás minden frissítés után helyes eredményre vezet.
	
## Tipp
	* Ha megakadsz és nem ugrik be a megoldás, nézz körül a python eval() függvény táján. Természetesen az eval() függvény nélkül is megoldható a feladat.

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `matek_app.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `zarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(