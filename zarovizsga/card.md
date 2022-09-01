# Feladat: Kártya

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a Kártya alkalmazást a http://selenium.oktwebs.training360.com/7709_zarovizsga/card.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Kártya alkalmazás tesztelését, aminek keretében megvizsgáljuk, hogy mennyire sikerült a véletlenszerű működést megvalósítani.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert` összehasonlításokat használj!

### TC_001: A weboldal működése
 * 10 kártyahúzás után az utolsó kártya és a kártya történelem utolsó elemének összehasonlítása. 

### TC_002: Random működés statisztikai ellenőrzése 
Végezzünk 40 kártyahúzást. Az így kapott kártya történelem elemeit gyűjtsük össze, és számoljuk meg, hány pikk kártyát kaptunk. Az assertben vizsgáljuk meg, hogy az elméleti 10 pikk kártya számhoz képest bent vagyunk-e a 9 és 11 határok között. 
 * Vizsgált kártya: pikk, azaz "♠"
 * Kártyahúzás: 40
 * Tesztelt határok: 9 és 11, a határértékeket beleértve
 * (Amennyiben nem esünk bele a 9 és 11 határértékek közé, akkor az azt jelzi, hogy a kártyahúzás random algoritmusa nem megbízható.)


## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `card.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `zarovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írj kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(