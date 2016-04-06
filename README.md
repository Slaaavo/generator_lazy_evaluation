1. Vytvorte generator, ktory bude prijmat pole cisel ako parameter a bude postupne vytvarat druhe mocniny tychto cisel.

2. Spravte toto iste pomocou funkcie map.

3. Spravte toto iste pomocou list comprehension.

4. Vyrobte generator, ktory bude cyklicky prechadzat pole a postupne bude vracat jeho prvky. Ked pride na koniec, tak znova zacne odznova.
  
5. Napiste generator, ktory bude vyrabat faktorial stale vacsich a vacsich cisel.

6. Napiste generator, ktory bude postupne vracat cifry cisla vo zvolenej ciselnej sustave. ratajte s tym, ze ciselna sustava nikdy nieje vacsia ako dsiatkova. Vypis cifier zacina od jednotiek.

7. Napiste funckiu, ktora spocita ciferny sucet prvkov cisla N! (! je faktorial) v desiatkovej sustave. Pouzite na to generatory z predchadzajucich uloh. 

8. Vyrobte generator, ktory bude fungovat ako funkcia `range`. Nepouzivajte funkciu range. Funkcia dostva dva alebo 3 vstupne parametre: `start`, `stop` a volitelny `step`. Generator vytvara sekvenciu cisel zacinajucu od hodnoty start po stop a rozdiel medzi dvoma nasledujucimi hodnotami je rovny parametru step

9. Spravte to iste ako v predchadzajucej ulohe ale tak, aby mohol byt krok aj zaporny.

10. Slovnik (dict, asociativne pole, hash tabulka ...) v Pythone ma metodu `items()`, ktora zo slovnika vytvori zoznam dvojic (kluc, hodnota). 
Vdaka tejto mejto metode, sa da iterovat cez dvojice kluc/hodnota v slovniku. Napiste generator, ktory bude simulovat fungovanie tejto metody. 
Pomocka: ak iterujete cez `dict` bez pouzitia `items()`, tak iterujete len cez jeho kluce. 

11. Napiste linearny kongruentny generator pseudonahodnych cisel. [pomocka](https://en.wikipedia.org/wiki/Linear_congruential_generator).
 
12. Napiste generator, ktory bude vyberat nahodne prvky zo zoznamku. Prvky sa mozu opakovat. Pouzite generator pseudonahodnych cisel inicializovany parametrami `pseudorandom(2**31, 1103515245, 12345, 1)`

13. To iste, ako predchadzajuca uloha, ale prvky sa nesmu opakovat.

14. Napiste generator prvocisel

15. Napiste generator prvocisel, ktory si pamata generovane prvocisla a pouziva ich pri vypocte.

16. Pomocou tohto generatora prvocisel apiste funkciu, ktora vam vrate n-te prvocislo v poradi.

17. Napiste generator, ktory bude prijmat dva zoznamy a bude generovat dvojice prvkov vstupnych zoznamov. 
Vzdy dvojicu bude tvoprit n-ty prvok zo vstupnych prvkov.Pre vstupy `[1, 2, 3, 4]` a `['a', 'b', 'c', 'd']` budu vystupy postupne `(1, 'a'), (2, 'b'), (3, 'c') a (4, 'd')`
Pomocka: zo zoznamu spravite iterator pomocou konstruktora iter(). 
Pomocka2: next() moze mat druhy parameter, ktoreho hodnota sa vrati ak uz iterator nema dalsie prvky, ktore by mal vratit. 
V spojeni s operatorom `is` (vrati True ak sa objekty (nie len ich hodnoty) rovnaju) sa tak da kontrolovat, kedy mate skoncit iteraciu.
 
18. Spravte to iste ako v predchadzajucej ulohe, ale pre premenlivy pocet vstupnych iteratorov

19. Napiste generator, ktory budevytvarat casove trojice (hodina, minuta, sekunda) od zaciatku do konca po inkrementoch. Vsetky parametre su definovane ako trojice. Priklad volania `trange((10, 10, 10), (13, 50, 15), (0, 15, 12))` 

20. Na prednaske ste mali ukazku rekurzivneho generatoru, ktory vyrabal vsetky permutacie prvkov zadaneho zoznamu. Upravte tento generator tak, aby vytvaral vsetky `n` prvkove permutacie. 
