# Настройки репозитория

Автор: Кучер Антон, kucheranton200, роль: Repository administrator
Issue: #1

## Включённые возможности
- Issues: включены (Settings → General → Features), используется шаблон `lab-task.yml`
- Actions: включены, workflow `CI` (job `quality`) запускается на push и pull request
- Права workflow: только чтение содержимого (`contents: read`)

## Участники (collaborators)
| GitHub login | Роль в ЛР1 | Права |
|---|---|---|
| @login1 | Release lead | Write |
| @login2 | Environment engineer | Write |
| @Z0rko32 | Quality engineer | Write |
| @login4 | Documentation and risk reviewer | Write |

## Правила ветки main (ruleset `main-protection`)
| Правило | Зачем |
|---|---|
| Merge только через pull request | Прямой push в main невозможен, каждое изменение видно в истории |
| Минимум 1 одобрение | Изменение проверяет второй человек |
| Сброс устаревших одобрений при новых commit | Одобрение относится к актуальному diff |
| Одобрение последнего изменения не автором push | Автор не может подтвердить собственные правки |
| Обязательное разрешение обсуждений | Замечания reviewer'а не остаются без ответа |
| Обязательная проверка `quality` | В main не попадает код, не прошедший ruff и pytest |
| Запрет force push | История main не переписывается |
| Запрет удаления ветки | main нельзя удалить случайно |
| Bypass list | Правила действуют на всех коллабораторов |

Экспорт правил: [docs/evidence/main-ruleset.json](evidence/main-ruleset.json)

## Ограничения
Ограничений нет

## Скриншоты
Скришотов нет