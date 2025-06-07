# Wirtualna Biblioteka

Prosty program w Pythonie do zarządzania wirtualną biblioteką. Umożliwia dodawanie, edytowanie, usuwanie i wyszukiwanie książek, a także zarządzanie studentami i wypożyczeniami.

## Funkcjonalności

### Zarządzanie książkami:
- Dodawanie nowych książek (tytuł, autor, rok wydania, liczba stron, liczba dostępnych egzemplarzy).
- Edycja istniejących książek.
- Usuwanie książek.
- Wyszukiwanie książek.

### Zarządzanie studentami:
- Dodawanie studentów (limit 15 osób).
- Informacje o wypożyczonych książkach przez studenta.

### Wypożyczenia i zwroty:
- Wypożyczenia (limit 5 książek na studenta).
- Oddawanie książek.

### Raporty i przypomnienia:
- Pełny raport stanu biblioteki.
- Przypomnienie o zwrocie książek.

## Uruchomienie

1. Wymagany Python 3.
2. Zapisz plik `biblioteka.py` i uruchom go w terminalu:

```bash
python biblioteka.py
```

## Uwagi

Program przechowuje dane tylko w pamięci operacyjnej (RAM). Po zamknięciu programu dane są tracone.
