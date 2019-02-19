from random import randint

campo1 = []
campo2 = []

p1 = ""
p2 = ""

tab_p1 = []
tab_p2 = []

contador_s_p1 = 0
contador_c_p1 = 0
contador_p_p1 = 0

contador_s_p2 = 0
contador_c_p2 = 0
contador_p_p2 = 0

numero_frotas = 3

# Menu de Opções
def menu():
    print("Olá, seja bem vindo ao Batalha Naval!\n")
    print(".:: MENU DE OPÇÕES ::. \n\n(1) Jogar\n(2) Créditos\n")   
   
# Gerando a Matriz
def gerar_matriz(c):
    for i in range(0,10):
        c.append(['']*10)
           
# Imprimindo o Tabuleiro
def tabuleiro(c):
    # Quando x = 0, campo em estado inicial
    # Quando x = *, campo foi acertado
    x = 0
    print("    | A | B | C | D | E | F | G | H | I | J |")
    for i in c:
        print("-"*45)
        x += 1
        if x != 11:
            print(" {:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|{:^3}|".format(x,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
    print("-"*45)

# Inserindo a Frota no Tabuleiro
def inserir(c,jogador):
    print("=-="*20)  
    print(f"Olá {jogador}, escolha sua frota:\n- Porta Avião(p)\n- Cruzador(c)\n- Submarino(s)")
    frota = input("Frota: ").upper()
    linha = int(randint(0,9))    
    coluna = int(randint(0,9))
    
#terá que ser criada uma repetição aqui    
    if frota == "S":             
        c[linha][coluna] = frota
    if frota == "P":
        c[linha][coluna] = frota
    if frota == "C":
        c[linha][coluna] = frota

def exibe_pontuacao():
    #jogador 1
    print("=-="*20) 
    print(f" Estatísticas { p1 }\n- Porta aviões acertados: { contador_p_p1 }\n- Cruzadores acertados: { contador_c_p1 }\n- Submarinos acertados: { contador_s_p1 }")
    
    #jogador 2
    print("=-="*20) 
    print(f" Estatísticas { p2 }\n- Porta aviões acertados: { contador_p_p2 }\n- Cruzadores acertados: { contador_c_p2 }\n- Submarinos acertados: { contador_s_p2 }")
    

# Coordenadas de Ataque 
def coord_atk(cam,jogador,tab):
    # definindo variáveis globais
    global contador_s_p1
    global contador_c_p1
    global contador_p_p1

    global contador_s_p2
    global contador_c_p2
    global contador_p_p2
    
    print("=-="*19)
    print(f"Sua vez {jogador}, informe as Coordenadas do Ataque!")

    lin = int(input("Linha 1-10: "))
    col = str(input("Coluna A-J: ").upper())

    #Coluna
    if col == 'A':
        col = 0
    if col == 'B':
        col = 1
    if col == 'C':
        col = 2
    if col == 'D':
        col = 3
    if col == 'E':
        col = 4
    if col == 'F':
        col = 5
    if col == 'G':
        col = 6
    if col == 'H':
        col = 7
    if col == 'I':
        col = 8
    if col == 'J':
        col = 9

    #Linha
    if lin == 1:
        lin = 0
    if lin == 2:
        lin = 1
    if lin == 3:
        lin = 2
    if lin == 4:
        lin = 3
    if lin == 5:
        lin = 4
    if lin == 6:
        lin = 5
    if lin == 7:
        lin = 6
    if lin == 8:
        lin = 7
    if lin == 9:
        lin = 8
    if lin == 10:
        lin = 9

    if (cam[lin][col] == "") or (cam[lin][col] == "*"):
        #tab[lin].insert(col,hitF)
        cam[lin][col] = "*"   
        tab[lin][col] = "*"
        exibe_pontuacao()    

        return False
    else:
        # conta acerto de submarino
        if cam[lin][col] == "P":
            # altera na matriz de exibição
            tab[lin][col] == "P" 
            # adiciona ao contador do player que acertou
            if jogador == p1:
                contador_p_p1 += 1
            elif jogador == p2:
                contador_p_p2 += 1
        elif cam[lin][col] == "C":
            tab[lin][col] == "C" 
            # adiciona ao contador do player que acertou
            if jogador == p1:
                contador_c_p1 += 1
            elif jogador == p2:
                contador_c_p2 += 1
        elif cam[lin][col] == "S":
            tab[lin][col] == "S" 
            # adiciona ao contador do player que acertou
            if jogador == p1:
                contador_s_p1 += 1
            elif jogador == p2:
                contador_s_p2 += 1

        # transforma campo indisponivel na matriz de controle
        cam[lin][col] = "*"
        exibe_pontuacao()
        return True 

def qtde_frotas_p1():
    return (contador_c_p1 + contador_p_p1 + contador_s_p1)

def qtde_frotas_p2():
    return (contador_c_p2 + contador_p_p2 + contador_s_p2)
        
# Função de Manipulação Principal
def main():       
    menu()
    print("=-="*20) 
    opcao = int(input("Escolha uma Opção: "))
    #Opção Jogar
    if opcao == 1:
        global p1
        global p2

        print("=-="*20)
        p1 = input("Jogador 1 informe seu Nome: ").capitalize()
        p2 = input("Jogador 2 informe seu Nome: ").capitalize()

        #Jogador 1 Setup
        gerar_matriz(campo1)
        gerar_matriz(tab_p1)
        for i in range(3):
            inserir(campo1,p1)

        #Jogador 2 Setup
        gerar_matriz(campo2)
        gerar_matriz(tab_p2)
        for i in range(3):
            inserir(campo2,p2)

        #Modo de Testes
        print("=-="*20)
        debug = input("Deseja ativar o Modo Testes? (s/n): ").upper()
        if debug == "S":
            print("\n       ..:: MODO DE TESTES ATIVADO ::..\n")
            debug = True
        else:
            print("\n            ..:: VAMOS COMEÇAR ::..\n") 
            debug = False
               
        while True:
            x = 0
            y = 0
            ganhou = 0

            #Jogador 1 Loop                       
            while x == 0 and ganhou == 0:                       
                if debug == True:                    
                    tabuleiro(campo2)
                    res = coord_atk(campo2,p1,campo2)
                else:
                    tabuleiro(tab_p2)
                    res = coord_atk(campo2,p1,tab_p2)
                                 
                if res == False:                    
                    x = 1
                    print("=-="*19)
                    print(f" Você errou {p1}, o seu tiro atingiu a Água :( ")
                    print("=-="*19)
                else:
                    print("=-="*19)
                    print(f" Fogo! Bela jogada {p1} você acertou e continua jogando! ")
                    print("=-="*19)

                if qtde_frotas_p1() == numero_frotas:
                    ganhou = 1
                    
            #Jogador 2 Loop
            while y == 0 and ganhou == 0:
                if debug == True:                    
                    tabuleiro(campo1)
                    res = coord_atk(campo1,p2,campo1)
                else:
                    tabuleiro(tab_p1)
                    res = coord_atk(campo1,p2,tab_p1)
                                 
                if res == False:                    
                    y = 1
                    print("=-="*19)
                    print(f" Você errou {p2}, o seu tiro atingiu a Água :( ")
                    print("=-="*19)
                else:
                    print("=-="*19)
                    print(f" Fogo! Bela jogada {p2} você acertou e continua jogando! ")
                    print("=-="*19)

                if qtde_frotas_p1() == numero_frotas:
                    ganhou = 1

            if qtde_frotas_p1() == numero_frotas:
                print(f"Parabéns { p1 }, você venceu!")
                break
            elif qtde_frotas_p2() == numero_frotas:
                print(f"Parabéns { p2 }, você venceu!")
                break
    
    #Opção Créditos
    if opcao == 2:
        print("\nEste jogo foi Desenvolvido por: \n- Lucas Olegário\n- Messias Souza\n- Andréia Berto \n")
        
    
main()