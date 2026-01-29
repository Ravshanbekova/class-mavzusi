class Transport:
    def __init__(self, model: str, yil: int) -> None:
        self.model = model
        self.yil = yil

    def malumot(self) -> str:
        return f"Model: {self.model}, Yil: {self.yil}"

class Avtomobil(Transport):
    def __init__(self, model: str, yil: int, yonilgi_turi: str) -> None:
        super().__init__(model, yil)
        self.yonilgi_turi = yonilgi_turi

    def malumot(self) -> str:
        baza = super().malumot()
        return f"{baza}, Yonilg'i: {self.yonilgi_turi}"

class Avtobus(Transport):
    def __init__(self, model: str, yil: int, orinlar_soni: int) -> None:
        super().__init__(model, yil)
        self.orindiqlar_soni = orinlar_soni

    def malumot(self) -> str:
        baza = super().malumot()
        return f"{baza}, O'rinlar: {self.orindiqlar_soni}"

a = Avtomobil("Nexia", 2020, "benzin")
print(a.malumot())

b = Avtobus("Isusu", 2010, 26)
print(b.malumot())