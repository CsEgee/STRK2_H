## Feladat: Tic Tac Toe alkalmazás tesztelése

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a Tic Tac Toe app-ot a http://selenium.oktwebs.training360.com/7709_zarovizsga/tic_tac_toe.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Tic Tac Toe app tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### TC_001: Megjelenés és beállítások:
    * Az alaphelyzetben megjelenő táblán ellenőrizd, hogy minden cella/gomb `?` karaktert tartalmaz
	* Ellenőrizzük, hogy ha a Win Size mezőbe nagyobb értéket állítunk be, mint a Board Size mezőbe, akkor alert hibaüzenetet kapunk. 
	Ennek minden reális (maximum 50) Board Size és Win Size érték esetén működnie kell.
    
### TC_002: Játék működésének tesztelése:
    * Bármelyik sorba vigyünk be a Win Size-nak megfelelő számú azonos karaktert egymás mellé.
    * Ellenőrizzük, hogy egy alert üzenetben a Game Over szavakkal kezdődő üzenetet kapunk.


## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `tic_tac_toe.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `zarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(