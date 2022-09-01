# Feladat: Egyszerű kalkulátor tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ.
A program töltse be a Calculator app-ot a http://selenium.oktwebs.training360.com/7904_potzarovizsga/calculator.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Calculator app tesztelését. A tesztelés célje, hogy ellenőrizzük a 
kalkulátor működését 27%-os áfa mellett a fizetendő bruttó összeg kiszámításával. 
Szükségünk van az áfa értékére a számlához, tehát nem elegendő a bruttó összeg kiszámítása. 

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### TC_001: Áfa és bruttó összeg számítás árucikkek vásárlásakor:
    * Két árucikkünk van (1-1 darab). Az egyik árucikk nettó értéke 1000 Ft, a másiké nettó 3000 Ft.
    * Számítsuk ki a két árucikk nettó összértéket a kalkulátor segítségével!
	* Számítsuk ki a két árucikk áfa (27%) összegét. (Ebben a kalkulátorban a `%` jel megnyomása a korábban bevitt érték 1 %-át adja vissza.)
	* Ellenőrizzük a kiszámított áfa összeget, a várt összeg 1080 Ft.
	* Számítsuk ki a bruttó értéket, azaz adjuk hozzá a kiszámított nettó összértékhez a kiszámított áfa összeget!
	* Ellenőrizzük a kapott bruttó értéket, a várt érték 5080 Ft.


## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `calculator.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `potzarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(