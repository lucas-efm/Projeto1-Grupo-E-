# =====================================+ PROTOTIVO V1 +========================================= #

# ========= GABRIELA ALVES == GABRIEL PORTELA == LUCAS MENDES == LUCIA NEGREIROS =============== #


# ===================================== MODO DE TESTE ===========================================#

test = False  # se TRUE as contas serao criadas autmaticamente com
# valores padroes (apenas para teste de funcoes)
# SENHA » 123456
test_livros = False  # se TRUE os livros serao adiicionados autmaticamente
# com valores padroes (apenas para teste de funcoes)

# ================================= IMPORTS E DECLARACOES ====================================== #

from datetime import date, datetime  # Para calculo de idade e momento de realizacao dos posts
import difflib  # Para pesquisa por proximidade

usernames, datas_nascimento, senhas, emails, nomes, cidades = [], [], [], [], [], []
opcao, opcao_log = '', ''


titulos, editoras, autores, anos, generos, livros_por_usuario, chats, posts = [], [], [], [], [], [], [], []
finalizar = ''

end, bold = '\033[0m', '\033[1m'
red, green, blue, orange, gray = '\033[91m', '\033[32m', '\033[34m', '\033[33m', '\033[1m\033[90m'
semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]


# ================================== DEFINICOES DE FUNCOES ====================================== #

# ================================ LISTAR E SELECIONAR =================================== #

def listar_opcoes(lista):
    while True:
        for i in range(len(lista)):
            print(f"{bold}{blue}{i + 1}{end} - {lista[i]}")

        escolha = int(input(f"{gray}Selecione uma das opções:{end} \n"))

        if len(lista) >= escolha > 0:
            break
        else:
            print(f"{red}Código inválido.{end}\n")

    return escolha - 1


# ================================ VERIFICAR FORMATO DA SENHA =================================== #

def check_senha():
    print("Digite sua senha, ela deve ter de 6 a 16 Caracteres")
    while True:
        sen = input(f"{gray}Senha: {end}")
        if len(sen) < 6:
            print(f"{red}Sua senha deve ter mais de 6 dígitos{end}\n")
            continue
        elif len(sen) > 16:
            print(f"{red}Sua senha deve ter menos de 16 caracteres{end}\n")
            continue

        check = input(f"{gray}Confirme sua senha: {end}")
        if sen != check:
            print(f"{red}As senhas não são iguais{end}\n")
            continue
        else:
            break
    return sen


# =========================== VERIFICAR EXISTENCIA DO NOME DE USUARIO ============================ #

def check_username():
    print("Digite um Username, ele deve ter de 4 a 16 caracteres"),
    while True:
        username = input(f"{gray}Username: {end}")
        if username.__len__() <= 4:
            print(f"{red}Seu username deve ter mais de 4 dígitos{end}\n")
            continue
        elif username.__len__() >= 16:
            print(f"{red}Seu username deve ter menos de 16 caracteres{end}\n")
            continue
        if username in usernames:
            print(f"{red}Username não disponível{end}\n")
            continue
        else:
            break
    return username


# ================================ VERIFICAR INPUT DE NOME ====================================== #

def nome():
    return input(f"{gray}Nome completo: {end}")


# ========================= VERIFICAR FORMATO E EXISTENCIA DO EMAIL ============================== #

def check_email():
    while True:
        email = input(f"{gray}E-mail: {end}")
        if email in emails:
            print(f"{red}E-mail já cadastrado{end}\n")
            continue
        if '.' not in email and '@' not in email:  # verificar ':'?
            print(f"{red}E-mail inválido{end}\n")
        else:
            break
    return email


# ========================= VERIFICAR FORMATO DA DATA E IDADE(+18) ============================== #

def idade(nascimento):
    hoje = date.today()
    return hoje.year - nascimento[2] - ((hoje.month, hoje.day) <
                                        (nascimento[1], nascimento[0]))


def check_formato(data):
    if len(data) == 10 and data[2] == '/' and data[5] == '/' and \
            data[:2].isdigit() and data[3:5].isdigit() and data[6:].isdigit():
        return True
    return False


