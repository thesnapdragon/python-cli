#!/usr/bin/env python

import argparse
from dotenv import load_dotenv, find_dotenv
import logging
import logging.handlers
from pythonjsonlogger import jsonlogger


def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    log_handler = logging.handlers.RotatingFileHandler('log/app.log', maxBytes=2000, backupCount=100)
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s')
    log_handler.setFormatter(formatter)
    log_handler.setLevel(logging.DEBUG)
    root.addHandler(log_handler)


def main():
    parse_args()
    setup_logging()

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    main()
