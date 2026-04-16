import logging
import os
from datetime import datetime

def setup_logger(name: str = "api_tests", log_level=logging.INFO):
    
    # Создаём папку logs, если её нет
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Имя файла лога с текущей датой/временем
    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    # Создаём логгер
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Формат сообщений
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Обработчик для файла
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Обработчик для консоли
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()