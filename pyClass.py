#Example for classes in Python
import json

class Life:
    reino = ""
    celulas = ""
    fonteEnergia = ""
    nome = ""
    
    def morre(self, causaMorte):
        print(f"{self.nome} morreu {causaMorte}")
    
        
class Animal(Life):
    movimento = None
    def __init__(self, prop: object):
            self.reino = "Animal"
            self.celulas = "Multicelular"
            self.fonteEnergia = "Trófico"
            self.nome = prop["nome"]
            self.movimento = prop["movimento"]

    def movimenta(self):
        if type(self.movimento) == str:
            print(self.nome + " " + self.movimento)
        else:
            print("<<<Movimento ainda não definido!>>>")
    
class Planta(Life):
    altura = None
    def __init__(self, prop: object):
        self.reino = "Planta"
        self.celulas = "Multicelular"
        self.fonteEnergia = "Autotrófico"
        self.nome = prop["nome"]
        self.altura = prop["altura"]
        
    def mede(self):
        if type(self.altura) == int:
            print(f"{self.nome} mede {self.altura} metros")
        else:
            print("<<<Altura ainda não definida!>>>")
    
def printLife(life):
    serialized = json.dumps(life, default=lambda x: x.__dict__)
    print("------------")
    print("")
    print(serialized)
    print("")
        
Leao = Animal({ "nome": "Leão",
             "movimento": "corre" })

Aguia = Animal({ "nome": "Águia",
             "movimento": "voa" })

Sumauma = Planta({ "nome": "Sumauma",
                  "altura": 60 })

Embauba = Planta({"nome": "Embaúba",
                  "altura": 15 })

Leao.movimenta()
Aguia.movimenta()
Sumauma.mede()
Embauba.mede()

printLife(Leao)
printLife(Aguia)
printLife(Sumauma)
printLife(Embauba)

Leao.morre("de velhice.")