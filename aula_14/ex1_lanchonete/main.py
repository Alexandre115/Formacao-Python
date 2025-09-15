from lanchonete import registrar_pedido

def main():
    while True:
        print("## Lanchonete peito de Pomba ##")
        registrar_pedido()
        continuar = input("Deseja registrar um novo pedido (S/N): ")
        print("-"*30)
        if continuar.lower() != 's':
            print("Sistema finalizado")
            break

if __name__ == "__main__":
    main()        