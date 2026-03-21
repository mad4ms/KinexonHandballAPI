"""Kinexon Handball API wrapper package."""

from kinexon_handball_api.statistics_center import (
    StatisticsCenterAPI,
    StatisticsCenterAPIError,
)

__all__ = ["StatisticsCenterAPI", "StatisticsCenterAPIError"]
