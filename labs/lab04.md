## Zad. 1
Napisz program, który prosi użytkownika o podanie wyrazów rozdzielonych spacją. Program powinien posortować wyrazy w kolejności alfabetycznej.

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

## Zad. 2
Napisz program, który obliczy średnią długość wyrazu w poniższym zdaniu.

```python
text = "The Wellcome Trust Sanger Institute is a world leader in genome research."
```

Wynik:

```
Mean word size: 5.2
```


## Zad. 3
Napisz program `common_aa.py`, który poprosi użytkownika o wpisanie dwóch sekwencji białkowych i wyświetli w porządku alfabetycznym wszystkie wspólne aminokwasy między sekwencjami.

```
Enter 1st protein sequence: MKSTGYWTRSFVCDH
Enter 2nd protein sequence: MGTYWSSQEG
```

Wynik:

```
['G', 'M', 'S', 'T', 'W', 'Y']
```


## Zad. 4
Napisz program `molmass.py`, który w oparciu o poniższy słownik obliczy masę molową (kDa) sekwencji białkowej wprowadzonej przez użytkownika.

Masa molowa sekwencji białkowej to suma mas wszystkich aminokwasów znajdujących się w sekwencji. Jeżeli sekwencja użytkownika zawiera znak, którego nie ma w słowniku `protein_weights` to przyjmij, że masa molowa tego znaku to 0. Na przykład, masa molowa sekwencji `MKSX` jest równa 149.2113 + 146.1876 + 105.0926 + 0 = 400.4915

```python
protein_weights = { 
   'A': 89.0932, 
   'C': 121.1582, 
   'D': 133.1027, 
   'E': 147.1293, 
   'F': 165.1891, 
   'G': 75.0666, 
   'H': 155.1546, 
   'I': 131.1729, 
   'K': 146.1876, 
   'L': 131.1729, 
   'M': 149.2113, 
   'N': 132.1179, 
   'O': 255.3134, 
   'P': 115.1305, 
   'Q': 146.1445, 
   'R': 174.201, 
   'S': 105.0926, 
   'T': 119.1192, 
   'U': 168.0532, 
   'V': 117.1463, 
   'W': 204.2252, 
   'Y': 181.1885 
}
```

## Zad. 5
Utwórz skrypt `words.py`, który wyświetli liczbę wystąpień każdego wyrazu w poniższym tekście.

```python
text = 'The first rule of Fight Club is you do not talk about Fight Club'
```

Wynik:

```
of 1
is 1
do 1
the 1
you 1
not 1
rule 1
club 2
talk 1
first 1
fight 2
about 1
```

## Zad. 6
Utwórz program `translate.py`, który w oparciu o poniższy słownik kodonów dokona translacji sekwencji DNA na sekwencję białka.

```python
codons = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
}
```

```
Enter DNA sequence: ATGTACTCTCTAGCGTGA
```

Wynik:

```
MYSLA*
```


## Zad. 7
Utwórz program `dinucleotide.py`, który zliczy dwunukleotydowe podsekwencje występujące w poniższej sekwencji DNA.

```python
dna = 'AGCCCGATGCTTAAACGTAGATTTTCC'
```

Wynik:

```
AA  2
AC  1
AG  2
AT  2
CC  3
CG  2
CT  1
GA  2
GC  2
GT  1
TA  2
TC  1
TG  1
TT  4
```