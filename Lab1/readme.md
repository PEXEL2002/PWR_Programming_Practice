# Laboratorium 1 – Test Driven Development

## 📌 Temat:
Ćwiczenia praktyczne z wykorzystania podejścia **Test Driven Development (TDD)**.

## 🎯 Cel zajęć:

- Poznanie procesu pisania testów przed implementacją kodu.
- Praca z narzędziami do testowania (np. `unittest`, `pytest`).
- Utrwalenie podejścia Red → Green → Refactor.

## 🧪 Zadania:

1. Stwórz funkcję sprawdzającą czy liczba jest pierwsza.
2. Napisz testy jednostkowe dla funkcji.
3. Refaktoryzuj kod i przetestuj ponownie.

## 🛠️ Użyte narzędzia:
- Python
- Pytest

## 📝 Notatki:

- Pierwsze testy nie przechodziły — brak obsługi przypadku `n <= 1`.
- Poprawa logiki funkcji pomogła w 100% przejściu testów.

## 📁 Pliki:

- `is_prime.py`
- `test_is_prime.py`
Jeśli chcesz, mogę:

przygotować wszystkie README.md dla folderów Lab1 do Lab6

zapisać je w .zip do pobrania

dorzucić plik .gitignore dla repozytorium Python

Chcesz to?







Powiedziałeś(-aś):
Praktyki_programowania_LAB1.pdf
PDF
oto następny plik drogi studencie
ChatGPT powiedział:
Świetnie! Na podstawie pliku Praktyki_programowania_LAB1.pdf, oto przykładowy README.md dla folderu Lab1_TDD, który możesz umieścić w swoim repozytorium:

📄 Lab1_TDD/README.md
markdown
Kopiuj
Edytuj
# 🧪 Laboratorium 1 – Test Driven Development (TDD)

---

## 🎯 Cel laboratorium

Celem zajęć było praktyczne poznanie podejścia **Test Driven Development (TDD)**.  
Podczas warsztatów:
- Najpierw każdy student pisał testy jednostkowe dla zadania.
- Następnie zmienialiśmy stanowiska, aby zaimplementować kod spełniający cudze testy.
- Na koniec refaktoryzowaliśmy kod i przesyłaliśmy efekty pracy na GitHub.

---

## 🧠 Teoria

**TDD** to podejście zakładające:
1. Pisanie testów jednostkowych przed kodem.
2. Implementację funkcjonalności tak, by testy przechodziły.
3. Refaktoryzację kodu bez psucia testów.

Proces ten powtarzamy cyklicznie:  
**Red → Green → Refactor**

Zalety:
- Wczesne wykrywanie błędów
- Czystszy, bardziej przemyślany kod
- Testy jako forma dokumentacji

Wady:
- Większy nakład czasu na pisanie i utrzymanie testów

---

## 🛠️ Narzędzia

- **Python**
- Biblioteka `unittest` (wbudowana)
- Środowisko: np. PyCharm

## 📚 Zadania – Kata String Calculator

Zadanie polegało na rozwoju funkcji `Add(numbers)` krok po kroku:

### 🔹 Etap 1
* Napisz testy jednostkowe dla funkcji `Add(numbers)`
  * Obsługa: `""`, `"1"`, `"1,2"`
  * Wynik: suma lub `0` dla pustego stringa

### 🔹 Etap 2
* Napisz funkcję `Add(numbers)` spełniającą testy z Etapu 1

### 🔹 Etap 3
* Rozszerz testy o obsługę wielu liczb

### 🔹 Etap 4
* Rozszerz implementację funkcji

### 🔹 Etap 5
* Dodaj obsługę znaków nowej linii (`\\n`) jako separatorów:
  * `"1\\n2,3"` → `6`
  * `"1,\\n"` → **błąd**

### 🔹 Etap 6
* Finalna wersja funkcji `Add` spełniająca wszystkie wymagania