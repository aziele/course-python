## Zad. 1
Napisz program `celsius.py`, który dla stopni Celsjusza od 0 do 100 wyświetli odpowiedające stopnie Fahrenheita (F = 32 + 9/5 * C).

Wynik:

```
0°C   32.0°F
1°C   33.8°F
2°C   35.6°F
3°C   37.4°F
4°C   39.2°F
5°C   41.0°F
...
```

## Zad. 2
Utwórz pętle `for`, która wyświetli poniższy wynik:

```
1 4 9 16 25 36 49
```


## Zad. 3
Poniższy program wyświetla na ekran wszystkie pozycje adeniny (A) w sekwencji DNA. Niestety kod zawiera **cztery błędy**. Napraw kod, aby działał prawidłowo.

```python
seq = 'ATGCTGACT"
position = 1

for char in seq
    if char = "A":
        print(position)
position = position + 1
```

## Zad. 4
Napisz program `sum_numbers.py`, który poprosi użytkownika o podanie liczby całkowitej *n* i obliczy sumę wszystkich liczb całkowitych z przedziału od 0 do *n-1*. Na przykład, gdy liczba *n* = 4, suma liczb wynosi 1 + 2 + 3 = 6.

```
Enter an integer number: 4
Sum is equal to: 6
```


## Zad. 5
Utwórz program `rev_comp.py`, który w opariu o pętle `for` i instrukcje `if` wyświetli w jednej linii sekwencję komplementarną do sekwencji podanej przez użytkownika.

```python
seq = input("Enter a DNA sequence: ")

# ATGCAATC  <-- sekwencja użytkownika
# GATTGCAT  <-- sekwencja (odwrotnie) komplementarna
```


## Zad. 6
Napisz kod `dinucleotides.py`, który wypisze wszystkie dwunukleotydowe wyrazy znajdujące się w poniższej sekwencji.

```python
dna = 'ATGCTGATGATGAT'
word_size = 2
```

Wynik:

```
AT
TG
GC
CT
TG
GA
AT
TG
GA
AT
TG
GA
AT
```


## Zad. 7
Napisz program `sort_words.py`, który prosi użytkownika o podanie wyrazów rozdzielonych spacją. Program powinien posortować wyrazy w kolejności alfabetycznej.

```
Enter words: Monkey Donkey Dog Cat Parrot Elephant
```

Wynik: 

```
Cat
Dog
Donkey
Elephant
Monkey
Parrot
```


## Zad. 8
Napisz program `mean_word.py`, który obliczy średnią długość wyrazu w poniższym zdaniu.

```python
text = "The Wellcome Trust Sanger Institute is a world leader in genome research."
```

Wynik:

```
Mean word size: 5.1
```


## Zad. 9
Utwórz program `prime_number.py`, który poprosi użytkownika o podanie liczby całkowitej i sprawdzi, czy podana liczba jest liczbą pierwszą.

```
Enter an integer number: 4
```

Wynik:

```
The number 4 is not prime.
```


## Zad. 10 (dla chętnych)
Utwórz program `multiplication_table.py`, który w oparciu o dwie pętle `for` wyświetli na ekranie tabliczkę mnożenia.

```python
1   2   3   4   5   6   7   8   9   10  
2   4   6   8   10  12  14  16  18  20  
3   6   9   12  15  18  21  24  27  30  
4   8   12  16  20  24  28  32  36  40  
5   10  15  20  25  30  35  40  45  50  
6   12  18  24  30  36  42  48  54  60  
7   14  21  28  35  42  49  56  63  70  
8   16  24  32  40  48  56  64  72  80  
9   18  27  36  45  54  63  72  81  90  
10  20  30  40  50  60  70  80  90  100
```


## Zad. 11 (dla chętnych)
Zapis dot-bracket używany jest do tekstowego przedstawienia struktury drugorzędowej cząsteczek RNA.

Przykładowy zapis dot-bracket:

```
.((..(((...)))..((..)))).
```

Utwórz program `dotbracket.py` sprawdzający, czy zapis dot-bracket jest prawidłowy, tj:

* składa się jedynie z nawiasów i kropek,
* liczba nawiasów otwierających i zamykających musi być identyczna,
* każdy nawias otwierający musi mieć swój nawias zamykający.

Przykłady **prawidłowego** zapisu:

```
.((.))..()
.(((...).(...)))
()
.(.).
```

Przykłady **nieprawidłowego** zapisu:

```
.(..)..(.
.(..)..a()..
..()..)(..
(.)))(((.)
```
