# Feladat: Speciális számok kiválasztása

Nevezzük speciálisnak azokat a számokat, amelyek `11` többszörösei (másként fogalmazva oszthatók `11`-el) vagy pont `1`-el nagyobbak, mint `11` valamelyik többszöröse.

írj egy olyan Python függvényt, ami megkapja a tesztelendő számot paraméterként és visszaadja, hogy a kérdéses szám az speciális-e vagy nem. Ezt igen/nem formájában várjuk!

```Python
special_eleven(22) -> True
special_eleven(23) -> True
special_eleven(24) -> False
```

Próbáld ki a függvényed az alábbi számokra:
```
23, 24, 122, 96
```

### Tanácsok a megoldáshoz:
* Fontos, hogy függvényt adj be!
* Fontos, hogy legyen bekérés a felhasználótól a konzolon keresztül.
* Ne gondold túl! Nem kell ellenőrizni, hogy a bemenet csak egész szám legyen!
* Bármilyen megoldás, ami a fenti teszt adatokra (és hasonló tesztadatokra) a helyes megoldást adja tökéletesen megfelel.
* Nincs pontlevonás ha `lehetne ezt egyszerűbben is`.
* Nincs plusz pont ha `kevesebb sorból oldod meg`.


### A megoldás beadása
A megoldást egy `specialis.py` nevű fájlban kell beadnod! 
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `felezovizsga` nevű mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása (`ctlr`+`alt`+`l`).
* Akkor is add be megoldásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű, a tárgyhoz kötődő kód beadása.
* A megoldás fájlba írj kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* Nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér. :(