def check_data():
    while True:
        data = input(f"{gray}Data de nascimento (dd/mm/aaaa): {end}")
        dia_mes_ano = []
        if check_formato(data):
            dia_mes_ano = data.split('/')
            dia_mes_ano[0] = int(dia_mes_ano[0])
            dia_mes_ano[1] = int(dia_mes_ano[1])
            dia_mes_ano[2] = int(dia_mes_ano[2])
            if idade(dia_mes_ano) >= 18:
                break
            else:
                print(
                    f"{red}Idade inválida, só é permitido maiores de 18{end}\n"
                )
                continue
        else:
            print(f"{red}Formato inválido{end}\n")
            continue
    return dia_mes_ano


# ================================ VERIFICAR CIDADE =================================== #

def cidade():
    while True:
        sn = input(
            "Você mora em Recife?"
            f"\n{blue}{bold}S{end}{gray} - Sim / {blue}{bold}N{end}{gray} - Não: {end}").upper()
        if sn == 'S':
            cid = "Recife"
            break
        elif sn == 'N':
            cid = input(f"{gray}Digite o nome da sua cidade: {end}")
            print(
                f"{red}Você pode entrar na plataforma, mas não pode realizar trocas.\n{end}"
            )
            break
    return cid


# ================================ ESCOLHA GÊNERO =================================== #
# Pretendemos utilizar a funcao listar e selecionar para nao precisarmos mais desta

def escolha_genero():
    print(f"\nEscolha o Gênero: "
          f"\n{bold}{blue}1{end} - Autoajuda"
          f"\n{bold}{blue}2{end} - Científico"
          f"\n{bold}{blue}3{end} - Comédia"
          f"\n{bold}{blue}4{end} - Drama"
          f"\n{bold}{blue}5{end} - Fantasia"
          f"\n{bold}{blue}6{end} - Ficção"
          f"\n{bold}{blue}7{end} - Poesia"
          f"\n{bold}{blue}8{end} - Religião"
          f"\n{bold}{blue}9{end} - Romance"
          f"\n{bold}{blue}10{end} - Suspense"
          f"\n{bold}{blue}11{end} - Terror"
          f"\n{bold}{blue}12{end} - Outro")

    genero = input(f"\n{gray}Selecione uma das opções: {end}")

    if genero == '1':
        gen = "Autoajuda"
    elif genero == '2':
        gen = "Científico"
    elif genero == '3':
        gen = "Comédia"
    elif genero == '4':
        gen = "Drama"
    elif genero == '5':
        gen = "Fantasia"
    elif genero == '6':
        gen = "Ficção"
    elif genero == '7':
        gen = "Poesia"
    elif genero == '8':
        gen = "Religião"
    elif genero == '9':
        gen = "Romance"
    elif genero == '10':
        gen = "Suspense"
    elif genero == '11':
        gen = "Terror"
    elif genero == '12':
        gen = "Outro"
    else:
        print(f"{red}Opção inválida!{end}\n")
        gen = ''
    return gen


# ========================= INICIO DO ACESSO DO USUARIO ============================== #

