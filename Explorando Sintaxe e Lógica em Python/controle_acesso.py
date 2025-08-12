'''Controle de Acesso Inteligente
Uma biblioteca está implementando um sistema automatizado para 
liberar o acesso à área de livros raros. O sistema deve permitir a 
entrada apenas para visitantes autorizados e com idade mínima de 18 anos. 
Para isso, é necessário utilizar operadores lógicos, estruturas condicionais (if, else, else if) e 
conceitos básicos como tipos primitivos e palavras-chave. Desenvolva um programa que verifique se o 
visitante pode acessar a sala especial.
'''

def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"  
    age = int(input()) 

    print
    # TODO: Verifique condições de acesso
    
    if not has_permission:
        print("Acesso negado")
    elif age >= 18:
        print("Acesso permitido")
    else:
        print("Idade insuficiente")        

if __name__ == "__main__":
    main()