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
   print('1. Cadastrar restaurante\n2. Listar restaurantes\n3. Listar restaurantes\n4. Sair')

def voltar_ao_menu():
    time.sleep(3 )
    os.system('cls')
    input('Digite uma tecla qualquer para voltar ao Menu Inicial: ')
    os.system('cls')
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(subtitulo)
    print()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

def cadatrar_restaurantes():
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante}, foi cadastrado com sucesso!\n')
    voltar_ao_menu()

def listar_restaurantes():
    os.system('cls')
    for i in restaurantes:
        print(f'- {i}')
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao = int(input('Digite o número da opção escolhida: '))
        print(f'Você escolheu a opção: {opcao}')

        if opcao == 1:
            exibir_subtitulo('Cadastrar Restaurante:')
            cadatrar_restaurantes()
        elif opcao == 2:
            exibir_subtitulo('Listar restaurantes')
            listar_restaurantes()
        elif opcao == 3:
            exibir_subtitulo('Listar restaurantes')
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