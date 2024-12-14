from uso_log import log_decorator, time_measure_decorator
import time

@log_decorator
#@time_measure_decorator
def soma(x: float, y: float) -> float:
    time.sleep(2)
    return x + y

# Chamando a função com diferentes entradas
print(soma(3, 5))          # Funciona normalmente
print(soma(3, "5"))        # Gera um erro e loga a exceção