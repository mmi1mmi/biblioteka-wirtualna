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

class Biblioteka:
    def __init__(self):
        self.ksiazki = []
        self.studenci = []
        self.dodaj_poczatkowe_ksiazki()  # Dodajemy początkowe książki
        self.dodaj_poczatkowych_studentow() #Dodajemy studentow

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def usun_ksiazke(self, tytul):
        ksiazki_do_usuniecia = self.wyszukaj_ksiazke(tytul=tytul)
        if not ksiazki_do_usuniecia:
            print(f"Nie znaleziono książki o tytule '{tytul}'.")
            return

        if len(ksiazki_do_usuniecia) > 1:
            print("Znaleziono kilka książek o tym tytule.  Proszę podać autora, aby doprecyzować.")
            autor = input("Autor: ")
            ksiazki_do_usuniecia = self.wyszukaj_ksiazke(tytul=tytul, autor=autor)
            if not ksiazki_do_usuniecia:
                print("Nie znaleziono książki o podanym tytule i autorze.")
                return
            if len(ksiazki_do_usuniecia) > 1:
                print("Nadal znaleziono wiele książek. Nie można usunąć - zbyt niejednoznaczne kryteria.")
                return

        ksiazka = ksiazki_do_usuniecia[0]  # Bierzemy pierwszą (i jedyną, po ew. doprecyzowaniu)

        if ksiazka.dostepne > 1:
            ksiazka.dostepne -= 1
            print(f"Zmniejszono liczbę dostępnych egzemplarzy książki '{tytul}' do {ksiazka.dostepne}.")
        else:
            self.ksiazki.remove(ksiazka)
            print(f"Książka '{tytul}' została usunięta z biblioteki (ostatni egzemplarz).")

    def edytuj_ksiazke(self, tytul, nowe_dane):
        ksiazki_do_edycji = self.wyszukaj_ksiazke(tytul=tytul)
        if ksiazki_do_edycji:
            if len(ksiazki_do_edycji) > 1:
                print("Znaleziono kilka książek o tym tytule. Podaj dokładniejsze dane.")
            else:
                ksiazka = ksiazki_do_edycji[0]
                ksiazka.tytul = nowe_dane.get("tytul", ksiazka.tytul)
                ksiazka.autor = nowe_dane.get("autor", ksiazka.autor)
                ksiazka.rok_wydania = int(nowe_dane.get("rok_wydania", ksiazka.rok_wydania))  # Konwersja na int
                ksiazka.liczba_stron = int(nowe_dane.get("liczba_stron", ksiazka.liczba_stron)) # Konwersja na int
                ksiazka.dostepne = int(nowe_dane.get("dostepne", ksiazka.dostepne))  # Konwersja na int
                print(f"Zaktualizowano książkę: '{tytul}'.")
        else:
            print(f"Nie znaleziono książki o tytule '{tytul}'.")
    def wyszukaj_ksiazke(self, tytul=None, autor=None, rok_wydania=None):
        wyniki = self.ksiazki
        if tytul:
            wyniki = [ksiazka for ksiazka in wyniki if tytul.lower() in ksiazka.tytul.lower()]
        if autor:
            wyniki = [ksiazka for ksiazka in wyniki if autor.lower() in ksiazka.autor.lower()]
        if rok_wydania:
             # Poprawne porównywanie roku wydania
             wyniki = [ksiazka for ksiazka in wyniki if rok_wydania == ksiazka.rok_wydania]
        return wyniki

    def dodaj_studenta(self, student):
        if len(self.studenci) < 15:
            self.studenci.append(student)
            print (f'Dodano studenta {student.imie}')
        else:
            print("Osiągnięto maksymalną liczbę studentów.")

    def wypozycz_ksiazke(self, tytul, student):
         # Wyszukujemy książkę (używając wyszukaj_ksiazke)
        ksiazki = self.wyszukaj_ksiazke(tytul=tytul)
        if not ksiazki:
            print(f"Nie znaleziono książki o tytule '{tytul}'.")
            return

        if len(ksiazki) > 1:
            print(f"Znaleziono więcej niż jedną książkę o tytule '{tytul}'. Proszę doprecyzować kryteria wyszukiwania.")
            return

        ksiazka = ksiazki[0]

        if ksiazka.dostepne > 0:
            if len(student.wypozyczone_ksiazki) < 5:
                ksiazka.dostepne -= 1
                student.wypozyczone_ksiazki.append(ksiazka)
                print(f"Książka '{tytul}' została wypożyczona przez {student.imie} {student.nazwisko}.")
            else:
                print(f"{student.imie} {student.nazwisko} ma już maksymalną liczbę wypożyczonych książek (5).")
        else:
            print(f"Książka '{tytul}' jest aktualnie niedostępna.")


    def oddaj_ksiazke(self, tytul, student):

        # Poprawne znajdowanie książki do oddania.  Wypożyczone książki są *obiektami* Ksiazka, nie tylko tytułami.
        ksiazka_do_oddania = None
        for ksiazka in student.wypozyczone_ksiazki:
            if ksiazka.tytul == tytul:
                ksiazka_do_oddania = ksiazka
                break

        if ksiazka_do_oddania:
            ksiazka_do_oddania.dostepne += 1
            student.wypozyczone_ksiazki.remove(ksiazka_do_oddania)
            print(f"Książka '{tytul}' została zwrócona przez {student.imie} {student.nazwisko}.")
        else:
            print(f"Student {student.imie} {student.nazwisko} nie wypożyczył książki '{tytul}'.")

    def przypomnij_o_zwrocie(self):
        for student in self.studenci:
            if student.wypozyczone_ksiazki:
                print(f"Przypomnienie dla {student.imie} {student.nazwisko}:")
                for ksiazka in student.wypozyczone_ksiazki:
                    print(f"- {ksiazka.tytul}")

    def raport(self):
        print("Raport biblioteki:")
        print("\nKsiążki:")
        for ksiazka in self.ksiazki:
            print(ksiazka)
        print("\nStudenci:")
        for student in self.studenci:
            print(student)

    def dodaj_poczatkowe_ksiazki(self):
        ksiazki_startowe = [
            ("Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954, 423, 5),
            ("Hobbit, czyli tam i z powrotem", "J.R.R. Tolkien", 1937, 310, 3),
            ("Zbrodnia i kara", "Fiodor Dostojewski", 1866, 600, 2),
            ("Mistrz i Małgorzata", "Michaił Bułhakow", 1967, 480, 4),
            ("Rok 1984", "George Orwell", 1949, 328, 6),
            ("Duma i uprzedzenie", "Jane Austen", 1813, 279, 3),
            ("Paragraf 22", "Joseph Heller", 1961, 453, 2),
            ("Mały Książę", "Antoine de Saint-Exupéry", 1943, 96, 10),
            ("Lalka", "Bolesław Prus", 1890, 700, 1),
            ("Ferdydurke", "Witold Gombrowicz", 1937, 300, 5),
            ("Pan Tadeusz", "Adam Mickiewicz", 1834, 500, 8),
            ("Chłopi", "Władysław Reymont", 1904, 900, 2),
            ("Wesele", "Stanisław Wyspiański", 1901, 150, 3),
            ("Dziady", "Adam Mickiewicz", 1823, 250, 4),
            ("Krzyżacy", "Henryk Sienkiewicz", 1900, 800, 2),
            ("Quo Vadis", "Henryk Sienkiewicz", 1896, 550, 3),
            ("Solaris", "Stanisław Lem", 1961, 250, 4),
            ("Cyberiada", "Stanisław Lem", 1965, 400, 2),
            ("Proces", "Franz Kafka", 1925, 224, 3),
            ("Zamek", "Franz Kafka", 1926, 352, 1),
            ("Sto lat samotności", "Gabriel García Márquez", 1967, 448, 4),
            ("Gra w klasy", "Julio Cortázar", 1963, 576, 2),
            ("Buszujący w zbożu", "J.D. Salinger", 1951, 277, 5),
            ("Wielki Gatsby", "F. Scott Fitzgerald", 1925, 180, 3),
            ("Ulisses", "James Joyce", 1922, 730, 1),
            ("Hamlet", "William Shakespeare", 1603, 200, 2),
             ("Makbet", "William Shakespeare", 1623, 233, 5)

        ]
        for tytul, autor, rok_wydania, liczba_stron, dostepne in ksiazki_startowe:
            self.dodaj_ksiazke(Ksiazka(tytul, autor, rok_wydania, liczba_stron, dostepne))

    def dodaj_poczatkowych_studentow(self):
        studenci = [
            ("Jan", "Kowalski"),
            ("Anna", "Nowak"),
            ("Piotr", "Wiśniewski"),
            ("Maria", "Dąbrowska"),
            ("Tomasz", "Lewandowski"),
            ("Katarzyna", "Wójcik"),
            ("Michał", "Kamiński"),
            ("Zofia", "Kowalczyk"),
            ("Grzegorz", "Zieliński"),
            ("Magdalena", "Szymańska"),
            ("Robert", "Woźniak"),
            ("Agnieszka", "Kozłowska"),
            ("Paweł", "Jankowski"),
            ("Barbara", "Kwiatkowska"),
            ("Marcin", "Kaczmarek")
]
        for imie, nazwisko in studenci:

            self.dodaj_studenta(Student(imie, nazwisko))

biblioteka = Biblioteka()

def menu():
    print("\n--- Menu Biblioteki ---")
    print("1. Dodaj książkę")
    print("2. Edytuj książkę")
    print("3. Usuń książkę")
    print("4. Wyszukaj książkę")
    print("5. Dodaj studenta")
    print("6. Wypożycz książkę")
    print("7. Oddaj książkę")
    print("8. Przypomnij o zwrocie")
    print("9. Raport")
    print("0. Wyjście")

while True:
    menu()
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        tytul = input("Tytuł: ")
        autor = input("Autor: ")
        while True:
             try:
                rok_wydania = int(input("Rok wydania: "))
                break
             except ValueError:
                print("Rok wydania musi być liczbą.")
        while True:
            try:
                liczba_stron = int(input("Liczba stron: "))
                break
            except ValueError:
                print("Liczba stron musi być liczbą.")

        while True:
             try:
                dostepne = int(input("Dostępne egzemplarze: "))
                if dostepne >=0:
                    break
                else:
                    print("Liczba egzemplarzy musi być nieujemna.")
             except ValueError:
                print("Dostępne egzemplarze muszą być liczbą.")

        biblioteka.dodaj_ksiazke(Ksiazka(tytul, autor, rok_wydania, liczba_stron, dostepne))

    elif wybor == "2":
        tytul = input("Tytuł książki do edycji: ")
        nowe_dane = {}
        nowe_dane["tytul"] = input("Nowy tytul (wciśnij Enter, aby pominąć): ")
        nowe_dane["autor"] = input("Nowy autor (wciśnij Enter, aby pominąć): ")
        rok_wydania = input("Nowy rok wydania (wciśnij Enter, aby pominąć): ")
        if rok_wydania:
            while True:
                try:
                   nowe_dane["rok_wydania"] = int(rok_wydania)
                   break
                except ValueError:
                    print("Rok wydania musi być liczbą.")
                    rok_wydania = input("Nowy rok wydania (wciśnij Enter, aby pominąć): ")
        else:
             nowe_dane["rok_wydania"] = ""

        liczba_stron = input("Nowa liczba stron (wciśnij Enter, aby pominąć): ")
        if liczba_stron:
            while True:
                try:
                    nowe_dane["liczba_stron"]= int(liczba_stron)
                    break
                except ValueError:
                    print("Liczba stron musi być liczbą.")
                    liczba_stron = input("Nowa liczba stron (wciśnij Enter, aby pominąć): ")
        else:
            nowe_dane["liczba_stron"] = ""

        dostepne = input("Nowa liczba dostępnych egzemplarzy (wciśnij Enter, aby pominąć): ")

        if dostepne:
             while True:
                try:
                    nowe_dane["dostepne"] = int(dostepne)
                    if nowe_dane["dostepne"] >= 0:
                         break
                    else:
                        print("Liczba egzemplarzy musi być nieujemna")
                        dostepne = input("Nowa liczba dostępnych egzemplarzy (wciśnij Enter, aby pominąć): ")

                except ValueError:
                    print("Dostępne egzemplarze muszą być liczbą.")
                    dostepne = input("Nowa liczba dostępnych egzemplarzy (wciśnij Enter, aby pominąć): ")
        else:
            nowe_dane["dostepne"]= ""
        biblioteka.edytuj_ksiazke(tytul, {k: v for k, v in nowe_dane.items() if v !=""})

    elif wybor == "3":
        tytul = input("Tytul książki do usunięcia: ")
        biblioteka.usun_ksiazke(tytul)

    elif wybor == "4":
        tytul = input("Tytuł (wciśnij Enter, aby pominąć): ")
        autor = input("Autor (wciśnij Enter, aby pominąć): ")
        rok_wydania_str = input("Rok wydania (wciśnij Enter, aby pominąć): ")

        rok_wydania = None
        if rok_wydania_str:
            try:
                rok_wydania = int(rok_wydania_str)
            except ValueError:
                print("Nieprawidłowy rok wydania. Wyszukiwanie bez roku.")
                # Nie ustawiamy rok_wydania, zostanie None

        wyniki = biblioteka.wyszukaj_ksiazke(tytul, autor, rok_wydania)
        if wyniki:  # Sprawdzamy, czy lista wyników nie jest pusta
            for ksiazka in wyniki:
                print(ksiazka)
        else:
            print("Nie znaleziono książek spełniających podane kryteria.")

    elif wybor == "5":
        imie = input("Imię: ")
        nazwisko = input("Nazwisko: ")
        biblioteka.dodaj_studenta(Student(imie, nazwisko))

    elif wybor == "6":
        tytul = input("Tytuł książki do wypożyczenia: ")
        imie = input("Imię studenta: ")
        nazwisko = input("Nazwisko studenta: ")
        # Poprawne wyszukiwanie studenta:
        znaleziony_student = None
        for student in biblioteka.studenci:
            if student.imie.lower() == imie.lower() and student.nazwisko.lower() == nazwisko.lower():
                znaleziony_student = student
                break

        if znaleziony_student:
            biblioteka.wypozycz_ksiazke(tytul, znaleziony_student)
        else:
            print(f"Nie znaleziono studenta o imieniu {imie} i nazwisku {nazwisko}.")

    elif wybor == "7":
        tytul = input("Tytuł książki do oddania: ")
        imie = input("Imię studenta: ")
        nazwisko = input("Nazwisko studenta: ")

        # Poprawne wyszukiwanie studenta (tak samo jak przy wypożyczaniu)
        znaleziony_student = None
        for student in biblioteka.studenci:
            if student.imie.lower() == imie.lower() and student.nazwisko.lower() == nazwisko.lower():
                znaleziony_student = student
                break

        if znaleziony_student:
            biblioteka.oddaj_ksiazke(tytul, znaleziony_student)
        else:
            print(f"Nie znaleziono studenta o imieniu {imie} i nazwisku {nazwisko}.")

    elif wybor == "8":
        biblioteka.przypomnij_o_zwrocie()

    elif wybor == "9":
        biblioteka.raport()

    elif wybor == "0":
        break  # Wyjście z pętli while

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")

