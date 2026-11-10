## Zad. 1. Kontrola poprawności sekwencji DNA

Dla sekwencji:

```python
sequence = "atgCGTNNaagtXc"
```

* Zamień wszystkie litery na wielkie.
* Za pomocą pętli wypisz pozycje i symbole wszystkich znaków innych niż A, C, G, T. Numeruj pozycje od 1.
* Utwórz nowy string zawierający wyłącznie poprawne nukleotydy.
* Oblicz procent nukleotydów G i C w oczyszczonej sekwencji.


## Zad. 2. Wszystkie wystąpienia motywu

Dane są sekwencja DNA i motyw:

```python
sequence = "ATATATGATATATGCTAGTCGATGATCGATATATATGCGTAGATGCTAGCTGATCGATATATAT"
motif = "ATAT"
```

Znajdź wszystkie pozycje początkowe motywu, również gdy wystąpienia na siebie zachodzą. Zapisz je w liście, numerując od 1.

Wynik:

```python
[1, 3, 8, 10, 29, 31, 33, 57, 59, 61]
```


## Zad. 3. Najdłuższy homopolimer

Homopolimer to fragment sekwencji złożony z powtórzeń tego samego nukleotydu, np. `AAAA`.

Dla sekwencji:

```python
sequence = "ATGGGGCTAAAAAATCC"
```

Znajdź najdłuższy homopolimer. Wypisz jego nukleotyd, długość i pozycję początkową, numerowaną od 1. Jeżeli kilka fragmentów ma taką samą maksymalną długość, wybierz pierwszy.

Spróbuj przejść przez sekwencję tylko raz.


## Zad. 4 Statystyki zestawu białek

Dane są sekwencje białek:

```python
proteins = [
    "MALWMRLLPLL",
    "MKWVTFISLLFLFSSAYS",
    "MAG",
    "MALWMRLLPLL",
    "GAVLIP"
]
```

1. Utwórz listę długości białek.
2. Oblicz liczbę białek, ich łączną i średnią długość.
3. Znajdź najkrótszą i najdłuższą sekwencję.
4. Utwórz listę białek o długości co najmniej 10 aminokwasów.
5. Utwórz listę unikalnych sekwencji, zachowując kolejność ich pierwszego wystąpienia. Do usuwania duplikatów użyj listy i operatora `in`.


## Zad. 5. Wczytywanie sekwencji z pliku

W dowolnym edytorze tekstu utwórz plik `proteins.txt` i umieść w nim sekwencje z poprzedniego zadania w poniższej formie. Zachowaj puste linie oraz spacje przed niektórymi sekwencjami.

```
malwmrllPLL  
MKWVTFISLLFLFSSAYS   

MaG 

  mAlwMRLLpLL
 gavlip

```

Wczytaj sekwencje do listy. Usuń białe znaki z początku i końca każdej linii, pomiń puste linie i zamień litery na wielkie. Następnie wykonaj analizy z poprzedniego zadania.

Na początek możesz wykorzystać:

```python
proteins = []

with open("proteins.txt") as file:
    for line in file:
        # Uzupełnij kod.
        print(line)
```


## Zad. 6. Wyrazy angielskie

W pliku [english_words.txt](./data/english_words.txt) znajduje się około 370 tys. wyrazów w języku angielskim, po jednym w każdym wierszu. Wykorzystaj kod z poprzedniego zadania, aby wczytać wyrazy do listy. Następnie odpowiedz na poniższe pytania:

1. Ile dokładnie wyrazów znajduje się w pliku?
2. Ile wyrazów ma co najmniej 20 liter?
3. Które wyrazy są palindromami i mają co najmniej 5 liter? Zapisz je na liście. Palindrom to wyraz czytany tak samo od lewej i od prawej, np. level.
4. Jaki jest najdłuższy wyraz i ile ma liter?
5. Litera `e` jest najczęściej występującą literą w języku angielskim. Oblicz jej procentowy udział w łącznej liczbie liter we wszystkich wyrazach z pliku.

