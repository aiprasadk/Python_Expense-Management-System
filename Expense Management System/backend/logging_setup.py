import logging

def setup_logger(name, log_file='server.log', level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding handlers if they already exist
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, mode="a")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional: Add a StreamHandler to print logs to the console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger