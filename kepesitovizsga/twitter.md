# Feladat: Twitter klón tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a Twitter klón alkalmazást a http://selenium.oktwebs.training360.com/5201_kepesitovizsga/twitter.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Twitter klón alkalmazás tesztelését.
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat!


### TC_001: Új tweet felvétele:
    * What's happening: New twitter post arrived
    * Tweet gomb megnyomása
	* Ellenőrizd, hogy az új bejegyzés megjelent a tweet listában

### TC_002: Követés beállítása:
	* Alaphelyzetből indulunk
    * Who to follow listából: CN kiválasztása és Follow aktiválása
    * Ellenőrizd, hogy a Following listában CN megjelent	

### TC_003: Követés megszüntetése:
	* Alaphelyzetből indulunk
    * Following listából: PN kiválasztása és Unfollow aktiválása
    * Ellenőrizd, hogy a Who to follow listában PN megjelent
	

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `twitter.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `kepesitovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írjál kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(