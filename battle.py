from random import randint
#Matriz dos repectivos jogadores
campo1 = []
campo2 = []
#Nome dos usuarios
p1 = ""
p2 = ""
#Mariz de exibição
tab_p1 = []
tab_p2 = []
#contador de acertos do jogador1
contador_s_p1 = 0
contador_c_p1 = 0
contador_p_p1 = 0
#contador de acertos do jogador2
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
        c.append([' ']*10)
           
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

#Função do Submarino
def submarino(c):
  lin = randint(0,10)
  col = randint(0,10)
  vert = randint(0,1)

  try:
    #Verifica se posição é Vertical
    if vert == 1:
      #Verifica se posição Vertical está Vazia
      if c[lin][col] == " " and c[lin][col+1] == " ":
          for i in range(lin,lin+1):
            for j in range(col,col+2):
              c[i][j] = 'S'
    
    #Se posição é Horizontal
    else:
      #Verifica se posição Horizontal está vazia
      if c[lin][col] == " " and c[lin+1][col] == " ":
          for i in range(lin,lin+2):
            for j in range(col,col+1):
              c[i][j] = 'S'
  except:
    submarino(c)

  return c
  
#Função do Cruzador
def cruzador(c):
  lin = randint(0,10)
  col = randint(0,10)
  vert = randint(0,1)

  try:
    #Verifica se posição é Vertical
    if vert == 1:
      if c[lin][col] == " " and c[lin][col+1] == " " and c[lin][col+2] == " ":
        for i in range(lin,lin+1):
          for j in range(col,col+3):
            c[i][j] = 'C'
    #Se posição é Horizontal
    else:
      #Verifica se posição Horizontal está vazia
      if c[lin][col] == " " and c[lin+1][col] == " " and c[lin+2][col] == " ":
        for i in range(lin,lin+3):
          for j in range(col,col+1):
            c[i][j] = 'C'
  except:
    cruzador(c)

  return c

#Função do Porta Avião
def porta_aviao(c):
  lin = randint(0,10)
  col = randint(0,10)
  vert = randint(0,1)

  try:
    #Verifica se posição é Vertical
    if vert == 1:
      if c[lin][col] == " " and c[lin][col+1] == " " and c[lin][col+2] == " "  and c[lin][col+3] == " ":
        for i in range(lin,lin+1):
          for j in range(col,col+4):
            c[i][j] = 'P'
    #Se posição é Horizontal
    else:
      #Verifica se posição Horizontal está vazia
      if c[lin][col] == " " and c[lin+1][col] == " " and c[lin+2][col] == " " and c[lin+3][col] == " ":
        for i in range(lin,lin+4):
          for j in range(col,col+1):
            c[i][j] = 'P'
  except:
    porta_aviao(c) 

  return c
  
# Inserindo a Frota no Tabuleiro
def inserir(c,jogador,op):
    print("=-="*20)   

    if op == "S":

      porta_aviao(c)
      
      for i in range(2): 
        cruzador(c)

      for i in range(3): 
        submarino(c)
         
    else:
      print(f" {jogador}, Escolha sua frota: \n")
      print(" (1) Porta Avião min 0 - 1 max\n (2) Cruzador min 0 - 2 max\n (3) Submarino min 1 - 3 max\n")
      print("Digite 0 para Finalizar a Escolha de Frotas")

      qtd_frota = 0
      qtd_p = 0
      qtd_c = 0
      qtd_s = 0
      
      #Usuario escolhe sua frota personalizada
      while qtd_frota < 6:
        print("=-="*20) 
        opt = int(input("Escolha uma Opção: "))
        if opt == 0:
            break        
        if opt == 1 and qtd_p < 1:
            if qtd_p == 0:  
                porta_aviao(c)
                qtd_p += 1
            else:
                print("=-="*20) 
                print("!!! Você adicinou a quantidade Máxima de Porta Aviões !!!")             
        if opt == 2 and qtd_c < 2:
            if qtd_c <2:  
                cruzador(c)
                qtd_c +=1
            else:
                print("=-="*20) 
                print("!!! Você adicionou a quantidade Máxima de Cruzadores !!!")                
        if opt == 3 and qtd_s < 3:
            if qtd_s < 3:  
                submarino(c)
                qtd_s +=1
            else:
                print("=-="*20) 
                print("!!! Você adicinou a quantidade Máxima de  Submarinos !!!")                
        print("=-="*20)  
        print(f" Frotas Adicionadas\n- Porta Avião {qtd_p}\n- Cruzador {qtd_c}\n- Submarino {qtd_s}")
        qtd_frota = (qtd_p + qtd_c + qtd_s)
        
          
#Exibir pontuação
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
    print(f"Sua vez {jogador}, Informe as Coordenadas do Ataque!")

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

    if (cam[lin][col] == " ") or (cam[lin][col] == "*"):
        #tab[lin].insert(col,hitF)
        cam[lin][col] = "*"   
        tab[lin][col] = "*"
        exibe_pontuacao()  
        return False
    else:
        # conta acerto de submarino
        if cam[lin][col] == "P":
            # altera na matriz de exibição
            tab[lin][col] = "P" 
            # adiciona ao contador do player que acertou
            if jogador == p1:
                contador_p_p1 += 1
            elif jogador == p2:
                contador_p_p2 += 1
        elif cam[lin][col] == "C":
            tab[lin][col] = "C" 
            # adiciona ao contador do player que acertou
      
            if jogador == p1:
                contador_c_p1 += 1
            elif jogador == p2:
                contador_c_p2 += 1
        elif cam[lin][col] == "S":
            tab[lin][col] = "S" 
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
      
        print("=-="*20)
        op = input("Deseja jogar com a Frota Máxima? (s/n): ").upper()

        #Jogador 1 Setup
        gerar_matriz(campo1)
        gerar_matriz(tab_p1)        
        inserir(campo1,p1,op)

        #Jogador 2 Setup
        gerar_matriz(campo2)
        gerar_matriz(tab_p2)        
        inserir(campo2,p2,op)


        qtd_s_p1 = 0
        qtd_c_p1 = 0
        qtd_p_p1 = 0
        qtd_s_p2 = 0
        qtd_c_p2 = 0
        qtd_p_p2 = 0


        for linha in campo1:
            for coluna in linha:
                if "S" in coluna:
                    qtd_s_p1 += 1
                if "C" in coluna:
                    qtd_c_p1 += 1
                if "P" in coluna:
                    qtd_p_p1 += 1
        
        for linha in campo2:
            for coluna in linha:
                if "S" in coluna:
                    qtd_s_p2 += 1
                if "C" in coluna:
                    qtd_c_p2 += 1
                if "P" in coluna:
                    qtd_p_p2 += 1

        #Soma o número de frotas contidos na Matriz do Jogador 1
        soma_p1 = (qtd_c_p1 + qtd_s_p1 + qtd_p_p1)

        #Soma o número de frotas contidos na Matriz do Jogador 2
        soma_p2 = (qtd_c_p2 + qtd_s_p2 + qtd_p_p2)         

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

                if qtde_frotas_p1() == soma_p2:
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

                if qtde_frotas_p1() == soma_p2:
                    ganhou = 1

            if qtde_frotas_p1() == soma_p2:
                print(f"Parabéns { p1 }, você venceu!")
                break
            elif qtde_frotas_p2() == soma_p1:
                print(f"Parabéns { p2 }, você venceu!")
                break
    
    #Opção Créditos
    if opcao == 2:
        print("\nEste jogo foi Desenvolvido por: \n- Lucas Olegário\n- Messias Souza\n- Andréia Berto \n")
        return main()
        
    
main()