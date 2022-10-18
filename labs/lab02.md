## Zad. 1
Poniższy program jest poprawny pod względem składni języka Python, ale zawiera *błąd logiczny*. Napraw poniższy kod, aby działał prawidłowo.

```python
age = int(input('How old are you? '))

if age > 13:
    print("You can get ice cream")
elif age > 18:
    print("You are an adult")
elif age > 5:
    print("You can get candy")
else:
    print("You need a nap") 
```

## Zad. 2
Utwórz program `dna2rna.py`, który przyjmie od użytkownika sekwencję DNA i zamieni ją na sekwencję RNA.

```
$ python3 dna2rna.py
DNA sequence: ATGCTGC
```

Wynik:

```
RNA sequence: AUGCUGC
```

## Zad. 3
Czy Twój program `dna2rna.py` zwróci prawidłową sekwencję RNA jeżeli użytkownik wprowadzi sekwencję `AtGcTgC`? Zmodyfikuj kod swojego programu, aby działał prawidłowow niezależnie od wielkości liter. 

```
$ python3 dna2rna.py
DNA sequence: AtGcTgC
```

Wynik:

```
RNA sequence: AUGCUGC
```

## Zad. 4
Wysoka zawartość nukleotydów `G` i `C` w sekwencji DNA wskazuje, że dany region DNA może być genem. Utwórz program `gc_content.py`, który przyjmie od użytkownika sekwencję DNA i obliczy w niej procentową zawartości sumy nukleotydów `G` i `C`.

```
$ python3 gc_content.py 
DNA/RNA sequence: ATGCTGC
```

Wynik:

```
GC content: 57.1%
```

## Zad. 5
Poniższa sekwencja stanowi fragment ludzkiego genu BRCA2, który związany jest z rakiem piersi.

```python
dna = "GGGCTTGTGGCGCGAGCTTCTGAAACTAGGCGGCAGAGGCGGAGCCGCTGTGGCACTGCTGCGCCTCTGCTGCGCCTCGGGTGTCTTTT"
```

Utwórz program `brca2.py`, umieść w nim powyższą zmienną i dodaj instrukcje, które odpowiedzą na poniższe pytania:

1. Z ilu nukleotydów składa się sekwencja?
2. Jaki procent sekwencji stanowi nukleotyd `G`?
2. Jaki fragment sekwencji znajduje się w pozycji od 56 do 68 nukleotydu (licząc od 1)?
3. W jakiej pozycji znajduje się sekwencja `GCGGCAGAG` (licząc od 0)?


## Zad. 6
Mówi się, że każdy rok psa równy jest 7 latom człowieka. Na przykład, jak pies ma 10 lat to odpowiada on 70 letniemu człowiekowi. Ponieważ pies zaczyna być dorosły w wieku 2 lat, niektórzy sugerują, aby liczyć dwa pierwsze lata psa po 10,5 lat człowieka, a każdy kolejny rok psa liczyć jako 4 lata. Na przykład, jak pies ma 2 lata to odpowiada on 21-letniemu człowiekowi, jak pies ma 3 lata to odpowiada 25-letniemu człowiekowi. Napisz program `dog.py`, który przeliczy wiek psa na odpowiadający mu wiek człowieka.


## Zad. 7
Utwórz program `bmi.py`, który prosi użytkownika o podanie wzrostu (cm) i wagi (kg), i obliczy wskaźnik masy ciała (BMI, *Body Mass Index*). Następnie w oparciu o obliczoną wartość BMI program wyświetli stosowny komunikat.

```python
#              waga (kg)
# BMI = -----------------------
#       wzrost (m) * wzrost (m)
# 
# Na przykład, BMI osoby ważącej 70 kg i mierzącej 175
# wynosi 70/(1.75 * 1.75) = 22.86

# BMI > 30           obesity
# 25 <= BMI <= 30    overweight
# 19 <= BMI <= 25    normal weight
# BMI < 19           underweight
```

## Zad. 8
Napisz program `numbers.py`, który odczytuje liczby tak długo, aż użytkownik wprowadzi "quit". Po wpisaniu "quit" program powinien wyświetlić sumę liczb, ile wprowadzono liczb oraz średnią z tych liczb.

```
$ python numbers.py
Type quit to exit the program.
Enter a number: 3
Enter a number: 4
Enter a number: 5
Enter a number: 5
Enter a number: quit
```

Wynik:

```
Sum: 17
Number count: 4
Mean: 4.2
```