## Zad. 1
Utwórz program `volume.py`, który obliczy objętość kuli po podaniu przez użytkownika promienia okręgu.

```
$ python volume.py
Enter a radius: 9
```

Wynik:

```
The volume of the sphere is: 3052.08
```


## Zad. 2
Napisz program `age_in_seconds.py`, który poprosi użytkownika o jego wiek w latach (liczba całkowita), a następnie obliczy i wyświetli wiek w sekundach (przyjmując, że rok ma 365 dni).


```
$ python age_in_seconds.py
Enter your age in years: 20
```

Wynik:

```
Your age is: 630720000 seconds.
```


## Zad. 3
Utwórz program `mm2km.py`, który pobierze od użytkownika liczbę milimetrów i zamieni ją na liczbę kilometrów, metrów, centymetrów i pozostałych milimetrów.

```
$ python mm2km.py
Enter number of millimeters [mm]: 1530293
```

Wynik:

```
1 km 530 m 29 cm 3 mm
```


## Zad. 4
Kartkę papieru można złożyć na pół maksymalnie 7 razy. Utwórz program `paper_fold.py`, który obliczy grubość kartki papieru gdyby można ją było złożyć na pół wiele razy. Standardowa kartka papieru ma grubość 0,05 mm. Po pierwszym złożeniu otrzymujemy kartkę o grubości 0,1 mm. Po drugim złożeniu kartka ma 0,2 mm grubości. Po trzecim złożeniu kartka ma grubość 0,4 mm. Przy siódmym złożeniu kartka ma 6,4 mm.

```
$ python paper_fold.py
Enter a number of paper folds: 7
```

Wynik:

```
Width: 6.4 mm
```

Ile kilometrów ma grubość kartki złożonej na pół 45 razy? Oblicz to uruchamiając programy `paper_fold.py` i `mm2km.py`.


## Zad. 5
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


## Zad. 6
Mówi się, że każdy rok psa jest równy siedmiu latom człowieka. Na przykład, jak pies ma 10 lat to odpowiada on 70 letniemu człowiekowi. Ponieważ pies zaczyna być dorosły w wieku 2 lat, niektórzy sugerują, aby liczyć dwa pierwsze lata psa po 10,5 lat człowieka, a każdy kolejny rok psa liczyć jako 4 lata. Na przykład, jak pies ma 2 lata to odpowiada on 21-letniemu człowiekowi, jak pies ma 3 lata to odpowiada 25-letniemu człowiekowi. Napisz program `dog.py`, który przeliczy wiek psa (liczbę całkowitą) na odpowiadający mu wiek człowieka.


```
$ python dog.py 
Enter dog age: 4
```

Wynik:

```
Human years: 29.0
```


## Zad. 7 (dla chętnych)
Utwórz program `bmi.py`, który prosi użytkownika o podanie wzrostu (cm) i wagi (kg), i obliczy wskaźnik masy ciała (BMI, *Body Mass Index*). Następnie w oparciu o obliczoną wartość BMI program wyświetli stosowny komunikat.

```python
#              waga (kg)
# BMI = -----------------------
#       wzrost (m) * wzrost (m)
# 
# Na przykład, BMI osoby ważącej 70 kg i mierzącej 175
# wynosi 70 / (1.75 * 1.75) = 22.86

# BMI >30       obesity
# BMI (25, 30]  overweight
# BMI [19, 25]  normal weight
# BMI <19       underweight
```