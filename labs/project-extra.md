# Projekt bioinformatyczny - wyszukiwanie powtórzeń terminalnych

## 1. Zakres materiału projektu

Projekt wykorzystuje zagadnienia omawiane w całym cyklu zajęć (zajęcia 1–15).

## 2. Cel projektu

Napisz program w Pythonie, który wyszukuje powtórzenia terminalne w sekwencjach DNA zapisanych w plikach FASTA i tworzy tabelę wyników w formacie TSV. Program będzie użyteczny w rzeczywistych analizach bioinformatycznych i metagenomowych.

## 3. Co to są powtórzenia terminalne i dlaczego ich szukamy

Metagenomika pozwala badać materiał genetyczny organizmów i wirusów obecnych w próbce środowiskowej, np. w wodzie, glebie lub jelicie człowieka. Krótkie odczyty uzyskane podczas sekwencjonowania składa się w dłuższe sekwencje nazywane **kontigami** (*contigs*). Kontig może odpowiadać całemu genomowi albo tylko jego fragmentowi. W przypadku wirusów często trudno ustalić, czy kontig odpowiada całemu genomowi, czy tylko jego fragmentowi.

Jedną ze wskazówek są **powtórzenia terminalne** (*terminal repeats*, TR), czyli odpowiadające sobie fragmenty na samym początku i samym końcu sekwencji. Mogą odzwierciedlać budowę genomu liniowego lub sposób złożenia genomu kolistego, którego końcowy fragment nakłada się na początek. Ich obecność sugeruje, że udało się odtworzyć kompletny genom lub segment genomu, ale nie stanowi samodzielnego dowodu kompletności ani wirusowego pochodzenia kontigu. Powtórzenia mogą też wynikać z błędów składania lub małej złożoności sekwencji. Dlatego obok samego wykrywania TR będziemy również obliczać ich statystyki.

### 3.1. Dwa typy powtórzeń terminalnych

#### DTR — direct terminal repeat

Na obu końcach występuje **identyczna sekwencja w tej samej orientacji**.

Przykład kontigu: `ACGATTTTGATACGA`.

| Początek | Fragment środkowy | Koniec |
| --- | --- | --- |
| `ACGA` | `TTTTGAT` | `ACGA` |

Jest to DTR o sekwencji `ACGA` i długości 4 nt. Skrót **nt** oznacza nukleotydy.

#### ITR — inverted terminal repeat

Fragment na końcu jest **odwrotnie komplementarny** do fragmentu z początku.

Przykład kontigu: `ACGATTTTGATTCGT`.

| Początek | Fragment środkowy | Koniec |
| --- | --- | --- |
| `ACGA` | `TTTTGAT` | `TCGT` |

Odwrotnym komplementem `ACGA` jest `TCGT`. Jest to więc ITR długości 4 nt. W wynikach jako `tr_seq` zapisujemy zawsze fragment z **początku kontigu**, tutaj `ACGA`.

Przykłady są celowo krótkie. W rzeczywistych analizach wymagamy dłuższych powtórzeń, np. co najmniej 20–30 nukleotydów, żeby ograniczyć przypadkowe dopasowania.

Dwie kopie terminalne używane do wykrywania DTR lub ITR nie mogą się nakładać. Długość powtórzenia nie może więc przekraczać połowy długości kontigu.

## 4. Oczekiwane działanie programu

Napisz program (o dowolnej nazwie, np. `trfinder.py`), który:

1. Przyjmuje ścieżkę do pojedynczego pliku FASTA lub katalogu zawierającego pliki FASTA.
2. Odczytuje kolejne kontigi z plików nieskompresowanych lub skompresowanych gzipem (`.gz`).
3. Wyszukuje najdłuższe powtórzenia terminalne typu DTR i ITR, zgodnie z podanymi progami długości.
4. Jeśli kontig zawiera oba typy powtórzeń, wybiera dłuższe. Przy jednakowej długości wybiera DTR.
5. Oblicza statystyki powtórzenia i całego kontigu.
6. Zapisuje wyniki ze wszystkich analizowanych plików do jednej tabeli TSV.

