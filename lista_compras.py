import os 
from random import randint

produtos = []

def listar_produtos(lista):
    if len(lista) > 0:
        print(f'{'Nome'.ljust(20)} | {'Quantidade'.ljust(20)} | {'Descrição'.ljust(50)} | ID')
        for produto in lista:
            plural_ou_singular = 's' if produto['quantidade'] > 1 else ''
            mensagem_quantidade = f'{produto['quantidade']} {produto['medida'] + plural_ou_singular}'
            mensagem_descricao = '-- SEM DESCRIÇÃO --' if len(produto['descrição']) == 0 else produto['descrição'] 
            print(f'{produto['nome'].ljust(20)} | {mensagem_quantidade.ljust(20)} | {mensagem_descricao.ljust(50)} | {produto['ID']}')
    else:
        print('-- SEM PRODUTOS NA LISTA --')

def exibir_titulo_do_programa():
    print('''
▒█░░░ ░▀░ █▀▀ ▀▀█▀▀ █▀▀█ 　 █▀▀▄ █▀▀ 　 ▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀ 
▒█░░░ ▀█▀ ▀▀█ ░░█░░ █▄▄█ 　 █░░█ █▀▀ 　 ▒█░░░ █░░█ █░▀░█ █░░█ █▄▄▀ █▄▄█ ▀▀█ 
▒█▄▄█ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ 　 ▀▀▀░ ▀▀▀ 　 ▒█▄▄█ ▀▀▀▀ ▀░░░▀ █▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀\n''')

def exibir_menu_principal():
    os.system('cls')
    exibir_titulo_do_programa()

    listar_produtos(produtos)

    print('\nOPÇÕES:')
    print('1. Adicionar produto')
    print('2. Remover produto')
    print('3. Pesquisar produtos')
    print('4. Sair do programa\n')

def exibir_subtitulo(texto):
    os.system('cls')
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))
    print()

def voltar_ao_menu():
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida! Certifique-se e tente novamente.')  
    voltar_ao_menu()

def adicionar_produto():
    exibir_subtitulo('Adicionar Produto')

    produto_nome = input('Digite o nome do novo produto: ')
    if produto_nome in [produto['nome'] for produto in produtos]:
        print(f'O produto {produto_nome} já está adicionado na lista! Se deseja adicionar mesmo assim, remova-o da lista primeiro.')
        return voltar_ao_menu()

    produto_unidade_medida = input('\nDigite a unidade de medida \n Opções:\n• Quilograma   • Grama   • Litro\n• Mililitro   • Unidade   • Metro   • Centímetro\nMedida: ').lower()
    if produto_unidade_medida not in ['quilograma', 'grama', 'litro', 'mililitro', 'unidade', 'metro', 'centímetro']:
        return opcao_invalida()
    
    try:
        produto_quantidade = int(input('Digite a quantidade do produto: '))
        if produto_quantidade < 1:
            raise ValueError
    except ValueError:
        print('\nErro. Insira um valor numérico válido para a quantidade do produto!')
        return voltar_ao_menu()

    produto_descricao = input('Digite a descrição do produto: ')

    id = produto_nome[0] + str(randint(1, 999))
    while id in [produto['ID'] for produto in produtos]:
        id = produto_nome[0] + str(randint(1, 999))


    produtos.append({'nome':produto_nome, 'medida':produto_unidade_medida, 'quantidade':produto_quantidade, 'descrição':produto_descricao, 'ID':id})
    print(f'\nProduto {produto_nome} adicionado com sucesso!')
    
    voltar_ao_menu()

def remover_produto():
    exibir_subtitulo('Remoção de produtos')

    id_produto_a_remover = input('Digite o ID do produto a ser removido: ')
    produto_removido = False
    for produto in produtos:
        if produto['ID'] == id_produto_a_remover:
            nome_do_produto = produto['nome']
            produtos.remove(produto)
            produto_removido = True

    if produto_removido == True:
        print(f'Produto {nome_do_produto} removido com sucesso!')
    else:
        print(f'Não foi possível encontrar o produto com o ID ({id_produto_a_remover}) especificado.')

    voltar_ao_menu()

def pesquisar_produtos():
    exibir_subtitulo('Pesquisar produtos')

    produto_pesquisado = input('Digite o nome do produto que deseja pesquisar: ')
    produtos_encontrados = [produto for produto in produtos if produto_pesquisado in produto['nome'].lower()]
    print('\nProdutos encontrados com base na sua pesquisa:')
    if len(produtos_encontrados) > 0:
        listar_produtos(produtos_encontrados)
    else:
        print('Nenhum produto encontrado.')

    voltar_ao_menu()

def finalizar_programa():
    os.system('cls')
    exibir_subtitulo('Encerrando Lista de Compras')
    exit()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Insira uma das opções: '))
        match opcao_escolhida:
            case 1: 
                adicionar_produto()
            case 2:
                remover_produto()
            case 3:
                pesquisar_produtos()
            case 4:
                finalizar_programa()
            case _:
                opcao_invalida()
    except ValueError:
        print('\nOpção inválida. Escolha uma das opções válidas listadas.')
        voltar_ao_menu()


def main():
    exibir_menu_principal()
    escolher_opcao()

if __name__ == '__main__':
    main()