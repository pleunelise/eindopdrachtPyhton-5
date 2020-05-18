class Adres:
    def __init__(self, _straat, _huisnummer, _stad, _postcode, _land):
        self.straat = _straat
        self.huisnummer = _huisnummer
        self.stad = _stad
        self.postcode = _postcode
        self.land = _land

class Persoon:
    def __init__ (self, _naam, _adres, _geboortedatum, _telefoonnummer):
        self.naam = _naam
        self.adres = _adres
        self.geboortedatum = _geboortedatum
        self.telefoonnummer = _telefoonnummer

class Medewerker(Persoon):
    def super().__init__(self, _naam, _adres, _geboortedatum, _telefoonnummer):
        self.uurprijs = _uurprijs
        self.werkuren = _werkuren

class Werkgever(Persoon):
    def super().__init__(self, _naam, _adres, _geboortedatum, _telefoonnummer):
        self.aantalmdw = _aantalmdw

x = Persoon("pleun", "goudpluvier 25", "10-01-2005", "0612345678")
y = Mederwerker("pleun", "goudpluvier 25", "10-01-2005", "0612345678", "5 euro", "4 uur")
x.naam
y.uurprijs
