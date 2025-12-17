## Zad. 1
Napisz generator `even_numbers(n)`, który zwraca liczby parzyste od `0` do `n` (włącznie).

Przykład:

```python
for num in even_numbers(10):
    print(num)
```

Output:

```python
0
2
4
6
8
10
```


## Zad. 2
Napisz generator `sliding_window(seq, k)`, który przesuwa okno o długości `k` po sekwencji.

Przykład:

```python
for w in sliding_window("ATGCTGA", 3):
    print(w)
```

Output:

```python
ATG
TGC
GCT
CTG
TGA
```


## Zad. 3
Przy rzucie dwoma kostkami do gry (sześć oczek), prawdopodobieństwo uzyskania sumy oczek równej 7 wynosi około 17%.

Napisz program `dice.py`, który wykona 1,000,000 symulowanych rzutów dwoma kostkami i zliczy liczbę wystąpień każdej możliwej sumy oczek (od 2 do 12) oraz obliczy procentowy udział każdej sumy względem wszystkich rzutów.

Przykład:

```
Simulating 1,000,000 rolls of 2 dice...

2 - 27590 rolls - 2.8%
...
7 - 166327 rolls - 16.6%
...
```


## Zad. 4
Rozszerz program z poprzedniego zadania tak, aby wyniki były uszeregowane malejąco według liczby wystąpień.


## Zad. 5* (dla chętnych)
Rozszerz program z poprzedniego zadania tak, aby zamiast dwóch kostek obsługiwał dowolną liczbę sześciościennych kostek, podaną przez użytkownika.


```
Enter how many six-sided dice you want to roll: 3

Simulating 1,000,000 rolls of 3 dice...
...

```


## Zad. 6* (dla chętnych)
W pliku [consensus.fasta](./data/consensus.fasta) jest 10 sekwencji DNA o równej długości.

Napisz program `consensus.py`, który na podstawie tych sekwencji wyznaczy sekwencję konsensusową, czyli taki ciąg znaków, w którym dla każdej pozycji wybierany jest nukleotyd najczęściej występujący w tej pozycji wśród 10 sekwencji. W przypadku remisu wybierz nukleotyd alfabetycznie wcześniejszy.


Wynik:

```
ATGGAACT
```


## Zad. 7* (dla chętnych)
Napisz generator `read_fasta(path)`, który czyta plik FASTA i zwraca krotki:

```
(identyfikator, sekwencja)
```

Generator powinien działać liniowo — to znaczy nie wczytujemy całego pliku do pamięci, tylko zwraca kolejne rekordy po napotkaniu następnego nagłówka (`>`), albo na końcu pliku. Przykładowy plik z pięcioma sekwencjami znajduje się w pliku [proteins.fasta](../data/proteins.fasta).

Przykład użycia:

```python
for seq_id, seq in read_fasta('proteins.fasta'):
    print(seq_id, len(seq))
```

Wynik:

```
sp|O00767|SCD_HUMAN 359
sequence2 1071
sp|O75845|SC5D_HUMAN 299
sequence 205
sp|P38606|VATA_HUMAN 617
```