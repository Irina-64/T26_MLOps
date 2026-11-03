# MLOps Lab 1 — Team 5

Репозиторий команды для лабораторной работы №1: воспроизводимая среда разработки и командный Git-процесс.

## Команда
- Team lead: `neazsot`
- Участник: `papikyn` (`student-01`)

## Требования
- Python 3.12
- Установка зависимостей через `pyproject.toml`
- Проверки качества кода: Ruff
- Тесты: pytest
- CI запускается при push и pull request

## Быстрый старт
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e ".[dev]"
ruff check .
pytest
```

## Структура
```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/lab-task.yml
│   ├── workflows/ci.yml
│   └── pull_request_template.md
├── docs/
│   ├── adr/0001-project-boundaries.md
│   ├── evidence/lr1-evidence-card.md
│   └── team-roles.md
├── src/team5_mlops/
├── tests/
├── .gitignore
├── .python-version
├── CODEOWNERS
├── CONTRIBUTING.md
└── pyproject.toml
```
