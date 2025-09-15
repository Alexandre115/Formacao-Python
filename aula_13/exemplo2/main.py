from notas import cadastrar_aluno

def main():
    #cadastrar_aluno()
    while True:
        print("## Sistema de notas ##")
        cadastrar_aluno()
        continuar = input("Deseja cadastrar um novo aluno (S/N): ")
        print("="*30)
        if continuar.lower() != 's':
            print("Cadastro finalizado.")
            break

if __name__ == "__main__":
    main()    