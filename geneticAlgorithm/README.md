# Algorytm genetyczny Hollanda
## Opis zadania
W ramach ćwiczenia wykonałem implementację algorytmu genetycznego
Hollanda, a następnie zastosowałem go do znalezienia minimum funkcji
podanej w treści polecenia. Całkowite argumenty funkcji zostały
przekonwertowane do kodu Graya w celu zapewnienia małych różnic między
sąsiednimi liczbami (kod Graya gwarantuje różnicę jednego bitu pomiędzy
kolejnymi wyrazami). Pewnej modyfikacji wymagała również funkcja celu
wykorzystywana w reprodukcji ruletkowej. Przyjąłem dla niej wartość
równą -f(x) + max(f(x)) + 1, która oznacza, że funkcja rośnie w kierunku
mniejszych wartości funkcji f(x), a także posiada jedynie wartości
dodatnie, dzięki czemu nigdy nie otrzymamy ujemnego prawdopodobieństwa.

## Testowanie
Eksperymentalne strojenie parametrów
====================================

W celu optymalnego działania algorytmu konieczne jest odnalezienie
odpowiednich parametrów, jak: liczba iteracji, rozmiar populacji,
prawdopodobieństwo mutacji i krzyżowania. Dla każdego z zestawów
parametrów przeprowadzono 25 przejść algorytmu, co pozwala zmniejszyć
losowość wyników.

Startowe parametry
------------------

Liczba iteracji: 500

Rozmiar populacji: 100

Prawdopodobieństwo mutacji: 0.05

Prawdopodobieństwo krzyżowania: 0.5

  Średnia wartość wyniku          13,45
  ------------------------------- ------------
  Odchylenie standardowe wyniku   **10,746**
  Średni czas trwania             **0,376s**

Większy rozmiar populacji
-------------------------

W celu znalezienia lepszych wyników podjąłem próbę zwiększenia rozmiar
populacji.

Liczba iteracji: 500

Rozmiar populacji: 1000

Prawdopodobieństwo mutacji: 0.05

Prawdopodobieństwo krzyżowania: 0.5

  Średnia wartość wyniku          1,072
  ------------------------------- -------------
  Odchylenie standardowe wyniku   **0,227**
  Średni czas trwania             **15,811s**

Zwiększenie rozmiaru populacji poprawiło efekty działania algorytmu,
kosztem znacznego wydłużenia czasu działania.

Mniejsze prawdopodobieństwo krzyżowania
---------------------------------------

Kolejny eksperyment związany jest z prawdopodobieństwem krzyżowania.
Spróbowałem zmniejszenia go, aby potencjalnie ograniczyć odchylenie
standardowe wyniku.

Liczba iteracji: 500

Rozmiar populacji: 1000

Prawdopodobieństwo mutacji: 0.05

Prawdopodobieństwo krzyżowania: 0.1

  Średnia wartość wyniku          2,028
  ------------------------------- -------------
  Odchylenie standardowe wyniku   **1,367**
  Średni czas trwania             **15,441s**

Na podstawie wyników eksperymentu widać, że zmniejszenie
prawdopodobieństwa krzyżowania pogarsza uzyskiwane wyniki, ponieważ
populacja nie zmienia się dostatecznie szybko.

Zwiększenie prawdopodobieństwa mutacji
--------------------------------------

Podjąłem także próbę zwiększenia prawdopodobieństwa mutacji, aby
sprawdzić wpływ większej losowości na wynik działania algorytmu.

Liczba iteracji: 500

Rozmiar populacji: 1000

Prawdopodobieństwo mutacji: 0.5

Prawdopodobieństwo krzyżowania: 0.5

  Średnia wartość wyniku          1,392
  ------------------------------- -------------
  Odchylenie standardowe wyniku   **1,08**
  Średni czas trwania             **16,862s**

Zwiększenie prawdopodobieństwa mutacji nie wpłynęło pozytywnie na
działanie algorytmu, ponieważ potencjalnie doprowadziło do utraty już
odnalezionych minimum.

## Wnioski
Zaimplementowany przeze mnie algorytm genetyczny Hollanda w zadowalający
sposób radzi sobie
z zadaniem znalezienia minimum funkcji. Największą jego wadą okazuje się
czas działania konieczny do uzyskania akceptowalnych wyników oraz jego
losowość. W celu poprawnego działania warto zastosować bardzo duży
rozmiar populacji, a także dużą liczbę iteracji, aby zapewnić dobrą
różnorodność w poszukiwaniach. Na podstawie eksperymentów mogę także
potwierdzić, że głównym mechanizmem ewolucji w tym algorytmie powinno
być krzyżowanie (zmniejszenie jego prawdopodobieństwa pogarsza wyniki),
natomiast mutacja musi być stosowana ostrożnie (zbyt duże jej
prawdopodobieństwo pogarsza wyniki i znacznie zwiększa ich losowość).
