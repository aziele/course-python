## Zad. 1
Utwórz funkcję `complement`, która jako argument przyjmuje sekwencję DNA i zwraca sekwencję komplementarnych nukleotydów.

Input:

```python
cdna = complement('ACTG')
print(cdna)
```

Output:

```
TGAC
```

## Zad. 2
Utwórz funkcję `reverse_complement`, która przyjmuje sekwencję DNA i wewnątrz wywołuje funkcję `complement`, aby zwrócić sekwencję odwrotnie komplementarną.

Input:

```python
rcdna = reverse_complement('ACTG')
print(rcdna)
```

Output:

```
CAGT
```

## Zad. 3
Wykorzystując funkcję `reverse_complement` wygeneruj sekwencje odwrotnie komplementarne do sekwencji z poniższej listy.

Input:

```python
dna_lst = ['CTGACT', 'GCATAGT', 'TAGATTAT', 'CGATGTTTA']
```

Output:

```python
cdna_lst = ['AGTCAG', 'ACTATGC', 'ATAATCTA', 'TAAACATCG']
```

## Zad. 4
Utwórz funkcję `hamming_distance`, która przyjmuje jako argumenty dwie sekwencje równej długości i oblicza między nimi *dystans Hamminga* - liczba miejsc (pozycji), na których dwie sekwencje się różnią.

Input:

```python
seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'
distance = hamming_distance(seq1, seq2)
print(distance)
```

Output:

```
7
```


## Zad. 5
Zapoznaj się poniższym kodem. Następnie utwórz funkcję `lotto`, która przeprowadzi losowanie dużego lotka (*losowanie sześciu różnych liczb z zakresu 1-49*).

```python
>>> import random
>>> random.randint(1, 49)
22
>>> random.randint(1, 49)
3
>>> random.randint(1, 49)
34
```

Output:

```python
>>> lotto()
{32, 34, 5, 10, 11, 16}
>>> lotto()
{4, 11, 45, 47, 49, 31}
```


## Zad. 6
Wytypuj własny zestaw sześciu liczb. Następnie wywołaj funkcję `lotto` milion razy i sprawdź, czy, w którymś losowaniu trafiłeś(aś) "szóstkę".


## Zad. 7
Zmodyfikuj kod, aby prowadził losowanie dużego lotka do momentu, aż wytypowane zostaną Twoje szczęśliwe liczby (skrypt powinien zwrócić numer losowania).


## Zad. 8 (dla chętnych)
Bakterie wykorzystują enzymy restrykcyjne do walki z wirusami. Enzymy restrykcyjne rozpoznają w sekwencjach genomów wirusów palindromowe sekwencje DNA długości od 4 do 12 nukleotydów i w tych miejscach przeprowadzają rozcięcie cząsteczek wirusa. 

Przykładową sekwencją palindromową jest `GATATC`, ponieważ jej sekwencja odwrotnie komplementarna to `GATATC`.

![palindrome](../images/palindrome.jpg)

Utwórz funkcję `restriction_sites`, która przyjmuje dwa argumenty - sekwencję DNA i długość palindromowej sekwencji, następnie w zadanej sekwencji zidentyfikuje pozycje początku i końca wszystkich palindromowych sekwencji o podanej długości. 

> Wskazówka: Niech funkcja `restriction_sites` skorzysta z już istniejącej funkcji `reverse_complement`.

Input:

```python
restriction_sites('TCAATGCATGCGGGTCTATATGCAT', size=4)
```

Output:

```python
[
  [5, 8, 'TGCA'],
  [7, 10, 'CATG'],
  [17, 20, 'TATA'],
  [18, 21, 'ATAT'],
  [21, 24, 'TGCA']
]
```