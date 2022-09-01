# Feladat: Kő-papír-olló játék tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a Rock, paper, scissors app-ot a http://selenium.oktwebs.training360.com/7904_potzarovizsga/rock_paper_scissors.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Rock, paper, scissors app tesztelését.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### TC_001: Betöltés utáni állapot tesztelése
    * Az oldal bal alsó részén a wins ties lossess total elemek értéke mind `0` kell legyen.

### TC_002: Működés megfelelősége:
    * Végezzünk el egy játékot, a `rock` szimbólumra kattintva.
	* Ellenőrizzük, hogy a játék szabályai szerint a megjelenő Me-CPU listaelem alapján a megfelelő wins ties lossess total értékek jelennek meg.	

### TC_003: Frissitsük az oldalt és hajtsunk végre 5 játékot :
    * Ellenőrizzük, hogy a total elem értéke pontosan 5!
	* Ellenőrizzük, hogy a historyban 5 item elem keletkezett!


## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `rock_paper_scissors.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `potzarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(