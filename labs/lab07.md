## Zad. 1
Utwórz skrypt `palindromes.py`, który wczyta plik [words_alpha.txt](../data/words_alpha.txt) i wyświetli na ekran wszystkie wyrazy które są palindromami składającymi się z co najmniej 6 liter.


## Zad. 2
Plik [Escherichia_coli.tsv](../data/Escherichia_coli.tsv) zawiera lokalizację genów bakterii *Escherichia coli*. Napisz program `ecoli.py`, który obliczy średnią, minimalną i maksymalną długość genu.

Wynik:

```
Min: 42
Avg: 949.8
Max: 7074
```


## Zad. 3
<img align="right" src="../images/Gadsby-book_cover.jpg" alt="Gadsby book cover" height="270px">

Powieść *"Gadsby"* autorstwa Ernesta Vincenta Wrighta to książka w której nie występuje litera *e*. W pliku [gadsby.txt](../data/gadsby.txt) znajduje się ta powieść. Napisz program `gadsby.py`, który sprawdzi, czy w książce rzeczywiście nie występuje litera *e*.

Wynik:

```
Letter e occurrences: ?
```

## Zad. 4
Rozszerz kod programu `gadsby.py`, aby policzyć liczbę wszystkich słów znajdujących się w powieści *Gadsby*.

Wczytaj zawartość całej książki jako łańcuch znaków, usuń wszystkie wystąpienia znaków `. , ? ! ; : " ' - _ () * `. Następnie rozdziel łańcuch znaków na listę słów.

Wynik:

```
Letter e occurrences : ?
Words in total       : ?
```


## Zad. 5
Rozszerz kod programu `gadsby.py`, aby policzyć liczbę różnych słów zawartych w *Gadsby*.

Wynik:

```
Letter e occurrences : ?
Words in total       : ?
Uniq words           : ?
```

## Zad. 6
Rozszerz kod programu `gadsby.py`, aby obliczyć liczbę wystąpień każdego słowa i zapisać wyniki do pliku `gadsby_words.txt`. Słowa powinny być uszeregowane alfabetycznie.

Zawartość pliku `gadsby_words.txt`:

```
count    word
?        a
?        abiding
?        abigail
?        ability
?        abnormality
?        abnormally
?        aboard
...
```


## Zad. 7
W pliku [lotto_history.txt](../data/lotto_history.txt) znajdują się wszystkie historyczne wyniki losowania Dużego Lotka od 27.01.1957 do 15.11.2025. Napisz program `lotto_history.py`, który przedstawi procentowy udział każdej z 49 liczb w odbytych losowaniach.

Wynik:

```
1   ?%
2   ?%
3   ?%
...
47  ?%
48  ?%
49  ?%
```

## Zad. 8
W pliku [NC_045512.fasta](../data/NC_045512.fasta) znajduje się genom wirusa SARS-CoV-2 pochodzący z Wuhan. Utwórz program `covid.py`, który policzy występowanie w genomie wirusa podsekwencji 6-nukleotydowych.

Wynik:

```
ATTAAA  26
TTAAAG  21
TAAAGG  13
AAAGGT  18
AAGGTT  19
AGGTTT  20
GGTTTA  17
GTTTAT  24
TTTATA  14
TTATAC  11
TATACC  6
...
```