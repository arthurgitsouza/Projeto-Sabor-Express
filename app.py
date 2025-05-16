import os
import time

restaurantes = []

def exibir_nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ \n''')

def exibir_opcoes():
   print('1. Cadastrar restaurante\n2. Listar restaurantes\n3. Ativar restaurantes\n4. Sair')

def voltar_ao_menu():
    input('\nDigite uma tecla qualquer para voltar ao Menu Inicial: ')
    os.system('cls')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print('*' * len(subtitulo))
    print(subtitulo)
    print('*' * len(subtitulo))
    print()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def cadatrar_restaurantes():
    '''Essa função é responsável por cadastrar
     novos restaurantes
    
        Inputs:
        
        -- Nome
        -- Categoria

        Outputs:

        -- Adiciona um novo restaurante na lista de restaurantes.
    '''
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome':nome_do_restaurante, 'Categoria':categoria, 'Ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante}, foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    os.system('cls')
    for restaurante in restaurantes:
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f'{'Nome do Restaurante'.ljust(25)} {'Categoria'.ljust(20)} Status')
        print(f'- {restaurante['Nome'].ljust(20)} | {restaurante['Categoria'].ljust(20)} | {ativo}')
    voltar_ao_menu()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterar Estado do Restaurante:')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o Status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:    
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo'] # O not inverte o valor de False para True, e vice-versa;
            mensagem = f'O restaurante: {restaurante['Nome']} foi ativado com Sucesso!' if restaurante['Ativo'] else f'O restaurante {restaurante['Nome']} foi desativado com Sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado!')
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao = int(input('Digite o número da opção escolhida: '))
        print(f'Você escolheu a opção: {opcao}')

        if opcao == 1:
            exibir_subtitulo('Cadastrar Restaurante:')
            cadatrar_restaurantes()
        elif opcao == 2:
            exibir_subtitulo('Listar Restaurantes')
            listar_restaurantes()
        elif opcao == 3:
            exibir_subtitulo('Ativar Restaurantes')
            alterar_estado_do_restaurante()
        elif opcao == 4:
            exibir_subtitulo('Programa Finalizado!')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcoes()

if __name__ == '__main__':
   main()