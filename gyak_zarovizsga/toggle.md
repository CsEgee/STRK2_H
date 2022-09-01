# Feladat: CSS toggle működésének ellenőrzése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ.
A program töltse be a CSS toggle működését bemutató app-ot a http://selenium.oktwebs.training360.com/7904_potzarovizsga/toggle.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a CSS toggle működését bemutató app tesztelését.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### TC_001: Alap megjelenés tesztelése:
    * Betöltés után látható a `Slide Down Toggle` üzenet és egy Open feliratú gomb.
    * Ellenőrizzük ezek jelenlétét!

### TC_002: A toggle működtetése:
    * Kattintsunk az Open gombra!
    * Ellenőrizzük, hogy a megjelenő fekete panelen a `This is the hidden message` szöveg megjelenik.
	* Kattintsunk a Close gombra!
	* Ellenőrizzük, hogy a betöltéskor megjelenő oldal látszik a felületen!
	(`Slide Down Toggle` üzenet és egy Open feliratú gomb)


## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `toggle.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `potzarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(