## 1. feladat: Kalkulátor automatizálása

Készíts egy python alkalmazást (egy darab python fájlt), ami selenium-ot használ! 

A program töltse be a bmi kalkulátor app-ot a http://selenium.oktwebs.training360.com/probavizsga/bmi.html oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a kalkulátorban:

Underweight:
* height: 171 cm
* weight: 45 kg
* Elvárt értékek:
    * Your BMI is: 15
    * This means you are: Underweight

Normal:
* height: 185 cm
* weight: 65 kg
* Elvárt értékek:
    * Your BMI is: 19
    * This means you are: Normal

Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl. a pytest).
Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.

### A megoldás beadása
A megoldást egy `bmi.py` nevű fájlban kell beadnod!
Az említett python fájlt és benne a megoldásodat a `hf-tesztelo-strk2-halado` szervezet alá létrehozott `vezeteknev_keresztnev` privát github repodban egy `probavizsga` nevű mappába helyezd el!

* Ne felejtsd el, hogy pontokat ér a szintaktikai konvenciók megvalósítása. (`ctlr`+`alt`+`l`)
* Akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód.
* A megoldás fájlba írj kommentet, amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
* Nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér.