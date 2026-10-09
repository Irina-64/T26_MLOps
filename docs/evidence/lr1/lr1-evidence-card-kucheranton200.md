# Evidence card ЛР1 Kucher Anton

| Поле | Значение |
|---|---|
| Студент | Кучер Антон, Т26УПМО-Т.МО41, team-2, @kucheranton200 |
| Контрольная версия |  TODO: Ссылка на tag `lr1-v1` и commit SHA  |
| Роль | Repository administrator |
| Задача | Issue #1 |
| Личный артефакт | [PR #2](https://github.com/kucheranton200/T26_MLOps/pull/2): `docs/lr1/lr1-repo-settings.md`, `docs/evidence/lr1-main-ruleset.json`; [issue #1](https://github.com/kucheranton200/T26_MLOps/issues/1) |
| Вклад | экспорт правил (ruleset) и PR с ним, шаблоны issue и PR |
| Решение | Защиту `main` настроил через ruleset, а не через классическое правило ветки, потому что ruleset экспортируется в JSON, и правила можно показать и сверить с настройками. Проверка: попытка прямого `git push` в `main` отклоняется. |
| Риск | Настройки в Settings и документация могут разойтись: правило изменят в интерфейсе, а `lr1-repo-settings.md` и CONTRIBUTING останутся прежними. Обнаруживается сверкой текущего ruleset с `lr1-main-ruleset.json` и таблицей в `lr1-repo-settings.md`. Второй риск: обязательная проверка `quality` блокирует merge, если CI упадёт или будет переименован job. Обнаруживается по PR: merge недоступен, а статус `quality` не найден или красный. |