while opcao_log != '-1':
    opcao_log = input(f"\n{bold}{orange}--------SWAP--------{end}"
                      f"\n{bold}{blue}1{end} - Criar Conta"
                      f"\n{bold}{blue}2{end} - Log in"
                      f"\n{bold}{blue}-1{end} - Encerrar"
                      f"\n{gray}Selecione uma das opções: {end}")

    # ======================== CRIACAO DE CONTA (APPEND(FUNCAO)) =========================== #
    # A conta no modo de teste eh criada automaticamente apenas com o nome do usuario
    # e a senha sera 123456

    if opcao_log == '1':
        print(f"\n{bold}{orange}---------CRIAR CONTA---------{end}")

        usuario = check_username()
        if test:
            usernames.append(usuario)
            senhas.append('123456')
            emails.append('cardib@bol.com')
            nomes.append('Belcalis Marlenis')
            cidades.append('New York')
            datas_nascimento.append('11/10/1992')

        else:
            usernames.append(usuario)
            senhas.append(check_senha())
            emails.append(check_email())
            nomes.append(nome())
            cidades.append(cidade())
            datas_nascimento.append(check_data())

        livros_por_usuario.append([usuario])
        chats.append([])
        editoras.append([])
        autores.append([])
        anos.append([])
        generos.append([])

        print(f"{green}Leitor cadastrado com sucesso!{end}")

    # ================================= ENTRAR NO SISTEMA =================================== #

    elif opcao_log == '2':
        while True:
            print(f"\n{bold}{orange}-------- ENTRAR --------{end}")
            usuario = input(f"{gray}Usuário: {end}")
            senha = input(f"{gray}Senha: {end}")
            logado = False
            if usuario in usernames:
                posicao = usernames.index(usuario)
                if senha == senhas[posicao]:
                    logado = True
                    print(f"{green}Login feito com sucesso!{end}")
                    break
                else:
                    print(f"{red}Senha inválida{end}\n")
                    if input(
                            f"{gray}Digite {bold}{blue}-1{end}{gray} para voltar ao cadastro"
                            f"\nou aperte {bold}{blue}enter{end}{gray} para tentar novamente: {end}"
                    ) == '-1':
                        break
                    else:
                        continue

            else:
                print(f"{red}Usuário não encontrado!{end}\n")
                if input(
                        f"{gray}Digite {bold}{blue}-1{end}{gray} para voltar ao cadastro"
                        f"\nou aperte {bold}{blue}enter{end}{gray} para tentar novamente: {end}"
                ) == '-1':
                    break
                continue
        # ========================= APOS ENTRAR, INICIO DO CRUD ============================== #

        while logado:
            print(f"\n{orange}-------- CHATS --------{end}")
            if chats[posicao]:
                for text in chats[posicao]:
                    print(text)
            else:
                print(f"{gray}Nenhuma mensagem recebida.{end}")
            print(f"\n{orange}-------- POSTS --------{end}")
            if posts:
                for text in posts:
                    print(text)
            else:
                print(f"{gray}Nenhum post feito.{bold}")
            opcao = input(f"\n{bold}{orange}-------- {usernames[posicao].upper()} --------{end}"
                          f"\n{bold}{blue}1{end} - Buscar Leitor"
                          f"\n{bold}{blue}2{end} - Editar Conta"
                          f"\n{bold}{blue}3{end} - Deletar Conta"
                          f"\n{bold}{blue}4{end} - Livros"
                          f"\n{bold}{blue}5{end} - Publicar"
                          f"\n{bold}{blue}-1{end} - Sair"
                          f"\n{gray}Selecione uma das opções: {end}")

            # ========================= BUSCAR LEITOR ============================== #

            if opcao == '1':
                print(f"\n{bold}{orange}---------BUSCAR LEITOR---------{end}")
                if usernames:
                    consulta_leitor = input(
                        f"{gray}Pesquisar por: {end}"
                    )
                    semelhantes = difflib.get_close_matches(
                        consulta_leitor, usernames, cutoff=0.5)

                    if not semelhantes:
                        print(f"{red}Leitor não encontrado!{end}\n")
                    else:
                        ind = usernames.index(
                            semelhantes[listar_opcoes(semelhantes)])
                        print(f"Username: {bold}{usernames[ind]}{end}")
                        print(f"Nome: {bold}{nomes[ind]}{end}")
                        print(f"E-mail: {bold}{emails[ind]}{end}")
                        print(f"Cidade: {bold}{cidades[ind]}{end}")
                        print(f"Livros: ")
                        for i in range(len(livros_por_usuario[ind]) - 1):
                            print(f"{i + 1} - {bold}{livros_por_usuario[ind][i + 1]}{end}")

                        print(f"Enviar mensagem para {bold}{usernames[ind]}{end}?")
                        escolha_chat = input(
                            f"{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                        ).upper()

                        if escolha_chat == 'S':
                            chat = input("Escreva: ")
                            chats[ind].append(
                                f"{bold}{green}{usernames[posicao]}{end} {green}{semana[datetime.today().weekday()]},"
                                f" {datetime.today().hour}:{datetime.today().minute}{end}: {chat}")
                else:
                    print(f"{red}Não há leitores cadastrados!{end}\n")

            # ========================= EDITAR CONTA ============================== #

            elif opcao == '2':
                print(f"\n{bold}{orange}---------EDITAR CONTA---------{end}")
                while True:
                    editar = input(
                        f"\n{blue}{bold}1{end} - Editar o Username"
                        f"\n{blue}{bold}2{end} - Editar o nome"
                        f"\n{blue}{bold}3{end} - Editar a data de nascimento"
                        f"\n{blue}{bold}4{end} - Editar a cidade"
                        f"\n{blue}{bold}5{end} - Editar o E-mail"
                        f"\n{blue}{bold}6{end} - Editar a senha:"
                        f"\n{blue}{bold}-1{end} - Sair e salvar alterações"
                        f"\n{gray}Selecione uma das opções:{end} ")

                    if editar == '1':
                        usernames[posicao] = check_username()
                        print(
                            f"{green}Username editado com sucesso!{end}\n"
                        )

                    elif editar == '2':
                        nomes[posicao] = nome()
                        print(
                            f"{green}Nome editado com sucesso!\n{end}")

                    elif editar == '3':
                        datas_nascimento[posicao] = check_data()
                        print(
                            f"{green}Data de nascimento editada com sucesso!\n{end}"
                        )

                    elif editar == '4':
                        cidades[posicao] = cidade()
                        print(
                            f"{green}Cidade editado com sucesso!\n{end}"
                        )

                    elif editar == '5':
                        emails[posicao] = check_email()
                        print(
                            f"{green}E-mail editado com sucesso!\n{end}"
                        )

                    elif editar == '6':
                        senhas[posicao] = check_senha()
                        print(
                            f"{green}Senha editada com sucesso!\n{end}"
                        )

                    elif editar == '-1':
                        print(f"{green}Alterações salvas!\n{end}")
                        break

                    else:
                        print(f"{red}Dígito incorreto!\n{end}")

            # ========================= DELETAR CONTA ===================================== #

            elif opcao == '3':
                print(f"\n{bold}{orange}---------DELETAR CONTA---------{end}")
                sim_nao = input(
                    f"Você deseja excluir sua conta?"
                    f"\n{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                )

                if sim_nao.upper() == 'S':
                    sim_nao = input(
                        f"Você tem certeza?"
                        f"\n{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                    )
                    if sim_nao.upper() == 'S':
                        usernames.pop(posicao)
                        nomes.pop(posicao)
                        datas_nascimento.pop(posicao)
                        emails.pop(posicao)
                        senhas.pop(posicao)
                        cidades.pop(posicao)
                        livros_por_usuario.pop(posicao)
                        chats.pop(posicao)
                        editoras.pop(posicao)
                        autores.pop(posicao)
                        anos.pop(posicao)
                        generos.pop(posicao)

                    print(f"{green}Conta removida com sucesso!{end}\n")

                else:
                    print(f"{red}Conta não removida!{end}\n")

            # ========================= INICIO DE CRUD(LIVRO) ============================== #

            elif opcao == '4':
                while True:
                    print(f"\n{bold}{orange}---------LIVROS---------{end}")
                    op = input(f"{bold}{blue}1{end} - Adicionar Livro"
                               f"\n{bold}{blue}2{end} - Buscar Livro"
                               f"\n{bold}{blue}3{end} - Editar Livro"
                               f"\n{bold}{blue}4{end} - Deletar Livro"
                               f"\n{bold}{blue}5{end} - Finalizar"
                               f"\n{gray}Selecione uma das opções:{end} ")

                    # ========================= CADASTRAR LIVROS ============================== #

                    if op == '1':
                        print(
                            f"\n{bold}{orange}---------ADICIONAR LIVRO---------{end}"
                        )
                        titulo = (input(f"{gray}Digite o título do livro: {end}"))
                        if test_livros:
                            livros_por_usuario[posicao].append(titulo)

                            editoras[posicao].append("test")
                            autores[posicao].append("test")
                            anos[posicao].append(00)
                            generos[posicao].append("test")

                        else:
                            livros_por_usuario[posicao].append(titulo)

                            editoras[posicao].append(input(f"{gray}Digite a editora: {end}"))
                            autores[posicao].append(input(f"{gray}Digite o autor: {end}"))

                            while True:
                                ano = int(input(f"{gray}Digite o ano: {end}"))
                                if ano <= int(str(date.today())[0:4]):
                                    break
                                else:
                                    print(f"{red}Ano inválido{end}\n")
                                    continue

                            anos[posicao].append(ano)
                            generos[posicao].append(escolha_genero())

                    # ========================= BUSCAR LIVRO ============================= #

                    elif op == '2':

                        nome_consulta = input(
                            f"\n{gray}Digite o nome do livro para consulta: {end}")

                        for i in range(len(livros_por_usuario)):
                            livros_user = difflib.get_close_matches(nome_consulta, livros_por_usuario[i][1:],
                                                                    cutoff=0.4)

                            for j in range(len(livros_user)):
                                print(
                                    f"{livros_user[j]}, @{livros_por_usuario[i][0]}"
                                )

                    # ========================= EDITAR LIVRO ============================== #

                    elif op == '3':
                        nome_consulta = input(
                            f"{gray}Digite o nome do livro para editar: {end}")

                        livros_user = difflib.get_close_matches(nome_consulta, livros_por_usuario[posicao][1:],
                                                                cutoff=0.4)

                        if not livros_user:
                            print(f"{red}Livro não encontrado{end}\n")

                        posicao_edliv = livros_por_usuario[posicao].index(livros_user[listar_opcoes(livros_user)]) - 1

                        while True:
                            print(f"{bold}{blue}1{end} - Nome"
                                  f"\n{bold}{blue}2{end} - Editora"
                                  f"\n{bold}{blue}3{end} - Autor"
                                  f"\n{bold}{blue}4{end} - Ano"
                                  f"\n{bold}{blue}5{end} - Gênero"
                                  f"\n{bold}{blue}6{end} - Sair")

                            op_editar = input(
                                f"{gray}Escolha uma opção para editar ou '6' para sair:{end}")

                            if op_editar == '1':
                                livros_por_usuario[posicao][posicao_edliv + 1] = input(
                                    f"{gray}Digite um novo nome: {end}")

                            elif op_editar == '2':
                                editoras[posicao][posicao_edliv] = input(
                                    f"{gray}Digite a nova editora: {end}")

                            elif op_editar == '3':
                                autores[posicao][posicao_edliv] = input(
                                    f"{gray}Digite o novo autor: {end}")

                            elif op_editar == '4':
                                while True:
                                    ano = int(input(f"{gray}Digite o ano: {end}"))
                                    if ano <= int(str(date.today())[0:4]):
                                        break
                                    else:
                                        print(f"{red}Ano inválido{end}\n")
                                        continue
                                anos[posicao][posicao_edliv] = ano

                            elif op_editar == '5':
                                generos[posicao][posicao_edliv] = escolha_genero()

                            elif op_editar == '6':
                                print(f"{green}Alterações Salvas!{end}")
                                break

                    # ========================= DELETAR LIVRO ============================== #

                    elif op == '4':
                        if livros_por_usuario[posicao]:
                            print(f"\n{gray}Qual o livro que deseja deletar? {end}")
                            posicao_livros = listar_opcoes(livros_por_usuario[posicao][1:])

                            print(f"{gray}Tem certeza que deseja deletar esta informação? {end}")

                            op_cofirmacao = input(
                                f"{bold}{blue}S{end}{bold}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}").upper()

                            if op_cofirmacao.upper() == 'S':
                                livros_por_usuario[posicao].pop(posicao_livros + 1)
                                editoras[posicao].pop(posicao_livros)
                                autores[posicao].pop(posicao_livros)
                                anos[posicao].pop(posicao_livros)
                                generos[posicao].pop(posicao_livros)
                                print(f"\n{green}Livro excluído!{end}")
                            else:
                                print(f"\n{red}O livro não foi deletado.{end}")
                        else:
                            print(f"\n{red}Nenhum livro cadastrado.{end}")
                    # ========================= SAIR DO CRUD DE LIVROS ============================== #

                    elif op == '5':
                        break

            # ========================= PUBLICAR =========================================== #

            elif opcao == '5':
                post = input(f"Escreva: ")
                while True:

                    public = input(
                        f"Deseja publicar?"
                        f"{bold}{blue}S{end}{gray} - Sim / {bold}{blue}N{end}{gray} - Não: {end}"
                    ).upper()

                    if public == 'S':
                        posts.append(
                            f"{bold}{green}{usernames[posicao]}{end} {green}{semana[datetime.today().weekday()]},"
                            f" {datetime.today().hour}:{datetime.today().minute}{end}: {post}")
                        print(f"{green}Publicação realizada{end}")
                        break
                    elif public == 'N':
                        print(f"{red}Publicação deletada.{end}\n")
                        break
                    else:
                        print(f"{red}Opção inválida!{end}\n")
                        continue

            # ========================= SAIR DA CONTA LOGADA =============================== #

            elif opcao == '-1':
                logado = False
                print(f"{red}Conta desconectada{end}\n")
            else:
                print(f"{red}Opção inválida!{end}\n")

    else:
        print(f"{red}Código inválido{end}\n")

print(f"{red}Programa encerrado pelo usuário{end}")
