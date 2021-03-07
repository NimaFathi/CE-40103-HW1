from decouple import config


def set_logger(logging, name):
    logging.basicConfig(
        format='%(levelname)s %(asctime)s %(message)s',
        level=logging.INFO,
        filename=config('LOG_PATH', default='log.log')
    )
    logger = logging.getLogger(name)
    return logger
