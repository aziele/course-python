## Zad. 1
Napisz program `common_aa.py`, który poprosi użytkownika o wpisanie dwóch sekwencji białkowych i wyświetli w porządku alfabetycznym wszystkie wspólne aminokwasy między sekwencjami.

```
Enter 1st protein sequence: MKSTGYWTRSFVCDH
Enter 2nd protein sequence: MGTYWSSQEG
```

Wynik:

```
['G', 'M', 'S', 'T', 'W', 'Y']
```


## Zad. 2
W trzech plikach [cancer1.txt](../data/cancer1.txt), [cancer2.txt](../data/cancer2.txt) i [control.txt](../data/control.txt) znajdują się nazwy genów, które wykazują podwyższony poziom ekspresji, odpowiednio, u pacjentów z nowotworem skóry, białaczki i ludzi zdrowych.

Utwórz program `common_genes.py`, który wyszuka geny charakterystyczne jedynie dla pacjentów chorych na oba typy raka (i których nie ma w control) i zapisze je do pliku tekstowego `cancer_common.txt`

Input:

```
cancer1.txt     cancer2.txt       control.txt
-----             -----             -----
gene1             gene3             gene1
gene2             gene4             gene3
gene3             gene2             gene5
```

Output:

```
cancer_common.txt
-----
gene2
```

## Zad. 3
W pliku [virus_genomes.fasta](../data/virus_genomes.fasta) znajdują się sekwencje genomowe 100 wirusów w formacie FASTA. Utwórz program `summary_genomes.py`, który wczyta wszystkie sekwencje, obliczy podstawowe statystyki dla każdego genomu i zapisze wyniki do pliku `virus_genomes.tsv`.

Output:

```
id          length	gc_percent	n_percent
X15511.1	4733	49.9472	0.0211
EU877232.1	88487	38.8938	0.0011
MN853672.1	9651	42.5863	0.0207
KJ591604.1	132541	36.0273	0.0030
...
```

gdzie:

* `virus_id` - identyfikator sekwencji — tekst znajdujący się od znaku > do pierwszej spacji
* `length` - długość sekwencji (liczba nukleotydów)
* `gc_percent` - procent nukleotydów G + C w sekwencji (GC / length * 100)
* `n_percent` - procent nukleotydów N w sekwencji (N / length * 100)