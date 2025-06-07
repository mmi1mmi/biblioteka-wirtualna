import datetime

class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania, liczba_stron, dostepne):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron
        self.dostepne = dostepne

    def __str__(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania}, Liczba stron: {self.liczba_stron}, Dostępne: {self.dostepne}"

class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wypozyczone_ksiazki = []

    def __str__(self):
        ksiazki_str = ", ".join([ksiazka.tytul for ksiazka in self.wypozyczone_ksiazki])
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Wypożyczone książki: ({len(self.wypozyczone_ksiazki)}) {ksiazki_str}"

# Dalsza część kodu została skrócona dla przejrzystości (w rzeczywistości będzie pełna).