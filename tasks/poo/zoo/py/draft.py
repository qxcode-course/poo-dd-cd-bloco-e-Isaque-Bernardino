from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")
    @abstractmethod
    def fazer_som(self) -> None:
        pass
    @abstractmethod
    def mover(self) -> None:
        pass

def apresentar(animal: Animal):
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(animal)

class Leao(Animal):
    def __init__(self) -> None:
        super().__init__("Leo")
    def fazer_som(self):
        print("Rooooar!")
    def mover(self):
        print("Scrrt… scrrt…") 
    def __str__(self):
        return "Leão é um Animal"
class Elefante(Animal):
    def __init__(self) -> None:
        super().__init__("Biu")
    def fazer_som(self):
        print("Brrrooooooh!")
    def mover(self):
        print("THOOOM… THOOOM…")
    def __str__(self):
        return "Elefante é um Animal"
class Cobra(Animal):
    def __init__(self) -> None:
        super().__init__("Voldemort")
    def fazer_som(self):
        print("Ssssss!")
    def mover(self):
        print("Fssss…")
    def __str__(self):
        return "Cobra é um Animal"

animais = [Leao(), Elefante(), Cobra()]
for animal in animais:
    apresentar(animal)
    print()