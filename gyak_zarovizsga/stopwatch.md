# Feladat: Stopper alkalmazás tesztelése

Készíts egy Python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a Stopper alkalmazást a
 http://selenium.oktwebs.training360.com/7904_potzarovizsga/stopwatch.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Stopper alkalmazás tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### TC_001: Alkalmazás alaphelyzetének tesztelése:
    * Ellenőrizzük, hogy a weboldal megnyitásakor a stopper 00: 00: 00 értéket mutat.
    * Kattintsunk a Start feliratra, majd töltsük újra az oldalt. 
	* Ellenőrizzük ismét, hogy a stopper a kezdőértéket mutatja.


### TC_002: Megállítás x másodpercnél:
	* A Start felirattal indítsuk el a stoppert, és 5 másodperccel később állítsuk le.
	* Írjuk ki a stopper által mutatott időt.
	* Ellenőrizzük, hogy a megállított stopper 4 másodperc és 6 másodperc közötti értéket mutat.
	
### TC_003: Lapszámláló tesztelése:
    * Índítsuk el a stoppert!
	* 5 másodperc elteltével állítsuk le, és nyomjuk meg a Lap feliratot.
    * Ellenőrizzük, hogy a Lap által mutatott idő és a stopperen látható idő egyezik-e.
	

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `stopwatch.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `potzarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(
