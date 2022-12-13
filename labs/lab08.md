## Zad. 1
Utwórz program `random_dna.py`, który będzie generował losową sekwencję DNA o podanej przez użytkownika długości.

```python
import sys
print(sys.argv)
```

```bash
python random_dna.py 50
```

Wynik:

```
ATTGCTGATGATGAGTAGATCGTATAGGATTAGTAGAGATATGATAGAGC
```

## Zad. 2
Utwórz program `simulation.py`, który 1000 razy wykona program `random_dna.py` dla sekwencji długości 20 nukleotydów.

```python
import os
os.system('python random_dna.py 20')

# lub

import subprocess
process = subprocess.run(
    'python random_dna.py 20', 
    shell=True, text=True, capture_output=True
)
print(process.stdout)
#print(process.stderr)
```


## Zad. 3
W skompresowanym pliku [human_proteins.zip](../data/human_proteins.zip) znajduje się katalog zawierający 250 sekwencji białkowych człowieka (każda sekwencja w osobnym pliku). Rozwiń poniższy kod, aby otwierał każdy z 250 plików i obliczał średnią długość tych sekwencji.

```python
from pathlib import Path

directory = Path('human_proteins')
for file in directory.iterdir():
    print(file)
    print(file.name)
    print(file.stem)
```

Wynik:

```
Mean sequence length: 628.1
```

## Zad. 4
Poniższy kod pobiera sekwencję białka `Q93062` z bazy UniProt.

```python
import urllib.request

f = urllib.request.urlopen('http://www.uniprot.org/uniprot/Q93062.fasta')
sequence = f.read().decode('utf-8')
f.close()
print(sequence)
```

Zmodyfikuj kod, aby pobierał sekwencje białkowe dla podanych poniżej identyfikatorów i zapisywał wszystkie sekwencje do pliku `uniprot.txt`. Zadbaj o to, aby czas pomiędzy wykonywaniem instrukcji `urllib.request.urlopen` wynosił przynajmniej 1 sekundę.

```python
ids = ['P68431', 'Q6ZQ08', 'O94687', 'Q9FNR1', 'P31350', 'Q91Z31', 'P11157']
```


## Zad. 5
Oblicz dystans Hamming pomiędzy każdą parą sekwencji w słowniku `SEQUENCES`. Dodaj również kod, który wskażę parę sekwencji o najmniejszym dystansie.

```python
import itertools

def hamming_distance(seq1, seq2):
    return sum([1 for n1, n2 in zip(seq1, seq2) if n1 != n2])

SEQUENCES = {
    'seq1': 'ATCGTCGTAGAT',
    'seq2': 'GCTGCTGATAGT',
    'seq3': 'TATGATGAGTAG',
    'seq4': 'ATGATGATTTGG',
    'seq5': 'CCTGCTAATAGA',
    'seq6': 'TTAGATGATGCT',
    'seq7': 'AGCTGATGCGTG'
}

for s1, s2 in itertools.combinations(SEQUENCES, r=2):
    print(s1, s2)
```


## Zad. 6* (dla chętnych)
Zapisz poniższy kod do pliku `random_dna_v2.py`.

```python
import argparse

__version__ = 0.5

p = argparse.ArgumentParser(
    description='Generate a random DNA sequence',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument('dna_length', type=int, help='Length of random DNA sequence')
p.add_argument('-a', '--a', dest='adenine', type=float,
               default=0.25, help='Adenine probability')
p.add_argument('-c', '--c', dest='cytosine', type=float,
               default=0.25, help='Cytosine probability')
p.add_argument('-g', '--g', dest='guanine', type=float,
               default=0.25, help='Guanine probability')
p.add_argument('-t', '--t', dest='thymine', type=float,
               default=0.25, help='Thymine probability')
p.add_argument('-v', '--v', '--version', action='version',
               version=f'v.{__version__}',
               help="Show tool's version number and exit")
args = p.parse_args()


print(args.dna_length)
print(args.adenine)
print(args.cytosine)
print(args.guanine)
print(args.thymine)
```

Uruchom program `random_dna_v2.py` poniższymi poleceniami. Następnie dokończ program, aby generował losową sekwencję DNA o podanej przez użytkownika długości. Program powinien mieć możliwość podania prawdopodobieństwa wystąpienia każdego z nukleotdów (domyślnie nukleotdy występują z jednakowym prawdopodobieństwem, czyli suma ich prawdopodobieństw musi być równa 1).

