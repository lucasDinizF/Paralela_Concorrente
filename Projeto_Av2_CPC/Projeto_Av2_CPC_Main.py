from Projeto_Av2_CPC_executores import Executores
import random, time


if __name__ == "__main__":
    # Gera as matrizes aqui (uma vez só para ambos os casos garantindo equidade).
    LA = random.randint(2500, 2500)
    CA = random.randint(2500, 2500)
    LB = CA
    CB = LA

    VA = [[random.randint(1, 9) for _ in range(CA)] for _ in range(LA)]
    VB = [[random.randint(1, 9) for _ in range(CB)] for _ in range(LB)]
    print(f"Matriz A ({LA}x{CA}):")
    for linha in VA:
        print(linha)

    print(f"\nMatriz B ({LB}x{CB}):")
    for linha in VB:
        print(linha)

    exe = Executores()


    print("===== Executando CONCORENTE =====\n")
    exe.executar_threadpool(LA, CA, VA, LB, CB, VB)   # roda primeiro e mede o tempo, CONCORENTE
    print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====\n")

    

    print("\n===== Executando PARALELO =====\n")
    exe.executar_processpool(LA, CA, VA, LB, CB, VB)  # roda depois e mede o tempo, PARALELO
    print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====\n")



    print("\n===== Executando SERIAL =====\n")
    exe.executar_serial(LA, CA, VA, LB, CB, VB)  # roda depois e mede o tempo, SERIAL
    print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== =====\n")


    print(f"\nTempo de execução com CONCORENTE: {exe.tempo_concorente:.4f} segundos\n")
    print(f"\nTempo de execução com PARALELO: {exe.tempo_paralelo:.4f} segundos\n")
    print(f"\nTempo de execução com SERIAL: {exe.tempo_serial:.4f} segundos\n")

    