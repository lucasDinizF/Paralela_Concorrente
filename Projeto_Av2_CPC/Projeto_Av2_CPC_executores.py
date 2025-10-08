from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
from Projeto_Av2_CPC_funcoes import *

class Executores:
    # Variáveis para armazenar os tempos
    def __init__(self):
        self.tempo_concorente = 0
        self.tempo_paralelo = 0
        self.tempo_serial = 0

    def executar_threadpool(self, LA, CA, VA, LB, CB, VB):
        inicio = time.perf_counter()
        
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(run_questao1, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao2, VA, VB),
                executor.submit(run_questao3, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao4, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao5, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao6, VA),
                executor.submit(run_questao7, VB),
            ]
            for f in futures: f.result()
        fim = time.perf_counter()
        self.tempo_concorente= fim - inicio
        

    def executar_processpool(self, LA, CA, VA, LB, CB, VB):
        inicio = time.perf_counter()
    
        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(run_questao1, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao2, VA, VB),
                executor.submit(run_questao3, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao4, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao5, LA, CA, VA, LB, CB, VB),
                executor.submit(run_questao6, VA),
                executor.submit(run_questao7, VB),
            ]
            for f in futures: f.result()
        fim = time.perf_counter()
        self.tempo_paralelo=fim - inicio
        
        
    def executar_serial(self, LA, CA, VA, LB, CB, VB):
        inicio = time.perf_counter()
        run_questao1(LA, CA, VA, LB, CB, VB)
        run_questao2(VA, VB)
        run_questao3(LA, CA, VA, LB, CB, VB)
        run_questao4(LA, CA, VA, LB, CB, VB)
        run_questao5(LA, CA, VA, LB, CB, VB)
        run_questao6(VA)
        run_questao7(VB)
        fim = time.perf_counter()
        self.tempo_serial = fim - inicio
        