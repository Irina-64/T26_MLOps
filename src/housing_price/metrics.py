"""Метрики качества регрессионной модели цены жилья."""

import math
from collections.abc import Sequence


def _check_lengths(y_true: Sequence[float], y_pred: Sequence[float]) -> None:
    if len(y_true) != len(y_pred):
        raise ValueError(f"Разная длина: y_true={len(y_true)}, y_pred={len(y_pred)}")
    if not y_true:
        raise ValueError("Пустые последовательности")


def rmse(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    """Root Mean Squared Error — основная метрика качества проекта."""
    _check_lengths(y_true, y_pred)
    squared = [(t - p) ** 2 for t, p in zip(y_true, y_pred, strict=True)]
    return math.sqrt(sum(squared) / len(squared))


def mae(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    """Mean Absolute Error — вспомогательная, легко интерпретируемая метрика."""
    _check_lengths(y_true, y_pred)
    return sum(abs(t - p) for t, p in zip(y_true, y_pred, strict=True)) / len(y_true)
