from loguru import logger
from functools import wraps
import time

def time_measure_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"Função {func.__name__} executada em {end_time - start_time} segundos")
        return result
    return wrapper

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Função {func.__name__} com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função {func.__name__} retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Erro capturado em {func.__name__}: {e}")
            return f"Erro: {e}"
    return wrapper

