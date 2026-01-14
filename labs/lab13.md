## Zad. 1
W klasie `SeqRecord` zmodyfikuj metodę `fasta`, aby sekwencja zawinięta była domyślnie do 60 znaków.

```python
class SeqRecord:
    
    def __init__(self, id, sequence, description=None):       
        self.id = id
        self.seq = sequence
        self.description = description

    def counts(self):
        d = {}
        for char in self.seq:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d

    def fasta(self):
        desc = self. description if self.description else ''
        return f'>{self.id} {desc}\n{self.seq}'

    def __str__(self):
        return self.id

    def __len__(self):
        return len(self.seq)

    def __contains__(self, char):
        return char in self.seq

    def __iter__(self):
        return iter(self.seq)

    def __getitem__(self, key):
        return self.seq[key]
        

class DNARecord(SeqRecord):

    def transcribe(self):
        return self.seq.replace('T', 'U')

    def complement(self):
        d = {'A': 'T', 'C': 'G', 'G': 'C', 'T':'A'}
        return "".join([d.get(nt, 'N') for nt in self.seq])

    def reverse_complement(self):
        return self.complement()[::-1]
```

## Zad. 3
W klasie `DNARecord` dodaj metodę `mutate`, która w sekwencij DNA wprowadzi jedną losową substytucję nukleotydu na losowej pozycji.


## Zad. 4
Utwórz klasę `ProteinRecord`, która będzie podrzędna do klasy `SeqRecord`. W klasie `ProteinRecord` utwórz metodę `aromaticity`, która oblicza *aromatyczność białka* (procentowy udziału aminokwasów aromatycznych: `Y` + `W` + `F`).