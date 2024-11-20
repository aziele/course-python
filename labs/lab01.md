## Zad. 1
Które z poniższych nazw zmiennych są prawidłowe? Spróbuj odpowiedzieć bez testowania kodu.

```
name
n
user name
NAME
_name
user-name
1st_name
user_name
name_1
n@me
userName
```

## Zad. 2
Utwórz program `hello.py`, który zapyta użytkownika o imię i ulubiony kolor, a następnie wyświetli stosowny komunikat.

```
$ python3 hello.py
What is your name? John
What is your favorite color? blue
```

Wynik:

```
John likes blue.
```

## Zad. 3
Utwórz program `volume.py`, który obliczy objętość kuli po podaniu przez użytkownika promienia okręgu.

```
$ python3 app.py
Enter a radius: 6
```

Wynik:

```
The volume of the sphere is: 904.3
```


## Zad. 4
Utwórz program `mm2km.py`, który pobierze od użytkownika liczbę milimetrów i zamieni ją na liczbę kilometrów, metrów, centymetrów i pozostałych milimetrów.

```
$ python3 mm2km.py
Enter number of millimeters [mm]: 1530293
```

Wynik:

```
1 km 530 m 29 cm 3 mm
```


## Zad. 5
Kartkę papieru można złożyć na pół maksymalnie 7 razy. Utwórz program `paper_fold.py`, który obliczy grubość kartki papieru gdyby można ją było złożyć na pół wiele razy. Standardowa kartka papieru ma grubość 0,05 mm. Po pierwszym złożeniu otrzymujemy kartkę o grubości 0,1 mm. Po drugim złożeniu kartka ma 0,2 mm grubości. Po trzecim złożeniu kartka ma grubość 0,4 mm. Przy siódmym złożeniu kartka ma 6,4 mm.

```
$ python3 paper_fold.py
Enter a number of paper folds: 7
```

Wynik:

```
Width: 6.4 mm
```

Ile kilometrów ma grubość kartki złożonej na pół 45 razy?


## Zad. 6
Napisz program `age_in_seconds.py`, który poprosi użytkownika o jego wiek w latach (liczba całkowita), a następnie obliczy i wyświetli wiek w sekundach (przyjmując, że rok ma 365 dni).


```
$ python3 age_in_seconds.py
Enter your age in years: 20
```

Wynik:

```
Your age in seconds is approximately: 630720000 seconds.
```