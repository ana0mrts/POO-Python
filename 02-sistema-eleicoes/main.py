import pickle
import traceback
from common import Eleitor, Candidato

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu_eleitor():
    print("\n--- MENU ---")
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Novo Candidato")
    print("4-Atualizar Candidato")
    print("5-Listar Todos")
    print("6-Sair")
    op = int(input("Digite a opcao [1-6]? "))
    while op not in (1, 2, 3, 4, 5, 6):
        op = int(input("Opcao invalida! Digite novamente [1-6]? "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def inserir_candidato(candidatos):
    numero = int(input("Digite o Numero do Candidato: "))
    if numero in candidatos:
        raise Exception("Numero ja existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def atualizar_candidato(candidatos):
    numero = int(input('Digite o numero do candidato: '))
    if numero in candidatos:
        candidato = candidatos[numero]
        print(candidato)
        nome = input("Digite o novo nome: ")
        RG = input("Digite o novo RG: ")
        CPF = input("Digite o novo CPF: ")
        candidato._Pessoa__nome = nome
        candidato._Pessoa__RG = RG
        candidato._Pessoa__CPF = CPF

        with open(FILE_CANDIDATOS, 'wb') as arquivo:
            pickle.dump(candidatos, arquivo)

        print('Atualizados dados do candidato!')
        print(candidato)
    else:
        raise Exception('Candidato inexistente')

def listar_todos(eleitores, candidatos):
    print("\n--- ELEITORES ---")
    if not eleitores:
        print("Nenhum eleitor cadastrado.")
    for eleitor in eleitores.values():
        print(eleitor)

    print("\n--- CANDIDATOS ---")
    if not candidatos:
        print("Nenhum candidato cadastrado.")
    for candidato in candidatos.values():
        print(candidato)


if __name__ == "__main__":
    eleitores = {} 
    candidatos = {}

    try:
        print("Carregando arquivo de eleitores ...")
        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de eleitores nao encontrado, nenhum eleitor carregado!")

    try:
        print("Carregando arquivo de candidatos ...")
        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de candidatos nao encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao != 6:
        try:
            opcao = menu_eleitor()

            if opcao == 1:
                inserir_eleitor(eleitores)
            elif opcao == 2:
                atualizar_eleitor(eleitores)
            elif opcao == 3:
                inserir_candidato(candidatos)
            elif opcao == 4:
                atualizar_candidato(candidatos)
            elif opcao == 5:
                listar_todos(eleitores, candidatos)
            elif opcao == 6:
                print("Saindo!")
                break
        except Exception as e:
            #traceback.print_exc()
            print(e)
