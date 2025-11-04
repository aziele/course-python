## Zad. 1
Napisz program `square_list.py`, który za pomocą funkcji `range` i pętli `for` utworzy listę kwadratów liczb od 1 do 15.

```
$ python square_list.py
```

Wynik:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
```


## Zad. 2
Utwórz program `gene_list.py`, umieść w nim poniższą listę nazw genów i dodaj instrukcje, które odpowiedzą na poniższe pytania:

```python
genes = ['lacZ', 'araC', 'trpA', 'recA', 'tnrc6b', 'tnrc6a']
```

1. Wyświetl pierwszy i ostatni gen.
2. Sprawdź, czy w liście znajduje się `'recA'`.
3. Dodaj do listy gen `'rpoB'` i posortuj listę alfabetycznie.
4. Usuń `'araC'` z listy.
5. Wyświetl długość listy i jej końcową zawartość.


## Zad. 3
Utwórz program `seq_list.py`, umieść w nim poniższą listę sekwencji i dodaj instrukcje, które odpowiedzą na poniższe pytania:

```python
sequences = ['ATGCGT', 'ATGCTGA', 'TTGGA', 'ATGC']
```

1. Utwórz nową listę `lengths`, zawierającą długości poszczególnych sekwencji.
2. Oblicz sumę długość sekwencji.
3. Oblicz średnią długość sekwencji.


## Zad. 4
Utwórz program `mutate.py`, który w poniższej sekwencji, wprowadzi substytucję nukleotydu w 3 pozycji (`G` → `A`)

```python
dna = 'ATGCTGA'
```

Wynik:

```
ATACTGA
```


## Zad. 5
Utwórz program `filter_seq.py`, który ma poniższą listę sekwencji DNA:

```python
sequences = ['ATGCGT', 'ATG', 'ATGCTGA', 'TTGGA', 'A']
```

Zapytaj użytkownika o minimalną długość sekwencji. Wyświetl tylko te sekwencje, które są równe lub dłuższe od podanej długości.

```
$ python filter_seq.py
Enter minimum length: 5
```

Wynik:

```
ATGCGT
ATGCTGA
TTGGA
```

## Zad. 6
Przyporządkuj odpowiednie wyrażnie po prawej do odpowiedniej strzałki. Swoją odpowiedź umieść w pliku `list_methods.py` w formie kodu Pythona lub jako komentarz podając numery wyrażeń w odpowiedniej kolejności.

![list.png](../images/list.png)



## Zad. 7
Utwórz program `rev_comp.py`, który w opariu o pętle `for` i instrukcje `if` wyświetli w jednej linii sekwencję komplementarną do sekwencji podanej przez użytkownika.

```python
seq = input("Enter a DNA sequence: ")

# ATGCAATC  <-- sekwencja użytkownika
# GATTGCAT  <-- sekwencja (odwrotnie) komplementarna
```


## Zad. 8
Napisz program `sort_genes.py`, który poprosi użytkownika o podanie nazw genów rozdzielonych spacją lub przecinkiem, a następnie wyświetla je w osobnych wierszach w kolejności alfabetycznej.

```
Enter gene names: BRCA1 TP53,EGFR,MYC KRAS GW182
```

Wynik: 

```
BRCA1
EGFR
GW182
KRAS
MYC
TP53
```
