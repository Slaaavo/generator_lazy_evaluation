
# Obsah dnesnej prednasky
## 1. Iterator a generator
## 2. Lenive vyhodnocovanie (Lazy evaluation)

# Iterator a Generator

inspirovane http://www.python-course.eu/python3_generators.php

# Iterator
* je objekt, ktory ma funkciu `__next__` a funkciu `__iter__`, ktora vracia `self`
* je to vseobecnejsi pojem ako generator
* da sa pouzivat na iterovanie cez kolekciu bez toho, aby sme vedeli aka je jej vnutorna struktura. Staci definovat funkciu `__next__`. Podobny koncept sa da najst vo vela jazykoch. Napriklad aj v Jave.

# Iterator sa napriklad implicitne pouziva pri prechadzani kolekcii for cyklom


```python
cities = ["Paris", "Berlin", "Hamburg", "Frankfurt", "London", "Vienna", "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)
```

    location: Paris
    location: Berlin
    location: Hamburg
    location: Frankfurt
    location: London
    location: Vienna
    location: Amsterdam
    location: Den Haag



```python
dir(cities.__iter__())
```




    ['__class__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__iter__',
     '__le__',
     '__length_hint__',
     '__lt__',
     '__ne__',
     '__new__',
     '__next__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__subclasshook__']




```python
print(type(cities.__iter__()))
print(type(cities.__iter__().__iter__()))
print(cities.__iter__().__next__())
```

    <class 'list_iterator'>
    <class 'list_iterator'>
    Paris


# Rovnako sa pouzivaju iteratory aj pri prechadzani inych kolekcii


```python
capitals = { "France":"Paris", "Netherlands":"Amsterdam", "Germany":"Berlin", "Switzerland":"Bern", "Austria":"Vienna"}
for country in capitals:
    print("The capital city of " + country + " is " + capitals[country])
```

    The capital city of France is Paris
    The capital city of Austria is Vienna
    The capital city of Switzerland is Bern
    The capital city of Germany is Berlin
    The capital city of Netherlands is Amsterdam


# Generator
* kazdy generator objekt je iterator, ale nie naopak
* tento pojem sa pouziva na pomenovanie funkcie (generator funkcia) ako aj jej navratovej hodnoty (generator objekt)
* generator objekt sa vytvara volanim funkcie (generator funkcie), ktora pouziva `yield`


# Generator pouziva vyraz `yield` na zastavenie vykonavania a na vratenie hodnoty

* Vykonavanie sa spusta folanim funkcie `next()` (alebo metody `__next__()`)
* Dalsie volanie zacina od posledneho `yield`
* Medzi volaniami sa hodnoty lokalnych premennych uchovavaju.

## Pozor, toto nieje ten isty `yield` ako je v Ruby
* V Ruby je `yield` volanie bloku asociovaneho s metodou
* V Ruby je nieco podobne generatorom napriklad trieda `Enumerator`

