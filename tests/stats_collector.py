# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Test Statistics Collection Module

This module provides functionality to collect and aggregate statistics during
Piyathon translation testing, including file counts, token counts, and NAME token
analysis for comprehensive test reporting.

Key Components:
    - TestStatistics: Data class for storing test statistics
    - StatisticsCollector: Main class for collecting and aggregating statistics
    - Formatting utilities for displaying statistics reports

Dependencies:
    - time: For measuring processing duration
    - dataclasses: For structured statistics storage
    - typing: For type hints
"""

import time
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TestStatistics:
    """
    Data structure for storing comprehensive test statistics.

    Attributes:
        files_tested (int): Number of files successfully processed
        files_with_errors (int): Number of files that encountered errors
        total_tokens (int): Total number of tokens processed across all files
        name_tokens (int): Number of NAME tokens (identifiers) that were translated
        processing_time (float): Total time spent processing files in seconds
        error_files (List[str]): List of file paths that encountered errors
    """

    files_tested: int = 0
    files_with_errors: int = 0
    total_tokens: int = 0
    name_tokens: int = 0
    processing_time: float = 0.0
    error_files: List[str] = field(default_factory=list)

    @property
    def total_files_attempted(self) -> int:
        """Total number of files that were attempted to be processed."""
        return self.files_tested + self.files_with_errors

    @property
    def success_rate(self) -> float:
        """Success rate as a percentage (0.0 to 100.0)."""
        if self.total_files_attempted == 0:
            return 0.0
        return (self.files_tested / self.total_files_attempted) * 100.0

    @property
    def translatable_token_ratio(self) -> float:
        """Percentage of NAME tokens (translatable identifiers) relative to total tokens."""
        if self.total_tokens == 0:
            return 0.0
        return (self.name_tokens / self.total_tokens) * 100.0


class StatisticsCollector:
    """
    Collector for aggregating test statistics across multiple file translations.

    This class provides methods to record statistics from individual file
    translations and aggregate them into comprehensive test statistics.
    """

    def __init__(self):
        """Initialize a new statistics collector."""
        self.stats = TestStatistics()
        self.start_time: Optional[float] = None

    def start_collection(self):
        """Start the statistics collection timer."""
        self.start_time = time.time()

    def stop_collection(self):
        """Stop the statistics collection timer and record total processing time."""
        if self.start_time is not None:
            self.stats.processing_time = time.time() - self.start_time

    def record_file_success(self, file_path: str, total_tokens: int, name_tokens: int):
        """
        Record statistics for a successfully processed file.

        Args:
            file_path (str): Path to the file that was processed
            total_tokens (int): Total number of tokens in the file
            name_tokens (int): Number of NAME tokens in the file
        """
        self.stats.files_tested += 1
        self.stats.total_tokens += total_tokens
        self.stats.name_tokens += name_tokens

    def record_file_error(self, file_path: str, error_message: str = ""):
        """
        Record a file that encountered an error during processing.

        Args:
            file_path (str): Path to the file that encountered an error
            error_message (str): Optional error message description
        """
        self.stats.files_with_errors += 1
        self.stats.error_files.append(file_path)

    def get_statistics(self) -> TestStatistics:
        """
        Get the current aggregated statistics.

        Returns:
            TestStatistics: Current statistics data
        """
        return self.stats

    def format_summary(self) -> str:
        """
        Format the statistics into a human-readable summary report.

        Returns:
            str: Formatted statistics summary
        """
        stats = self.stats

        # Format large numbers with commas
        def format_number(num: int) -> str:
            return f"{num:,}"

        summary_lines = [
            "",
            "=" * 50,
            "🔍 PIYATHON TRANSLATION TEST STATISTICS",
            "=" * 50,
            f"📁 Files processed:",
            f"   ✅ Successfully tested: {format_number(stats.files_tested)}",
            f"   ❌ Files with errors:   {format_number(stats.files_with_errors)}",
            f"   📊 Success rate:        {stats.success_rate:.1f}%",
            "",
            f"🔤 Token analysis:",
            f"   🔢 Total tokens:        {format_number(stats.total_tokens)}",
            f"   🏷️  NAME tokens:         {format_number(stats.name_tokens)}",
            f"   📈 Translatable token ratio: {stats.translatable_token_ratio:.2f}%",
            "",
            f"⏱️  Processing time:       {stats.processing_time:.1f} seconds",
        ]

        if stats.error_files:
            summary_lines.extend(
                [
                    "",
                    f"❌ Files with errors ({len(stats.error_files)}):",
                    *[f"   • {file_path}" for file_path in stats.error_files[:10]],
                ]
            )
            if len(stats.error_files) > 10:
                summary_lines.append(f"   ... and {len(stats.error_files) - 10} more")

        summary_lines.extend(["", "=" * 50, ""])

        return "\n".join(summary_lines)


# Global statistics collector instance for the test session
_global_collector: Optional[StatisticsCollector] = None


def get_global_collector() -> StatisticsCollector:
    """
    Get or create the global statistics collector instance.

    Returns:
        StatisticsCollector: The global collector instance
    """
    global _global_collector
    if _global_collector is None:
        _global_collector = StatisticsCollector()
    return _global_collector


def reset_global_collector():
    """Reset the global statistics collector to start fresh."""
    global _global_collector
    _global_collector = StatisticsCollector()
