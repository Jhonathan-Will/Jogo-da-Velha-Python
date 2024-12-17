import random

def verificar(matrix):
    for i in range(len(matrix)):
        valor = 0
        casaAtual = matrix[i][0]
        for o in range(len(matrix[i])):
            if matrix[i][o] == casaAtual:
                valor+=1
        if valor == 3:
            print("Computador Ganhou!!" if(matrix[i][0] == "O") else "Você ganhou!!!")
            return True

    for i in range(len(matrix)):
        valor = 0
        casaAtual = matrix[0][i]
        for o in range(len(matrix[i])):
            if matrix[o][i] == casaAtual:
                valor += 1
        if valor == 3:
          print("Computador Ganhou!!" if(matrix[0][i] == "O") else "Você ganhou!!!")
          return True  
    
    if (matrix[0][0] == matrix[1][1] == matrix[2][2]) | (matrix[0][2] == matrix[1][1] == matrix[2][0]):
        print("Computador Ganhou!!" if(matrix[1][1] == "O") else "Você ganhou!!!")
        return True  

    return False

def computador(matrix):
    while True:
        valor = random.randint(1, 9)

        for i in range(len(matrix)):
            for o in range(len(matrix[i])):
                if str(matrix[i][o]) == str(valor):
                    matrix[i][o] = "O"
                    mostrarJogo(matrix=matrix)
                    resultadoComputador = verificar(matrix=matrix)

                    if resultadoComputador:
                        return True
                    else:
                        return False

def jogar(valor, matrix):
    if(int(valor) > 9 | int(valor) < 1):
        print("Opção invalida")
        return False
    
    for i in range(len(matrix)):
        for o in range(len(matrix[i])):
            if str(matrix[i][o]) == str(valor):
                matrix[i][o] = "X"
    mostrarJogo(matrix=matrix)
    resultado = verificar(matrix=matrix)
    if resultado:
        return resultado
    else:
        return computador(matrix=matrix)

    

def mostrarJogo(matrix):
    for i in range(len(matrix)):
        print(40*"-")
        for o in range(len(matrix[i])):
            print(matrix[i][o], " | ", end=" " if o != (len(matrix[i]) -1) else "\n")
    print(40*"-")

matrix = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]

resultado = False

print("========================", "========================", sep="JOGO DA VELHA")
mostrarJogo(matrix= matrix)

while resultado == False:
    

    opcao = input("Selecione um numero para jogar: ")
    resultado = jogar(valor = opcao, matrix = matrix)
    if resultado != False:
        break


