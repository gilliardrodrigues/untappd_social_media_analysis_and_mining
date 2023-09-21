import logging
import time
from timeit import default_timer as timer
from datetime import datetime

"""
Utils
Funções úteis
getlogger: retorna um objeto do tipo logger
format_time: retorna o tempo formatado de acordo com o necessário
"""

__all__ = [
    'get_logger',
    'format_time',
    'Clock'
]


def get_logger(logger: logging.Logger, level: int = 10) -> logging.Logger:
    """
    Retorna um objeto do tipo logger
    Parâmetros
    ----------
    logger: logging.Logger
        Objeto do tipo logger
    level: int
        Nível do log. Default: 10 - DEBUG
    Retorno
    -------
    logging.Logger
        Objeto logger configurado
    """
    today = datetime.today()
    filename = f'experimento_{today.day}_{today.month}_{today.year}.log'

    logger.setLevel(level)

    _format = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(_format)

    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.FileHandler(filename=filename, mode='a', encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def format_time(elapsed_time: float) -> str:
    """
    Formata o tempo de acordo com a quantidade e retorna.
    Parâmetros
    ----------
    elapsed_time
        Tempo como float.
    Retorno
    -------
    str
        Tempo formatado.
    """
    if elapsed_time >= 86400:
        return time.strftime("%dd%Hh%Mm%Ss", time.gmtime(elapsed_time))
    elif elapsed_time >= 3600:
        return time.strftime("%Hh%Mm%Ss", time.gmtime(elapsed_time))
    elif elapsed_time >= 60:
        return time.strftime("%Mm%Ss", time.gmtime(elapsed_time))
    else:
        return time.strftime("%Ss", time.gmtime(elapsed_time))


logger_ = logging.getLogger(__name__)
logger_ = get_logger(logger=logger_)


class Clock:
    def __init__(self, process_label: str = 'default'):
        """
        Classe para calcular o tempo que uma tarefa leva para ser executada.

        Parâmetros
        ----------
        process_label : str, optional
            Processo que terá o tempo medido, por padrão 'default'.
        """
        self.start = timer()
        self.end = None
        self.elapsed_time = None
        self.label = process_label

    def stop_watch(self) -> None:
        """
        Calcula o tempo e registra a diferença de tempo para executar a tarefa rotulada.
        """
        self.end = timer()
        elapsed_time = self.end - self.start

        logger_.info(f"{self.label} levou {format_time(elapsed_time)} para ser executado.")

