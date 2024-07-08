
#### CLASSES ####

# class Carro():
  
#   velocidade = 0
  
#   def acelerar(self, outra_velocidade):
#     self.velocidade = self.velocidade + outra_velocidade

#   def freiar(self, outra_velocidade):
#     self.velocidade = self.velocidade - outra_velocidade

# # Instanciando um objeto a partir da classe Carro
# corvete = Carro()
# print(corvete.velocidade)

# corvete.acelerar(10)
# print(corvete.velocidade)

# corvete.acelerar(50)
# print(corvete.velocidade)

# corvete.acelerar(40)
# print(corvete.velocidade)

# corvete.freiar(20)
# print(corvete.velocidade)

# Exercicio 1: Rengar
# Instrucao: Escreva uma classe chamada Rengar que tenha 4 métodos: Q, W, E, R.
# O Rengar deve ter uma propriedade Energia, que comeca em 500.
# O método Q deve imprimir "Rengar usou Q: Savagery, Este metodo deve diminuir a energia em 30"
# O método W deve imprimir "Rengar usou W: Battle Roar, Este metodo deve diminuir a energia em 40"
# O método E deve imprimir "Rengar usou E: Bola Bola, Este metodo deve diminuir a energia em 50"
# O método R deve imprimir "Rengar usou R: Thrill of the Hunt, Este metodo deve diminuir a energia em 100"
# Caso a energia seja menor que o custo de um dos métodos, o método deve imprimir "Rengar não tem energia suficiente para usar este método"

#class Rengar():
 #   energy = 300
    
 #   def Q(self):
 #       energia_suficiente = self.valida_energia (30)
 #       if energia_suficiente is True:   
 #           print("Rengar usou Q: Savagery")
  #  def W(self):    
 #       energia_suficiente = self.valida_energia (40)
  #      if energia_suficiente is True:   
 #           print("Rengar usou W: Battle Roar")  
#    def E(self):
  #      energia_suficiente = self.valida_energia (50)
   #     if energia_suficiente is True:   
  #          print("Rengar usou E: Bola Bola")
  #  def R(self): 
  #      energia_suficiente = self.valida_energia (100)
  #      if energia_suficiente is True:   
  #          print("Rengar usou R: Thrill of the Hunt")
 #   def valida_energia(self, outra_energia):
 #       energy_atualizada = self.energy - outra_energia 
 #       if energy_atualizada >= 0:
 #           self.energy = energy_atualizada
 #           return True
 #       else:
 #           print("Rengar não possui energia")
 #           return False
        
#rengar = Rengar()        

#print(rengar.energy)
#rengar.R()

# Exercicios numero 2, criar outro campeão do lol com as mesmas regras:porém ele não pode usar a mesma skill duas vezes seguidas: se ele tentar usar 2 vezes
# printar dano ("Causou 50 de dano").
'''
import time


class Ryze():
    mana=1000
    
    def __init__(self):
        self.last_used_time = {"Q": 0, "W": 0, "E": 0, "R": 0}
        self.cooldown = 1.5
        
    def Q(self):
        if self.check_cooldown("Q"):
            mana_suficiente = self.valida_mana (60)
            if mana_suficiente is True:
                print("Ryze usou Q")
                print("100 de dano causado")
                self.last_used_time["Q"] = time.time()
                
    def W(self):
        if self.check_cooldown("W"):
            mana_suficiente = self.valida_mana (50)
            if mana_suficiente is True:
                print("Ryze usou W")
                print("80 de dano causado")
                self.last_used_time["W"] = time.time()
                
    def E(self):
        if self.check_cooldown("E"):
            mana_suficiente = self.valida_mana (80)
            if mana_suficiente is True:
                print("Ryze usou E")
                print("50 de dano causado")
                self.last_used_time["E"] = time.time()
            
    def R(self):
        if self.check_cooldown("R"):
            mana_suficiente = self.valida_mana (150)
            if mana_suficiente is True:
                print("Ryze usou R")
                self.last_used_time["R"] = time.time()
        
    def valida_mana(self, falta_mana):
        mana_atualizada= self.mana - falta_mana
        if mana_atualizada >= 0:
            self.mana = mana_atualizada
            return True
        else:
            print("Ryze esta sem mana")
            return False
        
    def check_cooldown(self, skill):
        current_time = time.time()
        if current_time - self.last_used_time[skill] >= self.cooldown:
            return True
        else:
            print(f"{skill} está em cooldown")
            return False
        
ryze= Ryze()

print(ryze.mana)
ryze.Q()
ryze.Q()
ryze.E()
ryze.E()
ryze.W()
ryze.W()
ryze.Q()
ryze.R()
ryze.R()
print(ryze.mana)
'''

# Exercicios 3, criar Uma luta entre Rengar e Ryze, Adicione as propriedades: Dano (por skill), Vida (1000 para ambos), Ataque Basico.
# A luta deve durar até um dos dois campeões ficar com a vida menor ou igual a 0.
# O cooldown de cada skill é de 1.5 segundos, e da ultimate é 5 segundos.
# Caso o campeão não tenha mana suficiente para usar uma skill, ele deve usar somente o ataque basico.

class Boneco:
    def __init__(self, nome, vida, ataque_basico, dano_skill, dano_ult, cooldown_skill, cooldown_ult):
        self.nome = nome
        self.vida = vida
        self.ataque_basico = ataque_basico
        self.dano_skill = dano_skill
        self.dano_ult = dano_ult
        self.cooldown_skill = cooldown_skill
        self.cooldown_ult = cooldown_ult
        self.ultima_skill = -cooldown_skill  
        self.ultima_ult = -cooldown_ult
        
    def atacar(self, inimigo, tempo_atual):
        if tempo_atual - self.ultima_ult >= self.cooldown_ult:
            print(f"{self.nome} usa ultimate em {inimigo.nome} causando
                  {self.dano_skill} de dano!")
            inimigo.vida -= self.ultima_ult
            self.ultima_ult = tempo_atual
        elif tempo_atual - self.ultima_skill >= self.cooldown_skill:
            print(f"{self.nome} usa uma skill em {inimigo.nome}causando
                  {self.dano_skill} de dano!!!")
            inimigo.vida -= self.dano_skill
            self.ultima_skill = tempo_atual
        else:
            print(f"{self.nome} deu ataque basico em {inimigo.nome} causando
                  {self.ataque_basico} de dano ao inimgo!!")
            inimigo.vida -= self.ataque_basico
            
        
            
         
                 

        