```bash
python random_dna_v2.py
python random_dna_v2.py -h
python random_dna_v2.py --help
python random_dna_v2.py 100
python random_dna_v2.py 100 -a 0.2 -c 0.3
python random_dna_v2.py 100 -v
```

## Zad. 7 (dla chętnych)
Metody *alignment-free* są nowoczesnymi metodami porównywania sekwencji. Większość z nich zakłada, że spokrewnione sekwencje (*homologiczne*) składają się z wielu podobnych krótszych podsekwencji (*k*-merów).

#### Przykład

Poniżej przedstawiono sposób porównania dwóch sekwencji: `x = ATGTGTG` i `y = CATGTG` przy użyciu *k*-mer = `3`.

1. Wyszukanie wszystkich *k*-merów w sekwencji `x` i `y`.
```
x = ATGTGTG           y = CATGTG
    ATG                   CAT          
     TGT                   ATG
      GTG                   TGT
       TGT                   GTG
        GTG
```

2. Zliczenia *k*-merów w sekwencji `x` i `y`.

```
       x      y
ATG    1      1
CAT    0      1
GTG    2      1           # GTG występuje 2 razy w x i 1 raz w y
TGT    2      1 
```

3. Częstości *k*-merów w sekwencjach `x` i `y`.

```
       x      y
ATG    0.2    0.25
CAT    0      0.25
GTG    0.4    0.25        # x: 2/5 = 0.4; y: 1/4 = 0.25
TGT    0.4    0.25 
```

4. Obliczenie [dystansu euklidesowego](https://en.wikipedia.org/wiki/Euclidean_distance) między wektorami częstości `x` i `y`.

```
d(x, y) = [(0.2 - 0.25)^2 + (0 - 0.25)^2 + (0.4 - 0.25)^2 + (0.4 - 0.25)^2]^0.5 
        = [0.0025 + 0.0625 + 0.0225 + 0.0225]^0.5
        = 0.11^0.5 = 0.332
```

Wartość `0.332` odpowiada dystansowi jaki dzieli dwie sekwencje `x` i `y`.


### Cel zadania
Celem zadania jest napisanie programu, który dla zadanego pliku sekwencji w formacie FASTA obliczy dystanse euklidesowe pomiędzy każdą parą sekwencji w zależności od podanej przez użytkownika długości słowa (*k*-mer) i sprecyzowania, czy wektorem mają być zliczenia czy częstości. Wynikiem powinnien być plik zawierający pary dystansów.

Na przykład dla 4 sekwencji białkowych:

```
>seq1
EVVIRSANFTDNAKIIIVQLNASVEINCTRPNNYTRKGIR
IGPGRAVYAAEEIIGDIRRAHCNISREKWNNTLKQVVTKL
REQFVNKTIIFTHPSGGDPEIVMHSVNCGGEFFY
>seq2
VIRSANFTDNAKIIIVQLNASVEINCTRPNNNTRKGIRIG
PGRAVYAAEEIIGDIRRAHCNISREKWNNTLKQVVTKLRE
QFVNKTIIFNHSSGGDPEIVMHSFNCGGEFFY
>seq3
EVVIRSANFTDNAKIIIVQLNASVEINCTRPNNNTRKGIH
IGPGRAVYATDRIIGDIRQAHCNISREKWNNTLKQVVTKL
REQFVNKTIIFTHPSGGDPEIVMHSVNCGGEFFY
>seq4
EVVIRSANFTDNAKIIIVQLNASVEINCTRPNNNTRRGIH
IGPGRAFYATDRIVGDIRQAYCNISREKWNNTLKQVVAKL
REQFVNKTIIFNHSSGGDPEIVMHSVNCGGEFFYCNT
```

Pary dystansów dla zliczeń 2-merów:

```
seq1 seq2 4.4721
seq1 seq3 4.2426
seq1 seq4 7.1414
seq2 seq3 5.4772
seq2 seq4 6.5574
seq3 seq4 5.7446
```

Pary dystanstów dla częstości 2-merów:

```
seq1 seq2 0.0400
seq1 seq3 0.0375
seq1 seq4 0.0623
seq2 seq3 0.0490
seq2 seq4 0.0577
seq3 seq4 0.0500
```