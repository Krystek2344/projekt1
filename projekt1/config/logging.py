import logging
from logging import Logger, Formatter, StreamHandler, Handler, getLogger, DEBUG
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys


class LoggerConfig:

    @staticmethod
    def get_console_logger(
            name: str,
            level: int = DEBUG,
            formatter: Formatter | None = None) -> Logger:
        if not formatter:
            formatter = LoggerConfig._get_formatter()
        stream_handler = LoggerConfig._get_stream_handler(formatter)
        return LoggerConfig._get_logger(name, level, [stream_handler])

    @staticmethod
    def get_file_logger(
            name: str,
            level: int = DEBUG,
            filename: str = 'app.log',
            formatter: Formatter | None = None) -> Logger:
        if not formatter:
            formatter = LoggerConfig._get_formatter()
        file_handler = LoggerConfig._get_file_handler(formatter, filename)
        return LoggerConfig._get_logger(name, level, [file_handler])

    @staticmethod
    def get_console_and_file_logger(
            name: str,
            level: int = DEBUG,
            filename: str = 'app.log',
            formatter: Formatter | None = None) -> Logger:
        if not formatter:
            formatter = LoggerConfig._get_formatter()
        stream_handler = LoggerConfig._get_stream_handler(formatter)
        file_handler = LoggerConfig._get_file_handler(formatter, filename)
        return LoggerConfig._get_logger(name, level, [stream_handler, file_handler])

    @staticmethod
    def set_level(level: int = DEBUG):
        all_loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
        for logger in all_loggers:
            logger.setLevel(level)

    @staticmethod
    def _get_formatter() -> Formatter:
        return Formatter(
            fmt='%(asctime)-10s [%(levelname)-8s] %(filename)s:%(lineno)-4s%(funcName)20s: %(message)-20s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    @staticmethod
    def _get_stream_handler(formatter: Formatter) -> StreamHandler:
        stream_handler = StreamHandler(stream=sys.stdout)
        stream_handler.setFormatter(formatter)
        return stream_handler

    @staticmethod
    def _get_file_handler(formatter: Formatter, filename: str = 'app.log') -> RotatingFileHandler:
        path = f'{sys.path[1]}/logs'
        Path(path).mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(
            f'{path}/{filename}',
            mode='a',
            maxBytes=5 * 1024 * 1024,
            backupCount=2,
            encoding='utf-8',
            delay=True
        )
        file_handler.setFormatter(formatter)
        return file_handler

    @staticmethod
    def _get_logger(name: str, level: int, handlers: list[Handler]) -> Logger:
        logger = getLogger(name)
        logger.setLevel(level)

        for handler in handlers:
            logger.addHandler(handler)

        return logger
