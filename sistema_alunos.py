# Sistema de Cadastro de Alunos
# Projeto Python - Parte 1

# Lista que vai guardar todos os alunos.
# Cada aluno será um dicionário: {"nome": ..., "idade": ..., "nota": ...}
alunos = []


def exibir_menu():
    print('\n========== MENU ==========')
    print('1. Adicionar aluno')
    print('2. Listar todos os alunos')
    print('3. Buscar aluno pelo nome')
    print('4. Remover aluno')
    print('5. Mostrar média geral das notas')
    print('6. Sair')
    print('==========================')


def ler_idade():
    # Repete até o usuário digitar uma idade válida
    while True:
        idade = input('Digite a idade: ')
        if idade.isdigit() and int(idade) > 0:
            return int(idade)
        print('Idade inválida! Digite apenas números inteiros maiores que 0.')


def ler_nota():
    # Repete até o usuário digitar uma nota entre 0 e 10
    while True:
        texto = input('Digite a nota (0 a 10): ').replace(',', '.')
        try:
            nota = float(texto)
        except ValueError:
            print('Nota inválida! Digite um número (ex: 7.5).')
            continue
        if nota >= 0 and nota <= 10:
            return nota
        print('A nota deve estar entre 0 e 10.')


def adicionar_aluno():
    nome = input('Digite o nome do aluno: ').strip()
    if nome == '':
        print('O nome não pode ficar vazio.')
        return

    idade = ler_idade()
    nota = ler_nota()

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }
    alunos.append(aluno)
    print(f'Aluno {nome} cadastrado com sucesso!')


def listar_alunos():
    if len(alunos) == 0:
        print('Nenhum aluno cadastrado.')
        return

    print('\n--- Lista de alunos ---')
    for pos, aluno in enumerate(alunos, start=1):
        print(f'{pos}. Nome: {aluno["nome"]} | Idade: {aluno["idade"]} | Nota: {aluno["nota"]}')


def buscar_aluno():
    nome = input('Digite o nome do aluno que deseja buscar: ').strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print('\nAluno encontrado:')
            print(f'Nome: {aluno["nome"]}')
            print(f'Idade: {aluno["idade"]}')
            print(f'Nota: {aluno["nota"]}')
            return

    print(f'Erro: aluno "{nome}" não encontrado.')


def remover_aluno():
    nome = input('Digite o nome do aluno que deseja remover: ').strip()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print(f'Aluno {aluno["nome"]} removido com sucesso!')
            return

    print(f'Aviso: aluno "{nome}" não encontrado.')


def mostrar_media():
    if len(alunos) == 0:
        print('Não há alunos cadastrados para calcular a média.')
        return

    soma = 0
    for aluno in alunos:
        soma += aluno["nota"]

    media = soma / len(alunos)
    print(f'Média geral das notas: {media:.2f}')


# Loop principal: o programa fica rodando até o usuário escolher 6
while True:
    exibir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        listar_alunos()
    elif opcao == '3':
        buscar_aluno()
    elif opcao == '4':
        remover_aluno()
    elif opcao == '5':
        mostrar_media()
    elif opcao == '6':
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida! Escolha um número de 1 a 6.')
