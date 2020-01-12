# Список запросов, каждое отдельное значение в кавычках, значения разделены запятой
queries = ["убил", "убила", "зарезал", "зарезала", "зарубил", "зарубила", "сжег", "сожгла", "застрелил", "застрелила",
           "задушил", "задушила", "погиб", "погибла", "убийство", "тяжкие телесные"]
# Дата. Результаты будут запрошены за 7 дней до указанной даты включительно
# Формат даты - "ГГГГ-ММ-ДД" (год-месяц двумя цифрами-день), в кавычках
# Если указать "сегодня" или "now" будет взята текущая дата
# Обработки ошибок по дате нет, скрипт нормально не сработает если дата некорректная
# date = "2020-01-04"
date = "now"
