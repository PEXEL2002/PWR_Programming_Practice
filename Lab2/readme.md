# 🧪 Laboratorium 2 – Programowanie w parach

---

## 🎯 Cel laboratorium

Celem laboratorium było zapoznanie się z techniką **Programowania w parach**.  
Podczas zajęć:
- Każdy z uczestników pracował w parze nad zadaniem przedstawionym przez prowadzącego.
- Przeprowadziliśmy cztery iteracje pracy w parach, każda trwająca 10 minut, z regularną zamianą ról.
- Na końcu zajęć omówiliśmy zalety i wady tej techniki oraz dokonaliśmy retrospektywy.

---

## 🧠 Teoria

**Programowanie w parach** to technika wytwarzania oprogramowania, w której dwóch programistów pracuje nad jednym projektem na jednym komputerze. W ramach tej techniki, jedna osoba pełni rolę **przodownika (driver)**, a druga **nawigatora (navigator)**.

Zasady pracy w parach:
1. **Przodownik** koduje rozwiązanie, skupiając się na szczegółach implementacji.
2. **Nawigator** pomaga, kontroluje postępy, sugeruje rozwiązania, ale nie pisze kodu.

Ważne zasady:
- Regularna zamiana ról co 25 minut, z przerwą na 5 minut.
- Działanie w zgodzie z techniką **gumowej kaczuszki**: omawianie kodu na głos, aby lepiej zrozumieć problem.

Zalety:
- Szybsze wykrywanie błędów
- Wymiana doświadczeń i wiedzy
- Zwiększona kreatywność

Wady:
- Większe koszty związane z czasem i potrzebą doboru odpowiednich par

---

## 📚 Zadanie – Gra w życie

Zadanie polegało na zaimplementowaniu **Gry w życie** Johna Conwaya, automatu komórkowego, który ewoluuje na podstawie prostych zasad.  

### 🔹 Etap 1
* Napisz program w Pythonie, który będzie symulować grę na siatce o zadanych wymiarach.
* Zainicjalizuj stan komórek, mogą być one losowe lub określone z góry.

### 🔹 Etap 2
* Zaimplementuj reguły zmiany stanów komórek:
  * Martwa komórka, która ma 3 żywych sąsiadów, staje się żywa.
  * Żywa komórka, która ma 2 lub 3 żywych sąsiadów, pozostaje żywa.
  * Żywa komórka, która ma mniej niż 2 lub więcej niż 3 żywych sąsiadów, umiera.

### 🔹 Etap 3
* Dodaj symulację czasową – każda zmiana stanu komórek następuje co sekundę.

### 🔹 Etap 4
* Przetestuj program w różnych warunkach i scenariuszach, aby upewnić się, że zasady zostały poprawnie zaimplementowane.

---

## 🧑‍🤝‍🧑 Współpraca w parze

Każda para miała za zadanie współpracować zgodnie z zasadami **Pair programming**:
- **Przodownik**: pisze kod, koncentruje się na implementacji.
- **Nawigator**: kontroluje kod, proponuje poprawki, upewnia się, że zadanie jest wykonywane zgodnie z wymaganiami.

---