Wynik powinien zawierać jeden wiersz na każdy kontig z wykrytym powtórzeniem spełniającym wymagania. Kontigi bez takich powtórzeń pomijamy.

### 4.1. Uruchamianie programu

Program powinien być uruchamiany z wiersza poleceń, bez konieczności edytowania kodu.

Przykład analizy katalogu:

```bash
python trfinder.py --in directory --min_dtr 30 --min_itr 30 --out results.tsv
```

Przykład analizy pojedynczego pliku:

```bash
python trfinder.py --in sample.fna.gz --min_dtr 30 --min_itr 30 --out results.tsv
```

### 4.2. Argumenty

| Argument | Znaczenie | Wartość domyślna |
| --- | --- | --- |
| `--in` | Ścieżka do pliku FASTA lub katalogu | Argument wymagany |
| `--out` | Ścieżka do wynikowego pliku TSV | Argument wymagany |
| `--min_dtr` | Minimalna długość DTR | `20` |
| `--min_itr` | Minimalna długość ITR | `20` |
| `--min_contig_len` | Minimalna długość analizowanego kontigu | `1500` |
| `-h`, `--help` | Wyświetlenie opisu programu i argumentów | — |


Do sprawdzania krótkich przykładów z instrukcji ustaw odpowiednio mniejsze progi:

```bash
python trfinder.py --in example.fasta --min_dtr 4 --min_itr 4 --min_contig_len 1 --out example.tsv
```


## 5. Dane wejściowe i reguły wyszukiwania

### 5.1. Obsługiwane pliki

Przykładowe dane wejściowe znajdziesz w archiwum [project-data.zip](./data/project-data.zip). Po jego rozpakowaniu możesz sprawdzić działanie programu zarówno dla pojedynczego pliku FASTA, jak i całego katalogu z plikami.

Program powinien sam rozpoznawać, czy ścieżka podana przez `--in` wskazuje plik, czy katalog.

Obsługiwane rozszerzenia FASTA:

- `.fna`
- `.fasta`
- `.fas`
- `.fa`

Każdy z tych plików może być również skompresowany gzipem, np. `sample.fasta.gz`. Wielkość liter w rozszerzeniu nie powinna mieć znaczenia.

Jeśli wejściem jest katalog:

- analizuj tylko pliki bezpośrednio w tym katalogu, bez przeszukiwania podkatalogów;
- pomijaj pliki o innych rozszerzeniach;
- przetwarzaj pliki w kolejności alfabetycznej ich nazw;
- zapisuj wszystkie wyniki do jednego pliku TSV.


### 5.2. Odczyt rekordów sekwencji FASTA

