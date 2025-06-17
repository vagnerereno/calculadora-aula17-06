import csv

if __name__ == '__main__':

    # Exercício 1: Escreva uma função em Python que aceite um nome de arquivo e
    # um texto como parâmetros e escreva o texto no arquivo com o nome especificado.
    def escrever_texto(nome_arquivo, texto):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(texto)

    # escrever_texto("meu_arquivo.txt", "Olá mundo! Programando em Python!")

    # Exercício 2: Crie uma função em Python que leia e retorne o conteúdo de um
    # arquivo de texto dado o seu nome.
    def ler_texto(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()

    # conteudo = ler_texto("meu_arquivo.txt")
    # print(conteudo)

    # Exercício 3: Modifique a função de escrita do Exercício 1 para adicionar linhas
    # a um arquivo de texto existente sem sobrescrever o conteúdo atual.
    def adicionar_linha_texto(nome_arquivo, texto):
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(texto + "\n")

    # adicionar_linha_texto("meu_arquivo.txt", "Olá mundo! Programando em Python!")

    # Exercício 4: Escreva uma função que crie um arquivo CSV chamado dados.csv
    # e escreva as seguintes informações: nome, idade e cidade de três pessoas.
    def salvar_em_csv(dados):
        with open('dados.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            escritor.writerows(dados)

    dados = [
        ['Ana', 30, 'São Paulo'],
        ['João', 25, 'Rio de Janeiro'],
        ['Jorge', 40, 'São Paulo']
    ]

    # salvar_em_csv(dados)

    # Exercício 5: Crie uma função que leia o arquivo dados.csv criado
    # no Exercício 4 e imprima cada linha do arquivo.
    def ler_csv(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)

    ler_csv('dados.csv')