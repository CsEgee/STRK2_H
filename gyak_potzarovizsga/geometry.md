# Feladat: Geometria app validálása

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ.
A program töltse be Geometria app-ot a http://selenium.oktwebs.training360.com/7904_potzarovizsga/geometry.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Geometria app tesztelését.

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!


### TC_001: Alapállapot tesztelése:
    * Betöltés után ellenőrizzük, hogy az Alap és Magasság input mezők üresek!
	* Ellenőrizzük, hogy a gombok alatt nincs semmiféle felirat!
    
### TC_002: Háromszög területének kiszámítása (alap * magasság / 2)
    * Alap: 5
    * Magasság: 4
	* Háromszög terület gomb aktiválása
	* Várt eredmény: Háromszög területe: 10, Rombusz területe: <üres>
	
### TC_003: Háromszög és rombusz területének kiszámítása (alap * magasság / 2, alap * magasság)
    * Alap: 7
    * Magasság: 5
	* Háromszög terület gomb aktiválása
	* Rombusz terület gomb aktiválása
	* Várt eredmény: Háromszög területe: 17.50, Rombusz területe: 35
	

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `geometry.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `potzarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(