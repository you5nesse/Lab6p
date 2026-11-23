from dataclasses import dataclass, asdict ,replace
import json

@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)
    def promo(self, prix_reduit):
        return replace(self, prix=prix_reduit)
livre = Livre("Inverting the pyramid", "Jonathan Wilson", 2008, 50.0)
print(livre.to_json())
Livre_promo = livre.promo(42.0)
print("Livre en promotion :", Livre_promo.to_json())