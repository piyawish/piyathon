# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Test configuration and shared fixtures for the Piyathon test suite.

This module provides common logging functionality and fixtures that can be used
across all test files in the project. It sets up a standardized logging
configuration that can be reused by different test modules.

Key Components:
    - Logging setup with customizable log levels
    - Session-scoped pytest fixture for accessing the logger
"""

import logging
import pytest
from tests.stats_collector import get_global_collector, reset_global_collector


def setup_logger(level=logging.INFO):
    """
    Configure and return a logger with the specified logging level.

    Args:
        level (int): The logging level to use (default: logging.INFO)
                    Can be logging.DEBUG, logging.INFO, logging.WARNING, etc.

    Returns:
        logging.Logger: A configured logger instance with console output handler
                       and formatted output.

    Example:
        >>> logger = setup_logger(logging.DEBUG)
        >>> logger.debug("Debug message")
        2024-01-26 12:34:56,789 - __main__ - DEBUG - Debug message
    """
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
    """
    Pytest fixture that provides a configured logger instance for the entire test session.

    This fixture is session-scoped, meaning the same logger instance is shared
    across all tests in the session. This prevents duplicate log handlers and
    ensures consistent logging behavior.

    Returns:
        logging.Logger: A configured logger instance set up by setup_logger()

    Example:
        def test_something(test_logger):
            test_logger.info("Starting test...")
    """
    return logger


@pytest.fixture(scope="session", autouse=True)
def setup_statistics_collection():
    """
    Session-wide fixture that manages statistics collection for the test session.
    
    This fixture automatically runs for the entire test session and:
    1. Resets the global statistics collector at the start
    2. Starts timing collection
    3. Stops timing and prints statistics summary at the end
    
    The autouse=True means this fixture runs automatically without being
    explicitly requested by test functions.
    """
    # Setup: Reset collector and start timing
    reset_global_collector()
    collector = get_global_collector()
    collector.start_collection()
    
    yield  # This is where all the tests run
    
    # Teardown: Stop timing and display statistics
    collector.stop_collection()
    print(collector.format_summary())


@pytest.fixture(scope="session")
def stats_collector():
    """
    Pytest fixture that provides access to the global statistics collector.
    
    This fixture can be used by tests that need direct access to the statistics
    collector, though most tests should rely on the automatic collection
    in test_cpython_files.py.
    
    Returns:
        StatisticsCollector: The global statistics collector instance
    
    Example:
        def test_something(stats_collector):
            stats_collector.record_file_success(100, 10)
    """
    return get_global_collector()
