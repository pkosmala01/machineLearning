# Uczenie się ze wzmocnieniem
## Opis zadania
W ramach ćwiczenia zająłem się implementacją algorytmu Q-learning, a
następnie wykorzystaniu go do stworzenia agenta grającego w grę Frozen
Lake dostępną w pakiecie gym. Użyta została przeze mnie strategia
decaying E-greedy, w której prawdopodobieństwo eksploracji zmniejsza się
co 100 epizodów (jest mnożone przez liczbę mniejszą od 1), otrzymana
liczba stanowi później szansę, z którą wykonana zostanie losowa akcja
zamiast akcji wybranej na podstawie QTable. Wartość learning rate
została ustawiona na 0.1, a discount na 0.99.

## Testowanie
W toku testowania poprawności implementacji zauważyłem, że największy
wpływ na efektywność działania ma szybkość spadku prawdopodobieństwa
eksploracji. Poniżej przedstawiam skutki wprowadzania zmian w tym
parametrze przy pozostawieniu innych w domyślnych wartościach.

DecayRate = 0.9
---------------

Średnia nagroda po 0 epizodach: 0.0

Średnia nagroda po 1000 epizodach: 0.045

Średnia nagroda po 2000 epizodach: 0.254

Średnia nagroda po 3000 epizodach: 0.476

Średnia nagroda po 4000 epizodach: 0.625

Średnia nagroda po 5000 epizodach: 0.686

W powyższym przypadku testowym udało się osiągnąć nagrodę 0.686, co
oznacza, że agent dociera do celu w około 68% przypadków.

DecayRate = 0.8
---------------

Średnia nagroda po 0 epizodach: 0.0

Średnia nagroda po 1000 epizodach: 0.056

Średnia nagroda po 2000 epizodach: 0.527

Średnia nagroda po 3000 epizodach: 0.724

Średnia nagroda po 4000 epizodach: 0.738

Średnia nagroda po 5000 epizodach: 0.731

Po zwiększeniu szybkości spadku parametru działanie algorytmu poprawia
się. Wynika to z dużej eksploracji w początkowych epizodach i szybkiego
zwiększenia eksploatacji pod koniec przypadku testowego.

DecayRate = 0.75
----------------

Średnia nagroda po 0 epizodach: 0.0

Średnia nagroda po 1000 epizodach: 0.104

Średnia nagroda po 2000 epizodach: 0.487

Średnia nagroda po 3000 epizodach: 0.635

Średnia nagroda po 4000 epizodach: 0.635

Średnia nagroda po 5000 epizodach: 0.62

Zbyt szybkie zmniejszanie prawdopodobieństwa eksploracji nie pozwala
algorytmowi na wystarczające rozbudowanie qTable zanim zostanie ona
podstawą działania, zatem pogarsza jego efektywność.

## Wnioski
W trakcie wykonywania ćwiczenia zauważyłem, że najważniejszą kwestią, od
której zależy skuteczność algorytmu, jest balans między eksploracją a
eksploatacją. Strategia decaying E-greedy wydaje się nie być
perfekcyjna, natomiast osiąga wyniki na poziomie 75% skuteczności w
stosunkowo krótkim czasie. W ciągu testów przy wykorzystaniu żadnej
kombinacji parametrów nie udało mi się przekroczyć tego wyniku, lecz
wydaje się on wystarczający.
