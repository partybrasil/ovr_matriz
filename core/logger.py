# Advanced, secure, colored logger setup

import logging
import logging.handlers

def setup_logger(name="ovr_matriz", level=logging.INFO, log_file=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s", "%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        if log_file:
            file_handler = logging.handlers.RotatingFileHandler(
                log_file, maxBytes=5*1024*1024, backupCount=3, encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    logger.setLevel(level)
    return logger

logger = setup_logger()
