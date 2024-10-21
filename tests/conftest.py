# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import logging
import pytest


def setup_logger(level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    # Create console handler and set level to the specified level
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    return logger


# Create a logger instance with INFO level by default
logger = setup_logger()


@pytest.fixture(scope="session")
def test_logger():
    return logger
