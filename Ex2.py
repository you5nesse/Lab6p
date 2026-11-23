
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être comprise entre 0 et 10")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    def __lt__(self, autre):
        return self.note < autre.note


# Création des films
film1 = Film("Inception", "Christopher Nolan", 2010, 8.8)
film2 = Film("Titanic", "James Cameron", 1997, 7.9)
film3 = Film("Interstellar", "Christopher Nolan", 2014, 9.0)

# Sérialisation JSON
print("Film 1 :", film1.to_json())

# Vérifier si le film est classique
print("Titanic est classique :", film2.est_classique())

# Comparaison des films
print("Film 1 > Film 2 :", film1 > film2)

# Trier les films par note croissante
films = [film1, film2, film3]
films_tries = sorted(films)

print("\nFilms triés par note croissante :")
for film in films_tries:
    print(film.titre, "-", film.note)
