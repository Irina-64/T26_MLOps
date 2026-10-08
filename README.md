# housing-price

Учебный MLOps-проект команды №4 курса «Управление процессами машинного обучения (MLOps)»:
прогнозирование стоимости жилья (тема 1 — Housing Price Prediction).

## Структура

- `src/housing_price/` — Python-пакет проекта (метрики качества, точка входа CLI).
- `tests/` — тесты pytest.
- `data/` — локальные данные, в Git не коммитятся (см. `data/README.md`).
- `docs/` — документация команды.
- `.github/workflows/ci.yml` — CI: Ruff и pytest.

## Требования

- Git
- Python 3.12 (версия зафиксирована в `.python-version`)

## Установка

Клонирование:

```bash
git clone https://github.com/haiksarg/T26_MLOps.git
cd T26_MLOps
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python --version
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux или macOS:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Команда `python --version` должна показать `Python 3.12.x`. Если версия другая,
окружение создано не тем интерпретатором: удалите `.venv` и создайте заново.

## Проверки

```bash
python -m ruff check .
python -m pytest -q
```

Ожидаемый вывод:

```text
All checks passed!
.........                                                        [100%]
9 passed in 0.03s
```

## Запуск

```bash
python -m housing_price
housing-price --version
```

Ожидаемый вывод (версия Python может отличаться):

```text
housing-price 0.1.0 | Python 3.12.10
smoke check: RMSE=11902.4, MAE=11666.7
housing-price 0.1.0
```

## Документация

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [ADR 0001](docs/adr/0001-project-boundaries.md)
- [Роли команды](docs/team-roles.md)
