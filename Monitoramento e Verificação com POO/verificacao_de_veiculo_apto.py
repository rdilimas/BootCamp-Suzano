'''
Um aplicativo de monitoramento de carros precisa verificar se um carro está apto
 para rodar com base no ano de fabricação e no ano atual. Um carro é considerado 
 apto se tiver até 10 anos de uso. Para resolver este desafio, você deve utilizar 
 conceitos de Programação Orientada a Objetos (POO), como a definição de métodos 
 estáticos, para realizar a verificação da aptidão do carro sem a necessidade de 
 instanciar objetos. A aplicação de POO deve ser utilizada para organizar a lógica
   de verificação do carro e para retornar o resultado da aptidão de forma estruturada.
'''

def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):
    
    idade_carro = ano_atual - ano_fabricacao
    carro_apto = "Nao apto"
    # TODO: Verifique se o carro está apto com base na idade

    if idade_carro <= 10:
      carro_apto = "Apto"
     
    print(modelo+":", carro_apto)
    


def main():
    
    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    # TODO: Chame a função para verificar a aptidão do carro
    
    verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual)
   



if __name__ == "__main__":
    main()