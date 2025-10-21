## Zad. 1
Utwórz program `dna2rna.py`, który przyjmie od użytkownika sekwencję DNA i zamieni ją na sekwencję RNA.

```
$ python dna2rna.py
DNA sequence: ATGCTGCCC
```

Wynik:

```
RNA sequence: AUGCUGCCC
```


## Zad. 2
Czy Twój program `dna2rna.py` zwróci prawidłową sekwencję RNA jeżeli użytkownik wprowadzi sekwencję `AtGcTgC`? Zmodyfikuj kod swojego programu, aby działał prawidłowo niezależnie od wielkości liter. 

```
$ python dna2rna.py
DNA sequence: AtGcTgC
```

Wynik:

```
RNA sequence: AUGCUGC
```


## Zad. 3
Wysoka zawartość nukleotydów `G` i `C` w sekwencji DNA wskazuje, że dany region DNA może być genem. Utwórz program `gc_content.py`, który przyjmie od użytkownika sekwencję DNA i obliczy w niej procentową zawartości sumy nukleotydów `G` i `C`.

```
$ python gc_content.py 
DNA sequence: ATGCTGC
```

Wynik:

```
GC content: 57.1%
```


## Zad. 4
Zmodyfikuj kod programu `gc_content.py` tak, aby na podstawie obliczonej zawartości GC klasyfikował sekwencję DNA:
* jeśli GC > 60% → `GC-rich region`
* jeśli 40% ≤ GC ≤ 60% → `Moderate GC region`
* jeśli GC < 40% → `AT-rich region`

Dodatkowo:
* jeśli sekwencja jest pusta → wypisz `Error: empty sequence` i zakończ program bez obliczania wartości GC.


```
$ python gc_content.py 
DNA sequence: ATGCTGC
```

Wynik:

```
GC content: 57.1%
Moderate GC region
```


## Zad. 5
Utwórz program `tail.py`, który przyjmie od użytkownika sekwencję DNA oraz długość fragmentu (*n*). Jeśli sekwencja ma co najmniej podaną długość (*n*), wyświetli ostatnie *n* nukleotydów. W przeciwnym razie wyświetli komunikat `Sequence too short`.

```
$ python tail.py
DNA sequence: AGCTGATGGATGGATGA
Tail length: 5
```

Wynik:

```
GATGA
```


## Zad. 6
Poniższa sekwencja stanowi fragment ludzkiego genu BRCA2, który związany jest z rakiem piersi.

```python
dna = "GGGCTTGTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCTGTGGCACTGCTGCGCCTCTGCTGCGCCTCGGGTGTCTTTT"
```

Utwórz program `brca2.py`, umieść w nim powyższą zmienną i dodaj instrukcje, które odpowiedzą na poniższe pytania:

1. Z ilu nukleotydów składa się sekwencja?
2. Jaki procent sekwencji stanowi nukleotyd `G`?
3. Jaki fragment sekwencji znajduje się w pozycji od 56 do 68 nukleotydu (licząc od 1)?
4. W jakiej pozycji znajduje się sekwencja `GCGGCAGAG` (licząc od 0)?


## Zad. 7
Utwórz program `coding_seq1.py`, który sprawdzi, czy wprowadzona przez użytkownika sekwencja DNA może kodować białko.

Sekwencja kodująca powinna:
* zaczynać się od kodonu start (`ATG`)
* kończyć się jednym z kodonów stop (`TAG` / `TGA` / `TAA`)
* mieć długość podzielną przez 3

```
$ python coding_seq.py 
DNA sequence: ATGGCACATTA
```

Wynik:

```
Sequence is invalid.
```


## Zad. 8
Utwórz program `coding_seq2.py`, który w przypadku nieprawidłowej sekwencji kodującej poinformuje użytkownika dokładnie, co jest niepoprawne.

```
$ python coding_seq.py 
DNA sequence: ATCGCACATTA
```

Wynik:

```
Start codon is missing.
Stop codon is missing.
Sequence length is not a multiple of 3.
```