'''Criando a classe mensagem'''
class Mensagem:
    '''Classe que representa uma mensagem a ser exibida no console.
    Contém métodos para exibir mensagens simples, com quebra de linha, 
    e controlando o comportamento do print'''

    def __init__(self):
        '''Método construtor da classe.
        O parâmetro Self representa a própria instância (objeto) que 
        está sendo criada.
        self é uma conversão no Python e é usado para acessar os 
        atributos e métodos do objeto'''
        pass #No momento, não há atributos a serem declarados

    def mensagem_inicial(self):
        '''Método para exibir uma mensagem inicial no console'''
        print("Olá mundo!!")
        print("Que emoção, meu primeiro programa em POO")

    def mensagem_sem_quebra(self):
        print("Utilizando o end para manter o texto na mesma linha",end="")
        print(" Aqui temos a continuação do texto")

    def mensagem_com_quebra(self):
        print("Aqui é uma linha \n Aqui é outra linha")

if __name__ == "__main__":
    # Criar um objeto da classe Mensagem
    mensagem = Mensagem() # Aqui mensagem é uma instância da classe Mensagem   

    mensagem.mensagem_inicial()
    mensagem.mensagem_sem_quebra()
    mensagem.mensagem_com_quebra()             