Jeden plik może zawierać wiele rekordów sekwencji w [formacie FASTA](https://pl.wikipedia.org/wiki/FASTA_format). Identyfikator kontigu to pierwszy wyraz nagłówka FASTA po znaku `>`. Pozostała część nagłówka jest opisem.

Przykład:

```text
>contig_17 sample from lake
```

Oczekiwany podział:

- `contig_id`: `contig_17`
- `contig_desc`: `sample from lake`

Jeśli opis nie występuje, zapisz puste pole.

### 5.3. Symbole niejednoznaczne IUPAC

Sekwencje mogą zawierać symbole inne niż `ACGT`. Na przykład `R` oznacza `A` lub `G`, a `N` dowolny z czterech nukleotydów.

Program powinien obsługiwać poniższy alfabet DNA:

| Symbol | Możliwe nukleotydy | Symbol komplementarny |
| --- | --- | --- |
| A | A | T |
| C | C | G |
| G | G | C |
| T | T | A |
| R | A, G | Y |
| Y | C, T | R |
| S | C, G | S |
| W | A, T | W |
| K | G, T | M |
| M | A, C | K |
| B | C, G, T | V |
| D | A, G, T | H |
| H | A, C, T | D |
| V | A, C, G | B |
| N | A, C, G, T | N |

W tym projekcie stosujemy **dokładne porównywanie symboli**, a nie porównywanie zbiorów możliwych nukleotydów:

- `R` pasuje do `R`, ale nie do `A` ani `G`;
- `N` pasuje tylko do `N`;
- przy ITR najpierw wyznaczamy odwrotny komplement zgodnie z tabelą, a następnie porównujemy symbole.

Przykładowo odwrotnym komplementem `ARYN` jest `NRYT`.

Jest to przyjęta reguła obliczeniowa. Zgodność symboli niejednoznacznych nie gwarantuje zgodności rzeczywistych nukleotydów. Nie odrzucamy jednak takich powtórzeń — obliczamy ich statystyki, aby umożliwić późniejszą ocenę.

## 6. Liczenie wystąpień powtórzenia

Pole `tr_count` opisuje liczbę wystąpień wybranego motywu w całym kontigu, uwzględniając kopie terminalne i wewnętrzne.

- Dla DTR licz wystąpienia `tr_seq`.
- Dla ITR licz wystąpienia `tr_seq` oraz jego odwrotnego komplementu.
- Podczas liczenia wystąpień motywu uwzględniaj również wystąpienia nakładające się na siebie.
- Każdą pozycję początkową licz tylko raz, również wtedy, gdy motyw jest własnym odwrotnym komplementem.

## 7. Format wyników

TSV to plik tekstowy, w którym kolumny oddzielone są znakami tabulacji. Pierwszy wiersz powinien zawierać nagłówek z poniższymi nazwami kolumn, w podanej kolejności.

| Kolumna | Znaczenie |
| --- | --- |
| `file_name` | Nazwa pliku źródłowego z rozszerzeniami, bez ścieżki, np. `sample.fna.gz` |
| `contig_id` | Oryginalny identyfikator kontigu |
| `contig_len` | Długość całego kontigu, łącznie z obiema kopiami terminalnymi |
| `tr_type` | Typ wybranego powtórzenia: `DTR` lub `ITR` |
| `tr_seq` | Sekwencja wybranego powtórzenia z początku kontigu |
| `tr_len` | Długość `tr_seq` |
| `tr_count` | Liczba wystąpień motywu według opisanych wcześniej zasad |
| `tr_nt_acgt_count` | Łączna liczba symboli `A`, `C`, `G` i `T` w `tr_seq` |
| `tr_nt_n_count` | Liczba symboli `N` w `tr_seq` |
| `tr_nt_n_freq` | Procent symboli `N` w `tr_seq` |
| `tr_nt_max_freq` | Największy procentowy udział pojedynczego nukleotydu wśród symboli `ACGT` w `tr_seq` |
| `contig_nt_acgt_count` | Łączna liczba symboli `A`, `C`, `G` i `T` w całym kontigu |
| `contig_nt_n_count` | Liczba symboli `N` w całym kontigu |
| `contig_nt_n_freq` | Procent symboli `N` w całym kontigu |
| `contig_desc` | Opis z nagłówka FASTA; puste pole, jeśli go nie było |

### Zasady obliczania statystyk

Pola zawierające `nt_n` dotyczą wyłącznie symbolu `N`, a nie wszystkich symboli niejednoznacznych. Na przykład `R` zwiększa długość sekwencji, ale nie zwiększa ani liczby `ACGT`, ani liczby `N`.

Częstotliwości obliczamy następująco:

- `tr_nt_n_freq = 100 × tr_nt_n_count / tr_len`
- `contig_nt_n_freq = 100 × contig_nt_n_count / contig_len`
- `tr_nt_max_freq = 100 × max(liczba A, liczba C, liczba G, liczba T) / tr_nt_acgt_count`

Wszystkie częstotliwości zapisuj:

- w skali 0–100;
- z dwoma miejscami po przecinku;
- z kropką dziesiętną;
- bez znaku `%`.

Przykład dla `tr_seq = AANR`:

| Pole | Wartość |
| --- | --- |
| `tr_len` | `4` |
| `tr_nt_acgt_count` | `2` |
| `tr_nt_n_count` | `1` |
| `tr_nt_n_freq` | `25.00` |
| `tr_nt_max_freq` | `100.00` |

Statystyki TR dotyczą jednej kopii zapisanej w `tr_seq`, a statystyki kontigu — całej sekwencji wejściowej.

Tabulatory w opisie kontigu zastąp spacjami, aby nie tworzyły dodatkowych kolumn.

Jeśli nie znaleziono żadnego powtórzenia spełniającego wymagania, plik wynikowy powinien zawierać sam nagłówek.

## 8. Proponowane etapy realizacji

W zależności od swojego doświadczenia w programowaniu możesz podzielić pracę na mniejsze etapy lub od razu rozwijać pełną wersję programu. Nie narzucam konkretnego podziału ani kolejności prac — wybierz sposób, który będzie dla Ciebie najwygodniejszy. Poniższa propozycja może pomóc w zaplanowaniu projektu.

### Etap 1 — pojedyncza sekwencja

Zacznij od sekwencji zapisanej jako string, bez odczytu plików.

- Przygotuj wyznaczanie odwrotnego komplementu.
- Dodaj wyszukiwanie DTR i ITR.
- Zastosuj regułę wyboru jednego wyniku.
- Sprawdź działanie na krótkich przykładach.

Na początek możesz ograniczyć się do `ACGT`, a pozostałe symbole IUPAC obsłużyć później.

### Etap 2 — statystyki

- Dodaj liczenie wystąpień motywu w całym kontigu.
- Oblicz wymagane liczby nukleotydów i częstotliwości.
- Sprawdź wyniki ręcznie na prostych przykładach.

### Etap 3 — jeden plik FASTA i wynik TSV

- Odczytuj kolejne rekordy z nieskompresowanego pliku FASTA.
- Zachowuj identyfikatory i opisy.
- Analizuj kontigi i zapisuj wyniki do TSV.

Na tym etapie ścieżki i progi mogą być jeszcze zapisane bezpośrednio w kodzie.

### Etap 4 — katalog i kompresja

- Dodaj rozpoznawanie pliku i katalogu.
- Wyszukuj pliki o obsługiwanych rozszerzeniach.
- Obsłuż odczyt `.gz`.
- Zapisuj wyniki ze wszystkich plików do jednej tabeli.

### Etap 5 — wiersz poleceń

- Dodaj argumenty określające wejście, wyjście i progi.
- Przygotuj pomoc `--help`.
- Sprawdzaj poprawność argumentów.
- Dodaj czytelne komunikaty błędów.

### Etap 6 — dopracowanie

- Uzupełnij wszystkie wymagania, w tym pełną obsługę IUPAC.
- Sprawdź przypadki brzegowe.
- Uporządkuj kod i dokumentację.
- Przygotuj instrukcję uruchamiania.
- Sprawdź program na udostępnionych danych.

Testy możesz przygotowywać już podczas wcześniejszych etapów, aby po każdej zmianie łatwo sprawdzać, czy dotychczasowe funkcje nadal działają poprawnie.

## 9. Wskazówki dotyczące kodu, bibliotek i testowania

### 9.1. Organizacja i czytelność kodu

Możesz przygotować jeden plik `trfinder.py` albo podzielić program na kilka modułów. Wybór należy do Ciebie.

Zależy mi przede wszystkim na tym, aby kod był staranny, bardzo czytelny i dobrze udokumentowany.

- Wydziel funkcje wykonujące konkretne zadania.
- Stosuj informatywne i konsekwentne nazwy zmiennych oraz funkcji.
- Dokumentuj przeznaczenie funkcji, ich argumenty i zwracane wartości.
- Komentarzami wyjaśniaj mniej oczywiste decyzje i fragmenty algorytmu.
- Unikaj powielania tego samego kodu.
- Zadbaj o prawidłowe zamykanie plików.
- Przetwarzaj kolejne pliki i rekordy zamiast wczytywać cały katalog do pamięci.

Nie chodzi o jak najszybsze napisanie programu, ale o przygotowanie rozwiązania, które można zrozumieć, sprawdzić i dalej rozwijać.

### 9.2. Przydatne moduły i biblioteki

| Moduł lub biblioteka | Możliwe zastosowanie |
| --- | --- |
| `pathlib` | Obsługa ścieżek, rozpoznawanie pliku i katalogu, iterowanie po plikach |
| `gzip` | Odczyt plików `.gz` |
| `argparse` | Obsługa argumentów wiersza poleceń i generowanie pomocy |
| Biopython lub `fastapy` | Parsowanie plików FASTA |
| `pytest` lub `unittest` | Automatyczne testowanie |

`argparse` wystarczy do przygotowania wymaganego interfejsu i jest częścią standardowej biblioteki Pythona.

Parser FASTA możesz napisać samodzielnie albo skorzystać z gotowego rozwiązania, np. Biopythona lub mojego `fastapy` [GitHub](https://github.com/aziele/fastapy). Jeśli korzystasz z bibliotek zewnętrznych, opisz sposób ich instalacji.

### 9.3. Obsługa błędów

Program powinien wyświetlać zrozumiałe komunikaty, gdy:

- ścieżka wejściowa nie istnieje;
- wskazany plik ma nieobsługiwane rozszerzenie;
- katalog nie zawiera obsługiwanych plików;
- argumenty mają nieprawidłowe wartości;
- pliku nie można odczytać lub wyniku nie można zapisać.

Takie błędy powinny powodować zakończenie programu z niezerowym kodem zakończenia.

Zabezpiecz również program przed nadpisaniem pliku wejściowego plikiem wynikowym.

### 9.4. Sprawdzanie poprawności

Nawet jeśli nie przygotowujesz automatycznych testów, sprawdź program na małych przykładach o znanych wynikach.

Uwzględnij między innymi:

- kontig z DTR;
- kontig z ITR;
- kontig bez powtórzeń terminalnych;
- kontig z oboma typami powtórzeń;
- remis długości DTR i ITR;
- powtórzenie dokładnie na progu minimalnej długości;
- kontig krótszy niż wymagany próg;
- powtórzenia zawierające symbole IUPAC;
- powtórzenie bez symboli `ACGT`, np. złożone wyłącznie z `N`;
- nakładające się wystąpienia motywu;
- motyw będący własnym odwrotnym komplementem;
- sekwencję FASTA zapisaną w kilku wierszach;
- nagłówek bez opisu;
- ten sam plik w wersji nieskompresowanej i `.gz`;
- katalog z różnymi rozszerzeniami plików;
- analizę, w której nie znaleziono żadnego TR.

Przykłady do sprawdzenia wyboru powtórzenia:

| Sekwencja | Minimalne długości DTR i ITR | Oczekiwany wynik |
| --- | --- | --- |
| `ACGATTTTGATACGA` | `4` | DTR: `ACGA`, długość 4 |
| `ACGATTTTGATTCGT` | `4` | ITR: `ACGA`, długość 4 |
| `AAAACCCC` | `4` | Brak TR |
| `GCAGCAGGGGCTGCCTGC` | `2` | DTR długości 2 i ITR długości 4; wybieramy ITR: `GCAG` |
| `ACGTGGACGT` | `4` | Oba typy długości 4; wybieramy DTR: `ACGT` |

Opcjonalnie napisz automatyczne testy przy użyciu `pytest` albo `unittest`. Najpierw zadbaj o poprawność i czytelność rozwiązania. Pomiar czasu i optymalizację możesz potraktować jako dalsze rozszerzenie projektu.