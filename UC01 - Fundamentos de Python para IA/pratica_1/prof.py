#classe Destino
class Destino:
    def __init__(self, nome, clima, tipo, custo):
      self.nome = nome
      self.clima = clima
      self.tipo = tipo
      self.custo = custo
   
    def combina_com(self,clima, tipo, orcamento):
      return(self.clima == clima and
             self.tipo == tipo and
             self.custo <= orcamento
             )
    
#Lista de destinos disponíveis
destinos = [
    Destino("Rio de Janeiro", "quente", "cidade", 2000),
    Destino("Gramado", "frio", "cidade", 2500),
    Destino("Lençóis Maranhenses", "quente", "natureza", 1800),
    Destino("Campos do Jordão", "frio", "natureza", 2300)
]


#Coleta de preferências
 
print("Vamos encontrar seu destino ideal!")
 
clima = input("Prefere clima quente ou frio?").strip().lower()
tipo = input("Prefere natureza ou cidade?").strip().lower()
orcamento = float(input("Qual é o seu orçamento máximo (R$)?"))

#Coleta de preferências
 
print("Vamos encontrar seu destino ideal!")
 
clima = input("Prefere clima quente ou frio?").strip().lower()
tipo = input("Prefere natureza ou cidade?").strip().lower()
orcamento = float(input("Qual é o seu orçamento máximo (R$)?"))
 
#Busca por destino
encontrado = False
 
for destino in destinos:
  if destino.combina_com(clima, tipo, orcamento):
    print(f"\nSugestão:{destino.nome}")
    print("Boa viagem!")
    encontrado = True
    break
 
if not encontrado:
  print("Infelizmente, não encontramos destinos compatíveis com suas preferências.")