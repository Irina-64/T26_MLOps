"""Точка входа: `python -m housing_price` или `housing-price`."""

import argparse
import platform

from housing_price import __version__
from housing_price.metrics import mae, rmse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="housing-price",
        description="Прогнозирование стоимости жилья (учебный MLOps-проект).",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.parse_args(argv)

    # Smoke-проверка окружения: пакет импортируется, метрики считаются.
    y_true = [200_000.0, 310_000.0, 150_000.0]
    y_pred = [210_000.0, 300_000.0, 165_000.0]
    print(f"housing-price {__version__} | Python {platform.python_version()}")
    print(f"smoke check: RMSE={rmse(y_true, y_pred):.1f}, MAE={mae(y_true, y_pred):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
