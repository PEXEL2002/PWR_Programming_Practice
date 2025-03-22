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