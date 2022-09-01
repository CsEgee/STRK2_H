
# Feladat: Pattern alapú szűrés validálása

Készíts egy python alkalmazást (egy darab python file) ami selenium-ot használ. 
A program töltse be a pattern ellenőrző alkalmazást a http://selenium.oktwebs.training360.com/5201_kepesitovizsga/input-pattern.html oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a pattern ellenőrző alkalmazás tesztelését.
Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat!

A cél az egyes pattern input mezők ellenőrző tesztelése:
Mindegyik mező esetén az ellenőrzéshez használt karaktersorozat egységesen a következő
`ab1ef2ij3op4uv5`. Ezt a karaktersorozatot kell az egyes input mezőkbe __karakterenként__ bevinni, és a mezőre beállított szűréseknek megfelelően különböző eredményt kapunk. Az oda nem illeszthető karakterek a bevitel során kimaradnak.


### TC_001: ALPHA ONLY esetén
    * Input mező tartalma: abefijopuv

### TC_002: NUMBER ONLY esetén
    * Input mező tartalma: 12345

### TC_003: ALPHANUMERIC ONLY esetén
    * Input mező tartalma: ab1ef2ij3op4uv5
	
### TC_004: VOWEL ONLY esetén
    * Input mező tartalma: aeiou

## Mindenképpen adj be valamit - tippek
* selenium webdriverrel megnyitjuk az adott url-t, már jár a pont
* kiszedjük a fent említett mezőket szelektorokkal, megint jár a pont érte
* megnyomunk egy gombot, ismét pont jár érte

### A megoldás beadása
A megoldást egy `input_pattern.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `kepesitovizsga` mappába helyezd el!

* ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`)
* akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása
* a megoldás fájlba írjál kommenteket, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül beadott fájlod.
* nem beadott vagy üres fájl formájában beadott feladat megoldás `0` pontot ér :(