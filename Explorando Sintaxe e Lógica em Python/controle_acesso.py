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