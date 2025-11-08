## Zad. 1
Napisz program `molmass.py`, który w oparciu o poniższy słownik masy pojedynczych aminokwasów obliczy masę molową (kDa) sekwencji białkowej wprowadzonej przez użytkownika.

> Masa molowa sekwencji białkowej to suma mas wszystkich aminokwasów znajdujących się w sekwencji. Masy pojedynczych aminokwasów znajdują się w poniższym słowniku `weights`. Jeżeli sekwencja użytkownika zawiera znak, którego nie ma w słowniku `weights` to przyjmij, że masa molowa tego znaku to 0. Na przykład, masa molowa sekwencji `MKSX` jest równa 149.2113 + 146.1876 + 105.0926 + 0 = 400.4915

```python
weights = { 
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

```
Enter DNA sequence: MKSX
```

Wynik:

```
400.49 kDa
```


## Zad. 2
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


## Zad. 3
Utwórz program `protein_histogram.py`, który zliczy wystąpienia każdego aminokwasu w podanej przez użytkownika sekwencji białkowej.

```
Enter protein sequence: MKTWYRSSVVVV
```

Wynik:

```python
{'M': 1, 'K': 1, 'T': 1, 'W': 1, 'Y': 1, 'R': 1, 'S': 2, 'V': 4}
```


## Zad. 4
Utwórz program `words.py`, który wyświetli liczbę wystąpień każdego wyrazu w poniższym tekście.

```python
text = 'The first rule of Fight Club is you do not talk about Fight Club'
```

Wynik:

```
# Kolejność słów nie ma znaczenia.
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


## Zad. 5
Utwórz program `dinucleotide.py`, który zliczy wszystkie dwunukleotydowe podsekwencje występujące w poniższej sekwencji DNA.

```python
dna = 'AGCCCGATGCTTAAACGTAGATTTTCC'
```

Wynik:

```
# Kolejność alfabetyczna.
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


## Zad. 6
Zmodyfikuj program `dinucleotide.py`, aby oprócz zliczeń każdego dwunukleotydowego słowa podawał również procentowy udział słowa w całej sekwencji.

Wynik:

```
AA  2  7.7
AC  1  3.8
AG  2  7.7
AT  2  7.7
CC  3  11.5
CG  2  7.7
CT  1  3.8
GA  2  7.7
GC  2  7.7
GT  1  3.8
TA  2  7.7
TC  1  3.8
TG  1  3.8
TT  4  15.4
```

## Zad. 7 (dla chętnych)
Utwórz program `aa2codons.py`, którzy na podstawie słownika `codons` z zad. 2 wyświetli kodony dla każdego aminokwasu.

Wynik:

```
*   TAA TAG TGA
A   GCA GCC GCG GCT
C   TGC TGT
D   GAC GAT
E   GAA GAG
F   TTC TTT
G   GGA GGC GGG GGT
H   CAC CAT
I   ATA ATC ATT
K   AAA AAG
L   CTA CTC CTG CTT TTA TTG
M   ATG
N   AAC AAT
P   CCA CCC CCG CCT
Q   CAA CAG
R   AGA AGG CGA CGC CGG CGT
S   AGC AGT TCA TCC TCG TCT
T   ACA ACC ACG ACT
V   GTA GTC GTG GTT
W   TGG
Y   TAC TAT
```