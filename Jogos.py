"""Categoriza jogos."""


class Jogos:
    """Cria a classe principal que é a base."""

    def __init__(self, nome, ano, categoria, valor, plataformas, interatividade):
        self.nome = nome
        self.ano = ano
        self.categoria = categoria
        self.valor = valor
        self.plataformas = plataformas
        self.interatividade = interatividade  # player vs player, cooperativo, equipa
        print(
            f"Jogo criado com sucesso. Classe de origem: {type(self).__name__}")

    def __str__(self):
        atributos = (vars(self))
        string = ""
        for atributo, info in atributos.items():
            if info:
                string += f"\n{atributo.capitalize()}: {info}"
        return string + "\n"


class Online(Jogos):
    def __init__(self, conexao, **kwargs):
        super().__init__(**kwargs)
        self.conexao = conexao  # LAN, Internet

    def dica(self):
        print(f'''
        Vai começar o jogo {self.nome} do tipo {self.interatividade}
        no modo Online.
        (evite conexões lentas para ter uma melhor experiência durante
        a partida, sempre ajude os membros da equipa quando possível).

        ''')


class Offline(Jogos):
    def __init__(self, duracao, **kwargs):
        super().__init__(**kwargs)
        self.duracao = duracao  # horas para concluir toda a história
        # e narrativa

    def dica(self):
        print(f'''
        Vai começar o jogo {self.nome} do tipo {self.interatividade}
        no modo Offline.
        (não esqueça de guardar o progresso antes de sair do jogo).

        ''')


class Singleplayer(Offline, Online):
    def __init__(self, nome=None, ano=None, categoria=None, valor=None,
                 plataformas=None, interatividade=None,
                 duracao=None, conexao=None):
        super().__init__(nome=nome, ano=ano, categoria=categoria, valor=valor,
                         plataformas=plataformas,
                         interatividade=interatividade, duracao=duracao,
                         conexao=conexao)


class Multiplayer(Online, Offline):
    def __init__(self, nome=None, ano=None, categoria=None, valor=None,
                 plataformas=None, interatividade=None,
                 duracao=None, conexao=None):
        super().__init__(nome=nome, ano=ano, categoria=categoria, valor=valor,
                         plataformas=plataformas,
                         interatividade=interatividade, duracao=duracao,
                         conexao=conexao)


jogo1 = Singleplayer(nome="God of War", ano=2022, categoria="Ação, Aventura",
                     valor="250 €",
                     plataformas="PC, Playstation",
                     interatividade="Player vs Computer", duracao=85)
print(jogo1)
jogo1.dica()
jogo2 = Multiplayer(nome="League of Legends", ano=2022,
                    categoria="MOBA, Estratégia", valor="0 €",
                    plataformas="PC, Android",
                    interatividade="Equipa vs Equipa", conexao="Internet")
print(jogo2)
jogo2.dica()
