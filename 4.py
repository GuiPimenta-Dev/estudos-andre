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

class Rengar():
    energy = 300
    
    def Q(self):
        energia_suficiente = self.valida_energia (30)
        if energia_suficiente is True:   
            print("Rengar usou Q: Savagery")
    def W(self):    
        energia_suficiente = self.valida_energia (40)
        if energia_suficiente is True:   
            print("Rengar usou W: Battle Roar")  
    def E(self):
        energia_suficiente = self.valida_energia (50)
        if energia_suficiente is True:   
            print("Rengar usou E: Bola Bola")
    def R(self): 
        energia_suficiente = self.valida_energia (100)
        if energia_suficiente is True:   
            print("Rengar usou R: Thrill of the Hunt")
    def valida_energia(self, outra_energia):
        energy_atualizada = self.energy - outra_energia 
        if energy_atualizada >= 0:
            self.energy = energy_atualizada
            return True
        else:
            print("Rengar não possui energia")
            return False
        
rengar = Rengar()        

print(rengar.energy)
rengar.R()

# Exercicios numero 2, criar outro campeão do lol com as mesmas regras:porém ele não pode usar a mesma skill duas vezes seguidas: se ele tentar usar 2 vezes
# printar dano ("Causou 50 de dano").