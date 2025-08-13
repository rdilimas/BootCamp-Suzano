'''
Um sistema de monitoramento de bicicletas compartilhadas precisa calcular a 
distância máxima que cada bicicleta pode percorrer, com base no nível atual de 
bateria. Cada 1% de bateria permite percorrer 0,5 km. Neste desafio, você deve 
utilizar os conceitos de Programação Orientada a Objetos (POO) para modelar a 
bicicleta. Crie uma classe que contenha os atributos necessários e um método para 
calcular a distância estimada.
'''

class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        # TODO: Calcule a distância estimada com base no nível de bateria
        distancia = self.nivel_bateria * 0.5
        return distancia
        

    def obter_mensagem(self, distancia):
        # TODO: Retorne a mensagem formatada com o modelo e a distância
        print(self.modelo+":", " Distancia estimada = ", distancia, " km")

def main():
    
    modelo = input()
    
    nivel_str = input()
    nivel_bateria = int(nivel_str)

    # TODO: Crie o objeto BicicletaInterna com os dados lidos
    
    bicicleta = BicicletaInterna(modelo, nivel_bateria)
    
    x = (bicicleta.calcular_distancia())

    bicicleta.obter_mensagem(x)


if __name__ == "__main__":
    main()