[http://stackoverflow.com/questions/2504494/are-there-something-like-python-generators-in-ruby](http://stackoverflow.com/questions/2504494/are-there-something-like-python-generators-in-ruby)


```python
def city_generator():
    yield "Konstanz"
    yield "Zurich"
    yield "Schaffhausen"
    yield "Stuttgart"
```


```python
gen = city_generator()
```


```python
next(gen)
```

# Vo vnutri generator funkcie mozem pouzivat cyklus


```python
cities = ["Konstanz", "Zurich", "Schaffhausen", "Stuttgart"]
def city_generator():
    for city in cities:
        yield city
gen = city_generator()
```


```python
next(gen)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-36-8a6233884a6c> in <module>()
    ----> 1 next(gen)
    

    StopIteration: 


# Generator funkcia moze prijmat parametre


```python
def city_generator(local_cities):
    for city in local_cities:
        yield city
gen = city_generator(["Konstanz", "Zurich", "Schaffhausen", "Stuttgart"])
```


```python
next(gen)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-42-8a6233884a6c> in <module>()
    ----> 1 next(gen)
    

    StopIteration: 


# Trik ako napisat generator, ktory velmi casto funguje

Uloha: Mame sekvenciu cisel a chceme vytvorit pohyblivy priemer dvoch po sebe nasledujucich cisel pre celu sekvenciu.

napr:

sekvencie = [1,2,3,4,5]

phyblivy priemer = [(0+1)/2, (1+2)/2, (2+3)/2, (3+4)/2, (4+5)/2] = [0.5, 1.5, 2.5, 3.5, 4.5]

# Ako by ste to napisali imperativne ak to chcete len zapisat do konzoly?


```python
sequence = [1,2,3,4,5]
previous = 0
for actual in sequence:
    print((actual + previous) * 0.5)
    previous = actual
```

# Zabalim to do funkcie


```python
sequence = [1,2,3,4,5]
def moving_average(sequence):
    previous = 0
    for actual in sequence:
        print((actual + previous) * 0.5)
        previous = actual
moving_average(sequence)
```

# Vymenim print za `yield`


```python
sequence = [1,2,3,4,5]
def moving_average(sequence):
    previous = 0
    for actual in sequence:
        yield (actual + previous) * 0.5
        previous = actual
print(list(moving_average(sequence)))
```

    [0.5, 1.5, 2.5, 3.5, 4.5]


# Pomocou generatoru by sa dala napriklad spravit funkcia `map`


```python
def map(f, seq):
    for x in seq:
        print(f(x))
```


```python
def map(f, seq):
    for x in seq:
        yield f(x)
```

# Porovnajte si ako by vyzerala implementacia `map` v python2 a python3


```python
def map(f, seq): # V pythone 2 map vracia list, implementacia by mohla byt napriklad takato
    result = []
    for x in seq:
        result.append(f(x))
    return result 
```


```python
def map(f, seq): # V pythone 3 map je generator a zabera konstantne mnozstvo pamati
    for x in seq:
        yield f(x)
```

# Niektore generatory sa daju nahradit funkciou `map`


```python
a, b = 1, 10
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(a, b)
print(generator)
print(next(generator))
print(list(generator))
```

    <generator object squares at 0x7f37353cafc0>
    1
    [4, 9, 16, 25, 36, 49, 64, 81]



```python
generator = map(lambda i: i*i, range(a, b))
print(generator)
print(next(generator))
print(list(generator))
```

    <map object at 0x7f373537ca20>
    1
    [4, 9, 16, 25, 36, 49, 64, 81]


# List comprehension tiez moze vytvarat generator


```python
generator = (i*i for i in range(a, b))
print(generator)
print(next(generator))
print(list(generator))
```

# Explicitny generator ma ale vacsiu vyjadrovaciu silu

Nieje obmedzeny len na formu:



```python
def generator(funkcia, iterator):
    for i in iterator:
        yield funkcia(i)
```

# Na co je to cele dobre?

# Lenive vyhodnocovanie - Lazy evaluation

# Strategie vyhodnocovania

## Skratene vyhodocovanie (Short-circuit)
## Lenive vyhodnocovanie (Lazy)
## Netrpezlive vyhodocovanie (Eager)
## Ciastocne vyhodocovanie (Partial)
## Vzdialene vyhodocovanie (Remote)

https://en.wikipedia.org/wiki/Evaluation_strategy

# Skratene vyhodnocovanie


```python
pole = []
def fun1(pole):
    pole.append('1')
    return False

def fun2(pole):
    pole.append('2')
    return True

if fun1(pole) or fun2(pole):
    pass
print(pole)
```

    ['1', '2']


# Lenive vyhodocovanie

Oddaluje vyhodnocovanie az do doby, ked je to treba


```python
pom = (x*x for x in range(5))
next(pom) #prvok z generatora sa vyberie az ked ho je treba a nie pri vytvoreni generatora
```

# Nedockave vyhodocovanie
Opak leniveho vyhodnotenia. Vyraz sa vyhodnoti hned ako je priradeny do premennej


```python
pom = [x*x for x in range(5)]
pom[4] # vyraz sa hned vyhodnocuje cely
```

## Vyhody
* programator moze kontrolovat poradie vykonavania
* nemusi sledovat a planovat poradie vyhodnocovania

## Nevyhody
* neumoznuje vynechat vykonavanie kodu, ktory vobec nieje treba
* neda sa vykonavat kod, ktory je v danej chvili dolezitejsi
* programator musi organizovat kod tak, aby optimalizoval poradie vykonavanie 

Moderne kompilatory ale uz niektore veci vedia optimalizovat za programatora

# Vzdialene vyhodnocovanie

* Vyhodnocovanie na vzdialenom pocitaci. 
* Hociaky vypoctovy model, ktory spusta kod na inom stroji.
* Client/Server, Message passing, MapReduce, Remote procedure call (RCP)

# Partial evaluation

* Viacero optimalizacnych strategii na to aby sme vytvorili program, ktory bezi rychlejsie ako povodny program.
  * Napriklad predpocitavanie kodu na zaklade dat, ktore su zname uz v case kompilacie.
  * Mamoization (Memoizacia?) - nevykonavanie (cistych) funkcii s rovnakymi vstupmi opakovane
  * Partial application - fixovanie niektorych parametrov funkcie a vytvorenie novej s mensim poctom parametrov.

# Lenive vyhodnocovanie moze zrychlit vyhodocovanie


```python
%%time
print(2+2)
```

    4
    CPU times: user 33 µs, sys: 8 µs, total: 41 µs
    Wall time: 54.6 µs



```python
%%time
import time
def slow_square(x):
    time.sleep(0.2)
    return x**2

generator = map(slow_square, range(10))
print(generator)
```

    <map object at 0x7f37353c04a8>
    CPU times: user 58 µs, sys: 0 ns, total: 58 µs
    Wall time: 66.3 µs



```python
%%time
print(list(generator))
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    CPU times: user 1.37 ms, sys: 348 µs, total: 1.71 ms
    Wall time: 2 s



```python
%%time
generator = map(slow_square, range(10))
pole = list(generator)
print(pole[:5])
```

    [0, 1, 4, 9, 16]
    CPU times: user 2.16 ms, sys: 0 ns, total: 2.16 ms
    Wall time: 2 s



```python
def head(iterator, n):
    result = []
    for _ in range(n):
        result.append(next(iterator))
    return result
```


```python
%%time

print(head(map(slow_square, range(10)), 5))
```

    [0, 1, 4, 9, 16]
    CPU times: user 1.71 ms, sys: 0 ns, total: 1.71 ms
    Wall time: 1 s



```python
%%time
from itertools import islice
generator = map(slow_square, range(10000))
print(list(islice(generator, 5)))
```

    [0, 1, 4, 9, 16]
    CPU times: user 0 ns, sys: 0 ns, total: 0 ns
    Wall time: 1 s


# Lenive vyhodnocovanie setri pamat


```python
from operator import add
from functools import reduce

reduce(add, [x*x for x in range(10000000)])
reduce(add, (x*x for x in range(10000000)))
```


```python
from functools import reduce
import gc
import os
import psutil
process = psutil.Process(os.getpid())

def print_memory_usage():
    print(process.memory_info().rss)

counter = [0] # Toto je hnusny hack a slubujem, ze nabuduce si povieme ako to spravit lepsie. Spytajte sa ma na to! 
def measure_add(a, result, counter=counter):
    if counter[0] % 2000000 == 0:
        print_memory_usage()
    counter[0] = counter[0] + 1
    return a + result
```


```python
gc.collect()
counter[0] = 0
print_memory_usage()
print(reduce(measure_add, [x*x for x in range(10000000)]))
```

    35061760
    441720832
    441720832
    441720832
    441720832
    441720832
    333333283333335000000



```python
gc.collect()
counter[0] = 0
print_memory_usage()
print(reduce(measure_add, (x*x for x in range(10000000))))
```

    35811328
    35811328
    35811328
    35811328
    35811328
    35811328
    333333283333335000000


# Ani ked su funkcie povnarane do seba a kolekcia sa predava ako parameter, nikdy nieje cela v pamati
map, filter, reduce aj list comprehension vnutorne pracuju skolekciami ako s iteratormi


```python
gc.collect()
counter[0] = 0
print_memory_usage()
print(reduce(measure_add, map(lambda x: x*x, range(10000000))))
```

# Ked vieme, ze generator sa vyhodnocuje lenivo, tak nam nic nebrani vlozit do neho nekonecny cyklus


```python
def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        
f = fibonacci()
```


```python
print(list(islice(f, 10)))
```

    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Voila, nekonecna datova struktura, ktora nezabera skoro ziadnu pamat dokedy ju nechcem materializovat celu.


```python
list(fibonacci()) # toto netreba pustat
```

# Vedeli by ste to pouzit na:
* generator prvocisel?
* citanie z velmi velkeho suboru, ktory vam nevojde do pamati?
* citanie dat z nejakeho senzoru, ktory produkuje kludne nekonecne mnozstvo dat?

# Dalo by sa to pouzit napriklad na cakanie na data
Predstavte si, ze mate subor, do ktoreho nejaky proces zapisuje logy po riadkoch a vy ich spracovavate.

Ako by ste spravili iterovanie cez riadky suboru tak, aby ste cakali na dalsie riadky a dojdete na koniec suboru?

inspirovane - http://stackoverflow.com/questions/6162002/whats-the-benefit-of-using-generator-in-this-case


```python
%%bash
echo -n 'log line' > log.txt
```


```python
import time
```


```python
# s generatorom napriklad takto
def read(file_name):
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

lines = read("log.txt")
print(next(lines))
```

    log line



```python
print(next(lines))
```

    next line
    



```python
for line in lines:
    print(line)
```

    next line
    
    next line
    
    next line
    
    next line
    
    next line
    



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-64-b5dd17cf8202> in <module>()
    ----> 1 for line in lines:
          2     print(line)


    <ipython-input-62-bf9f113a8cae> in read(file_name)
          5             line = f.readline()
          6             if not line:
    ----> 7                 time.sleep(0.1)
          8                 continue
          9             yield line


    KeyboardInterrupt: 


# Toto by som vedel spravit aj bez generatora ale ...
* nemal by som oddelenu logiku cakania a spracovavania riadku
* nevedel by som priamociaro znovupouzivat generator vzdy by som to musel kodit odznova 
  * jedine, ze by som pouzil funkciu ako parameter
  * stale tam ale zostava problem ako vratit viacero hodnot z jednej funkcie
* nevedel by som pekne transparentne, lenivo iterovat


```python
while True:
        line = logfile.readline()
        if not line:
            time.sleep(0.1)
            continue
        print line
```

# Generator moze byt aj trochu zlozitejsi, napriklad rekurzivny


```python
class Node(object):

    def __init__(self, title, children=None):
        self.title = title
        self.children = children or []
        
tree = Node(
    'A', [
        Node('B', [
            Node('C', [
                Node('D')
                ]),
            Node('E'),
            ]),
        Node('F'),
        Node('G'),
        ])
```


```python
def node_recurse_generator(node):
    yield node
    for n in node.children:
        for rn in node_recurse_generator(n):
            yield rn
        
[node.title for node in node_recurse_generator(tree)]
```




    ['A', 'B', 'C', 'D', 'E', 'F', 'G']



http://stackoverflow.com/posts/7634323/edit

# Ale castokrat sa to da aj bez pouzitia rekurzie

http://stackoverflow.com/questions/26145678/implementing-a-depth-first-tree-iterator-in-python


```python
from collections import deque

def node_stack_generator(node):
    stack = deque([node])
    while stack:
        # Pop out the first element in the stack
        node = stack.popleft()
        yield node
        # push children onto the front of the stack.
        # Note that with a deque.extendleft, the first on in is the last
        # one out, so we need to push them in reverse order.
        stack.extendleft(reversed(node.children))
        
[node.title for node in node_stack_generator(tree)]
```




    ['A', 'B', 'C', 'D', 'E', 'F', 'G']



# Vedeli by ste tieto dva generatory upravit pre binarny strom?

# Rekurzivny generator sa da napriklad pouzit na vyrabanie permutacii


```python
def permutations(items):
    n = len(items)
    if n==0: 
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc
```


```python
for p in permutations('red'): 
    print(''.join(p))
```

    red
    rde
    erd
    edr
    dre
    der



```python
for p in permutations("game"): 
    print(''.join(p) + ", ", end="")
```

    game, gaem, gmae, gmea, geam, gema, agme, agem, amge, ameg, aegm, aemg, mgae, mgea, mage, maeg, mega, meag, egam, egma, eagm, eamg, emga, emag, 

# Spominate si na `from itertools import islice` ?


```python
def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        
print(list(islice(fibonacci(), 5)))
```

    [1, 1, 2, 3, 5]


# Generator generatorov


```python
def firstn(g, n): # generator objekt je paraetrom generator funkcie
    for i in range(n):
        yield next(g)
```


```python
list(firstn(fibonacci(), 10))
```




    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]




```python

```


```python

```
