# grad_proj
# Дипломный проект "Условный блог об истории моды и модных тенденциях"
# 
# Для разметки использованы CSS grid и flex.
# Пользователь может просматривать весь список статей и каждую статью отдельно, отфильтровывать статьи по тематике. После регистрации/авторизации доступна форма для создания
# новой статьи.
# Реализованы: полноценное редактирование постов из админ-панели (таблицы, форматирование шрифта и др.), пагинация, подсчет просмотров постов как зарегистрированными пользователями,
# так и по ip-адресу незаригистрированных.
# PostgreSQL выбрана по 2 причинам: 1) для организации полнотекстового поиска по заглавиям и контенту и 2) в последний момент пришла идея, что статьи из рубрики "Тренды сезона" должны автоматически удаляться через 3 месяца после публикации.
# Пока при поиске используется метод annotate, но как я поняла, при разрастании БД он работает медленно, поэтому с прицелом на будущее создано поле SearchVectorField, 
# которое индексируется PostgreSQL.
