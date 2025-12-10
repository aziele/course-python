## Zad. 1
Użyj listy składanej, aby z poniższej listy utworzyć listę liczb parzystych większych od 10.

```python
input_list = [4, 50, 51, 10, 21, 5, 11, 12, 16]
```

Output:

```python
output_list = [50, 12, 16]
```


## Zad. 2
Zmodyfikuj poniższą funkcję stosując składnię listy składanej.

```python
def complement(dna):
    """Return a complementary DNA sequence"""
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    cdna = []
    for nt in dna.upper():
        cdna.append(d.get(nt, 'N'))
    return "".join(cdna)
```


## Zad. 3
Plik [genes.txt](../data/genes.txt) zawiera nazwy genów (po jednym w wierszu). Użyj listy składanej, aby utworzyć listę genów, których nazwa ma co najmniej 6 znaków.


## Zad. 4
Zapoznaj się z funkcjami `random.choice()` i `random.randint()` uruchamiając poniższy kod.

```python
import random

for i in range(10):
    print(random.choice(['DNA', 'RNA', 'protein']))
    print(random.randint(1, 10))
```

Następnie utwórz funkcję `mutate()`, która w sekwencji DNA wprowadzi jedną losową *substytucję* nukleotydu na losowej pozycji.

Na przykład:

```python
mutseq = mutate('ATGCG')
print(mutseq)               # ACGCG

mutseq = mutate('ATGCG')    # ATGCT
print(mutseq)
```


## Zad. 5* (dla chętnych)
<img align="right" src="../images/book-blindwatchmaker.jpg" alt="BlindWatchmaker" height="270px"> W książce "Ślepy zegarmistrz" Richard Dawkins zaprezentował symulację komputerową, która przedstawia działanie doboru naturalnego w zakresie tworzenia złożonych form biologicznych poprzez losowe mutacje. Symulacja zaczyna się od przypadkowej sekwencji liter i stopniowo przekształca się w sentencję z sztuki *Hamlet* **METHINKS IT IS LIKE A WEASEL** (*Zdaje mi się, że jest podobniejsza do łasicy*).

Napisz program `weasel.py`, który przeprowadzi procedurę Dawkinsa:

1. Wygeneruj losową sekwencję długości 28 znaków (alfabet: 26 liter i spacja).
2. Utwórz 100 kopii tej sekwencji (*reprodukcja*).
3. W każdej kopii sekwencji w jednym losowym miejscu zastąp znak innym przypadkowym znakiem z alfabetu (*mutacja*).
4. Określ, która z 100 kopii sekwencji jest najbardziej zbliżona do docelowej sekwencji METHINKS IT IS LIKE A WEASEL. W tym celu możesz obliczyć dystans Hamminga (liczbę pozycji w sekwencji niezgodnych z sekwencją docelową).
5. Zakończ program jeżeli któraś z 100 kopii sekwencji jest identyczna do hamletowskiej sentencji. W przeciwnym przypadku, wybierz jedną sekwencję, która wykazuje największe podobieństwo i przejdź do kroku 2.

Przykładowy output:

```
TATTIYAKXWTXTFTDXQHOFOYLPTLN  1
TATTIYAK WTXTFTDXQHOFOYLPTLN  2
TATTIYAK WTXTFTDXQHOF YLPTLN  3
TATTIYAK WTXTFTDXQEOF YLPTLN  4
TATTIYAK WTXTFTDXQE F YLPTLN  5
MATTIYAK WTXTFTDXQE F YLPTLN  6
...
METHINKS IT IS LIKE A WEASEL  N
```

Odpowiedz na pytania:

1. Ile pokoleń potrzebnych jest do wygenerowania docelowej sekwencji?
2. Czy symulacja Dawkinsa trafnie odwzorowuje działanie ewolucji? (dla chętnych)