## Zad. 1
Utwórz moduł `myfuncs.py` z dwiema funkcjami `complement(seq)` i `reverse_complement(seq)`. Następnie utwórz program `app.py`, który w pętli `for` wykorzysta funkcję `reverse_complement` na poniższych sekwencjach: 

```python
sequences = ['ATGCTAGT', 'GATGATAG', 'AGTCGA', 'AGATGCTAG']
```


## Zad. 2
W module `myfuncs.py` utwórz funkcję:


```python
def read_fasta_to_dict(fasta_file):
    """
    Wczytuje plik FASTA do słownika {id: sekwencja}.
    """
```

Przetestuj funkcję na 15 sekwencjach genomowych bakterii *Mycoplasma hominis*, które są w pliku [Mycoplasma_hominis.fasta](../data/Mycoplasma_hominis.fasta). Zwróć uwagę, że identyfikator sekwencji to część nagłówka po `>` do pierwszej spacji, a sekwencje mogą być rozbite na wiele linii. Funkcja powinna zwrócić słownik, np. `{ 'contig011': 'ACAGCCAGCG...', ... }`.


## Zad. 3
Plik [Mycoplasma_hominis.csv](../data/Mycoplasma_hominis.csv) zawiera lokalizacje genów i innych fragmentów w odniesieniu do sekwencji genomowych [Mycoplasma_hominis.fasta](../data/Mycoplasma_hominis.fasta).

```
contig,feature,start,end,strand,gene_id,biotype
contig011,gene,1,105,-,JX73_01575,rRNA
contig011,transcript,1,105,-,JX73_01575,rRNA
contig011,exon,1,105,-,JX73_01575,rRNA
contig011,gene,5831,5905,+,JX73_01605,tRNA
contig011,transcript,5831,5905,+,JX73_01605,tRNA
contig011,exon,5831,5905,+,JX73_01605,tRNA
...
```

Na przykład gen `JX73_01575` znajduje się w sekwencji `contig011` na nici `-` w lokalizacji `1` - `105` i koduje `rRNA`, a gen `JX73_01605` w sekwencji `contig011` na nici `+` w pozycji `5831` - `5905`.

Utwórz program `mycoplasma.py`, który na podstawie informacji z pliku *csv* oraz funkcji z modułu `myfuncs.py` wydobędzie sekwencje **genów** i zapisze je do pliku `genes.fasta`. Geny znajdujące się na nici `-` powinny zostać zapisane w kierunku 5'-3', czyli jako odwrotnie komplementarne.

Output:

```
>contig011|gene|JX73_01575|1:105|-
CTGGATACGAATACCATTAACGTCAATTTATTTTTTTATTTATAATCAACCAATTCAAATTTTTTTATAAGAGTTTGATCCTGGCTCAGGATGAACGCTGGCTGT
>contig011|gene|JX73_01605|5831:5905|+
GGTCGCATAGCTCAGTGGAAGAGCACGAGCCTCCTAAGCCCGGGGTCGCAGGTTCAACTCCTGTTGCGATCGCCA
>...
```


## Zad. 4
Zmodyfikuj program `mycoplasma.py`, aby sekwencja w pliku wynikowym była zawinięta do 60 znaków. W module `myfuncs.py` utwórz funkcję `wrap(seq, width)`, która przyjmuje string i liczbę znaków do zawinięcia.

Output:

```
>contig011|gene|JX73_01575|1:105|-
CTGGATACGAATACCATTAACGTCAATTTATTTTTTTATTTATAATCAACCAATTCAAAT
TTTTTTATAAGAGTTTGATCCTGGCTCAGGATGAACGCTGGCTGT
>contig011|gene|JX73_01605|5831:5905|+
GGTCGCATAGCTCAGTGGAAGAGCACGAGCCTCCTAAGCCCGGGGTCGCAGGTTCAACTC
CTGTTGCGATCGCCA
>...
```