from datetime import datetime
# Sistema de notas
print("## Sistema de notas ##")
quant = int(input("Informe a quantidade de registros que deseja realizar: "))

soma_medias = 0
dados_arquivo = []

for i in range(1, quant + 1):
    print("="*30)
    nome = input("Informe o nome do aluno: ")
    turma = input("Informe a turma: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    media = (n1+n2+n3) / 3
    soma_medias += media

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"


    # Exibir na tela as informações
    print("#"*30)
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Primeira nota: {n1}")
    print(f"Segunda nota: {n2}")
    print(f"Terceira nota: {n3}")
    print(f"Média final: {media:.1f}")
    print(f"Situação curricular: {situacao}")

    # Armazena para salvar no arquivo
    registro = (
        f"Nome: {nome}\n"
        f"Turma: {turma}\n"
        f"Notas: {n1}, {n2}, {n3}\n"
        f"Média final: {media:.1f}\n"
        f"Situação curricular: {situacao}\n"
        f"{'='*30}\n"        
    )
    dados_arquivo.append(registro)

# Calculo que exibe a média geral da turma
media_geral = soma_medias / quant
print("#"*30)
print(f"Média geral da turma: {media_geral:.1f}")

# Salvar os dados no arquivo
#with open("C:/Users/MIGUELANGELOMATIOLLA/Documents/nota.txt")
# Solicita o nome do arquivo para o usuário
n_arquivo = input("Digite o nome do arquivo para salvar: ")
# Armazena na variável a data atual e hora do computador
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Armazena na variável a concatenação do nome do arquivo definido pelo usuário +
# a data e hora do sistema + .txt
nome_arquivo = n_arquivo + f" {data_hora}.txt"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("## Relatório de notas dos alunos ##")
    arquivo.writelines(dados_arquivo)
    arquivo.write(f"Média geral do registro: {media_geral:.1f}")

print("Dados salvos com sucesso!")    