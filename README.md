# MLOps: учебный проект команды 2

Учебный ML-проект курса «Управление процессами машинного обучения (MLOps)».
Тема проекта: Система рекомендаций
Описание: MLOps система для рекомендации товаров/контента пользователям

## Требования

- Git
- Python 3.12 (версия зафиксирована в `.python-version`)
- Docker для ЛР1 не нужен

## Установка

Клонирование:

```bash
git clone https://github.com/kucheranton200/T26_MLOps.git
cd T26_MLOps
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux или macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Проверки

```bash
python -m ruff check .
python -m pytest -q
```

## Запуск

```bash
python -m mlops_project
```

Ожидаемый вывод: `mlops project is ready`.

## Структура

```
.github/        шаблоны issue и PR, CI workflow
data/           данные (в Git не попадают, кроме .gitkeep)
docs/           ADR, карточки вклада, роли команды
src/            исходный код пакета mlops_project
tests/          тесты
```

## Как работать с репозиторием

Правила веток, commit, pull request и review: [CONTRIBUTING.md](CONTRIBUTING.md).
