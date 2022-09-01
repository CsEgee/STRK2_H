### HF átnézés

* S21_linkek.py - A linkek számát a kimenetre kellett írni, nem a fájlba.
* S23_csvfeltoltes.py - Amit írtál az jó, csak kevés. Sajnos pont az érdemi rész hiányzik.
* S24_setdates.py - A date_time_local és a month esetében az ellenőrzéskor nem pontosan azt kaptam, mint az elvárt. Viszont mivel nálam valószínűleg mások a beállítások, ezért csak megjegyzésként írom, hogy date_time_local.send_keys(date_time_local_in.strftime('00%Y/%m/%d%H:%M')) és month.send_keys(month_in.strftime("%Y\t%B")) alkalmazva, HUN beállítások esetén működik.
* S25_edittable.py - Hiányzik a kereső mező és a törlés ellenőrzése. A sorok kitöltésére nagyon találó módot választottál, azzal, hogy a sor első celláját keresed ki, majd a következő webelementre tulajdonképpen egyszerűen csak tab-bal átlépsz. Ez a módszer két sor esetén kezelhető, de több sornál, mindenképpen ciklus, függvény alkalmazása lenne a célravezető.
* S27_formvalidation.py - Nemcsak egy fajta validációs üzenet van egy-egy mezőhöz, azaz több ellenőrzés kellett volna. Mivel többször csinálod ugyanazt, jobb lett volna függvényt használni.
* S29_pagination.py - Amit írtál az jó, csak kevés. Sajnos pont az érdemi rész hiányzik.
