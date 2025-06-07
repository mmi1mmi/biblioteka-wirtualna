# Wirtualna Biblioteka

Prosty program w Pythonie do zarządzania wirtualną biblioteką.  Umożliwia dodawanie, edytowanie, usuwanie i wyszukiwanie książek, a także zarządzanie studentami i wypożyczeniami.

## Funkcjonalności

*   **Zarządzanie książkami:**
    *   Dodawanie nowych książek (tytuł, autor, rok wydania, liczba stron, liczba dostępnych egzemplarzy).
    *   Edycja istniejących książek (zmiana tytułu, autora, roku wydania, liczby stron, liczby dostępnych egzemplarzy).
    *   Usuwanie książek (pojedyncze egzemplarze lub całe pozycje).
    *   Wyszukiwanie książek (po tytule, autorze i/lub roku wydania).
*   **Zarządzanie studentami:**
    *   Dodawanie nowych studentów (imię, nazwisko).
    *   Lista studentów (z informacją o wypożyczonych książkach).  Limit 15 studentów.
*   **Wypożyczenia i zwroty:**
    *   Wypożyczanie książek studentom (jeśli książka jest dostępna i student nie przekroczył limitu 5 wypożyczonych książek).
    *   Oddawanie książek przez studentów.
*   **Raporty i przypomnienia:**
    *   Wyświetlanie pełnego raportu biblioteki (lista książek i studentów).
    *   Przypomnienie o zwrocie książek (dla każdego studenta z wypożyczonymi książkami).

## Uruchomienie

1.  **Wymagania:** Program wymaga Pythona 3.
2.  **Uruchomienie:** Zapisz kod programu (np. jako `biblioteka.py`) i uruchom go w terminalu/konsoli:

    ```bash
    python biblioteka.py
    ```

3. **Interakcja:** Program wyświetli menu z dostępnymi opcjami.  Wprowadź numer opcji i naciśnij Enter, aby ją wybrać.  Program będzie prosił o podanie dodatkowych danych w zależności od wybranej opcji.

## Struktura kodu

Program składa się z trzech klas:

*   **`Ksiazka`:** Reprezentuje pojedynczą książkę.  Zawiera informacje takie jak tytuł, autor, rok wydania, liczba stron i liczba dostępnych egzemplarzy.
*   **`Student`:** Reprezentuje studenta.  Zawiera imię, nazwisko i listę wypożyczonych książek.
*   **`Biblioteka`:**  Główna klasa zarządzająca biblioteką.  Zawiera listy książek i studentów oraz metody do obsługi wszystkich funkcjonalności (dodawanie, usuwanie, edycja, wyszukiwanie, wypożyczanie, oddawanie, raporty).

Główne funkcje klasy `Biblioteka`:

* `__init__()`: Inicjalizuje bibliotekę, dodając początkowy zestaw książek i studentów.
* `dodaj_ksiazke(ksiazka)`: Dodaje nową książkę do biblioteki.
* `usun_ksiazke(tytul)`: Usuwa książkę z biblioteki (lub zmniejsza liczbę egzemplarzy).
* `edytuj_ksiazke(tytul, nowe_dane)`: Edytuje dane książki.
* `wyszukaj_ksiazke(tytul=None, autor=None, rok_wydania=None)`: Wyszukuje książki według podanych kryteriów.
* `dodaj_studenta(student)`: Dodaje nowego studenta do biblioteki (do limitu 15 studentów).
* `wypozycz_ksiazke(tytul, student)`: Wypożycza książkę studentowi.
* `oddaj_ksiazke(tytul, student)`: Obsługuje zwrot książki.
* `przypomnij_o_zwrocie()`: Wyświetla przypomnienia dla studentów z wypożyczonymi książkami.
* `raport()`: Wyświetla raport stanu biblioteki.
* `dodaj_poczatkowe_ksiazki()`: Dodaje początkowy zestaw 27 książek.
* `dodaj_poczatkowych_studentow()`: Dodaje 15 studentów.

## Przykładowe użycie

Po uruchomieniu programu możesz:

1.  **Dodać książkę:** Wybierz opcję 1 i podaj dane książki.
2.  **Wyszukać książkę:** Wybierz opcję 4 i podaj kryteria wyszukiwania (np. tytuł).
3.  **Wypożyczyć książkę:** Wybierz opcję 6, podaj tytuł książki oraz imię i nazwisko studenta.
4.  **Wyświetlić raport:** Wybierz opcję 9, aby zobaczyć listę wszystkich książek i studentów.
5.  **Wyjść z programu:** Wybierz opcję 0.

## Uwagi

*   Program przechowuje dane tylko w pamięci RAM. Po wyłączeniu programu dane zostaną utracone.  Aby zapewnić trwałość danych, należałoby dodać zapisywanie i odczytywanie z pliku (np. CSV, JSON) lub użyć bazy danych.
*   Kod jest napisany prostym językiem, program przeznaczony do nauki Pythona.
