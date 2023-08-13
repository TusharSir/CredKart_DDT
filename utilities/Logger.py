import logging
import inspect


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(
            "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#14 & 15\\CredKart_Pytest_Project\\Logs\\CredKart.log")
        log_format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s ")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# Debug
# Info
# Warning
# Error
# Critical
