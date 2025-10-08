import random
from threading import Lock

print_lock = Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

        

def questão_um(y, z, V):
    out = []
    out.append('-'*20 + ' Questão 01 ' + '-'*20)
    out.append("➡ Multiplicar todos os elementos da matriz por um número aleatório.")
    X = random.randint(1, 9)
    out.append(f'Número aleatório escolhido: {X}')
    for i in range(y):
        linha = []
        for j in range(z):
            linha.append(str(V[i][j] * X))
        out.append(" ".join(linha))
    out.append("")  
    return "\n".join(out)


# -------------------------------
# Questão 02
# -------------------------------
def questão_dois(nome, v):
    x = len(v)       # número de linhas
    y = len(v[0])    # número de colunas
    VT = [[v[j][i] for j in range(x)] for i in range(y)]
    
    out = [f"\n-------------------- Questão 02 ({nome}) --------------------"]
    out.append("➡ Transposta da matriz.")
    for linha in VT:
        out.append(" ".join(str(x) for x in linha))
    return "\n".join(out)


# -------------------------------
# Questão 03
# -------------------------------
def questão_tres(nome, x, y, v):
    out = []
    out.append('-'*20 + f' Questão 03 ({nome}) ' + '-'*20)
    out.append("➡ Calcular a soma de todos os elementos da matriz.\n")
    soma = sum(sum(linha) for linha in v)
    out.append(f"Soma total dos elementos: {soma}")
    out.append("")
    return "\n".join(out)


# -------------------------------
# Questão 04
# -------------------------------
def questão_quatro(nome, x, y, v):
    out = []
    out.append('-'*20 + f' Questão 04 ({nome}) ' + '-'*20)
    out.append("➡ Calcular o maior e o menor valor da matriz.\n")
    maior = max(max(linha) for linha in v)
    menor = min(min(linha) for linha in v)
    out.append(f"Maior valor encontrado: {maior}")
    out.append(f"Menor valor encontrado: {menor}")
    out.append("")
    return "\n".join(out)


# -------------------------------
# Questão 05
# -------------------------------
def questão_cinco(nome, x, y, v):
    out = []
    out.append('-'*20 + f' Questão 05 ({nome}) ' + '-'*20)
    out.append("➡ Separar elementos pares e ímpares da matriz.\n")
    pares = [str(el) for linha in v for el in linha if el % 2 == 0]
    impares = [str(el) for linha in v for el in linha if el % 2 != 0]
    out.append("Pares: " + " ".join(pares) if pares else "Pares: Nenhum")
    out.append("Ímpares: " + " ".join(impares) if impares else "Ímpares: Nenhum")
    out.append("")
    return "\n".join(out)    

# -------------------------------
# Questão 06
# -------------------------------
def questão_seis(A, nome='A'):
    out = []
    LA = len(A)
    CA = len(A[0])
    out.append('-'*20 + f' Questão 06 ({nome}) ' + '-'*20)
    out.append("➡ Calcular médias da matriz A (linha, coluna ou geral).\n")

    if LA == 1:  # só uma linha
        media = sum(A[0])/CA
        out.append(f"Média da linha: {media:.1f}")
    elif CA == 1:  # só uma coluna
        media = sum([A[i][0] for i in range(LA)])/LA
        out.append(f"Média da coluna: {media:.1f}")
    else:  # matriz normal
        med_lin = [sum(A[i])/CA for i in range(LA)]
        med_col = [sum([A[i][j] for i in range(LA)])/LA for j in range(CA)]
        out.append("Médias por linha:")
        out.append(" ".join(f"{m:.1f}" for m in med_lin))
        out.append("Médias por coluna:")
        out.append(" ".join(f"{m:.1f}" for m in med_col))

    out.append("")
    return "\n".join(out)


# -------------------------------
# Questão 07
# -------------------------------
def questão_sete(B, nome='B'):
    out = []
    LB = len(B)
    CB = len(B[0])
    out.append('-'*20 + f' Questão 07 ({nome}) ' + '-'*20)
    out.append("➡ Se B não for quadrada: imprimir transposta de B multiplicada por 2.5.\n➡ Se B for quadrada ou vetor: contar números primos.\n")

    if LB != CB and LB > 1 and CB > 1:  # B não quadrada
        VT = [[B[j][i] for j in range(LB)] for i in range(CB)]
        for linha in VT:
            out.append(" ".join(str(el*2.5) for el in linha))
    else:  # B quadrada ou vetor
        def is_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True

        np2 = sum(1 for linha in B for el in linha if is_primo(el))
        out.append(f"Quantidade de números primos em B: {np2}")

    out.append("")
    return "\n".join(out)

# ------------------------
# PROGRAMA PRINCIPAL
# ------------------------

# Gera matrizes automaticament



# ------------------------
# Funções de execução
# ------------------------
def run_questao1(LA, CA, VA, LB, CB, VB):
    #safe_print(questão_um(LA, CA, VA))
    #safe_print(questão_um(LB, CB, VB))
    questão1 = questão_um(LA, CA, VA) + "\n" + questão_um(LB, CB, VB)
    safe_print(questão1)


def run_questao2(VA, VB):
    questão2 = questão_dois('A', VA) + "\n" + questão_dois('B', VB)
    safe_print(questão2)


def run_questao3(CA, LA, VA, CB, LB, VB):
    #safe_print(questão_tres('A', LA, CA, VA))
    #safe_print(questão_tres('B', LB, CB, VB))
    questão3 = questão_tres('A', LA, CA, VA) + "\n" + questão_tres('B', LB, CB, VB)
    safe_print(questão3)

def run_questao4(CA, LA, VA, CB, LB, VB):
    #safe_print(questão_quatro('A', LA, CA, VA))
    #safe_print(questão_quatro('B', LB, CB, VB))
    questão4 = questão_quatro('A', LA, CA, VA) + "\n" + questão_quatro('B', LB, CB, VB)
    safe_print(questão4)

def run_questao5(CA, LA, VA, CB, LB, VB):
    #safe_print(questão_cinco('A', LA, CA, VA))
    #safe_print(questão_cinco('B', LB, CB, VB))
    questão5 = questão_cinco('A', LA, CA, VA) + "\n" + questão_cinco('B', LB, CB, VB)
    safe_print(questão5)

def run_questao6(VA):
    safe_print(questão_seis(VA, nome='A'))

def run_questao7(VB):
    safe_print(questão_sete(VB, nome='B'))