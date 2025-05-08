alunos = [{'aluno':'Gustavo', 'idade': 15, 'nota final':10}]

def cadastro_aluno():
    estudante = input('Digite o nome do aluno que deseja cadastrar: ')
    idade = int(input('Digite a idade do aluno: '))
    nota = int(input('Insira a nota final do aluno: '))
    dados_aluno = {'aluno':estudante, 'idade':idade, 'nota final': nota}
    alunos.append(dados_aluno)
    for aluno in alunos:
        nome_aluno = aluno['aluno']
        idade_aluno = aluno['idade']
        nota_aluno = aluno['nota final']
        print(f'Nome do aluno: {nome_aluno}, Idade: {idade_aluno}, nota final: {nota_aluno}')

cadastro_aluno()