# План ЛР1

Release lead: @GlooshSl
Репозиторий команды: https://github.com/kucheranton200/T26_MLOps

Сроки ниже: внутренний план команды. Они сдвигаются, если сдача по курсу назначена раньше.

## Задачи

| Роль / задача | Ответственный | Issue | Срок |
|---|---|---|---|
| Release lead: план ЛР1 (этот файл) | @GlooshSl | #6 | 11.10 |
| Repository administrator: доступ, правила main | @kucheranton200 | #1 | выполнено (PR #2) |
| Quality engineer: Ruff, pytest, CI | @Z0rko32 | #3 | выполнено (PR #4) |
| Documentation and risk reviewer: доработка ADR 0001 | @Vikabh | #? | 12.10 |
| Documentation and risk reviewer: CONTRIBUTING, CODEOWNERS | @Vikabh | #? | 13.10 |
| Environment engineer: Python 3.12, установка, README | @kerty0 | #? | 13.10 |
| Строки своих ролей в docs/team-roles.md | каждый свою | #? | 12.10 |
| Evidence card каждого участника | каждый свою | #? | 14.10 |
| Проверка установки по README на чистой машине | участник, не автор README | #? | 15.10 |
| Контрольная точка lr1-v1 (tag и Release) | @GlooshSl | #? | 16.10, после всех merge |
| Итоговый PR в репозиторий преподавателя (если требуется) | @kucheranton200 | #? | 16.10 |

## Порядок работы

1. У каждого участника своя issue с наблюдаемым результатом и критериями приёмки.
2. Каждое изменение делается в отдельной ветке и попадает в main только через pull request.
3. В описании pull request указывается `Closes #N` и способ проверки.
4. Merge возможен после зелёного CI и одобрения другого участника.
5. Тег `lr1-v1` ставится после merge всех pull request и добавления evidence cards.

# План ЛР1

Release lead: @GlooshSl
Репозиторий команды: https://github.com/kucheranton200/T26_MLOps

Сроки ниже: внутренний план команды. Они сдвигаются, если сдача по курсу назначена раньше.

## Задачи

| Роль / задача | Ответственный | Issue | Срок |
|---|---|---|---|
| Release lead: план ЛР1 (этот файл) | @GlooshSl | #6 | 11.10 |
| Repository administrator: доступ, правила main, шаблоны issue и PR | @kucheranton200 | #1 | выполнено (PR #2) |
| Quality engineer: Ruff, pytest, CI | @Z0rko32 | #3 | выполнено (PR #4) |
| Documentation and risk reviewer: доработка ADR 0001 | @Vikabh | #? | 12.10 |
| Documentation and risk reviewer: CONTRIBUTING, CODEOWNERS | @Vikabh | #? | 13.10 |
| Environment engineer: Python 3.12, установка, README | @kerty0 | #? | 13.10 |
| Строки своих ролей в docs/team-roles.md | каждый свою | #? | 12.10 |
| Evidence card каждого участника | каждый свою | #? | 14.10 |
| Проверка установки по README на чистой машине | участник, не автор README | #? | 15.10 |
| Контрольная точка lr1-v1 (tag и Release) | @GlooshSl | #? | 16.10, после всех merge |
| Итоговый PR в репозиторий преподавателя (если требуется) | @kucheranton200 | #? | 16.10 |

## Контроль связей issue и pull request

| Pull request | Автор | Issue | Review | Состояние на 09.10 |
|---|---|---|---|---|
| #2 docs: document repository settings and main ruleset | @kucheranton200 | #1 | требуется | влит |
| #4 [Quality] Настройка проверок CI и smoke-тестов | @Z0rko32 | #3 | одобрен @Vikabh и @kucheranton200 | влит |
| #5 docs: ADR-0001 project boundaries and risks | @Vikabh | #? | запрошен | открыт, нужна привязка к issue |
| #8 [Release] План ЛР1 | @GlooshSl | #6 | запрошен | в работе |

Таблица обновляется Release lead по мере появления новых pull request.

## Порядок работы

1. У каждого участника своя issue с наблюдаемым результатом и критериями приёмки.
2. Каждое изменение делается в отдельной ветке и попадает в main только через pull request.
3. В описании pull request указывается `Closes #N` и способ проверки.
4. Merge возможен после зелёного CI и одобрения другого участника.
5. Тег `lr1-v1` ставится после merge всех pull request и добавления evidence cards.