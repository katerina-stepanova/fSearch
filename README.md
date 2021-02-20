# fSearch
Поиск по сайту sledcom.ru и его региональным подсайтам. Используется апи гугла.

**Важно:** кастомный поиск ограничен 100 запросами в сутки. Один прогон проекта в конфигурации по умолчанию использует минимум 16 запросов.

### Установка и запуск
- Ставим питон 3.7.5 (Windows: желательно поставить галочку "Add python 3.7 to path")
- Ставим pipenv (pip3 install pipenv - линукс, мак; pip install pipenv - винда)
- Скачиваем/клонируем проект
- Заходим в терминале в папку проекта 
- Запускаем pipenv install (или pipenv install --ignore-pipfile чтобы поставить версии точно из Pipfile.lock)
- Запускаем pipenv shell
- Меняем параметры конфигурации если надо (см. ниже)
- Запускаем скрипт: python3 fSearch.py - линукс, мак; python fSearch.py - винда

### Конфигурация
config.py - конфигурация поисковых запросов и даты. По умолчанию поиск идет за последние 7 дней

custom_search_config.py - конфигурация кастомного поиска гугла. Ничего не надо редактировать, если этот файл вам достался с заполненными значениями)

### Создание своего кастомного поиска гугла для этого проекта
Если вам достался пустой custom_search_config.py или вы не хотите использовать значения по умолчанию.

Instruction to create apiKey and cx
1. Create google account or use existing one
2. Create google custom search - https://cse.google.com/cse/all
3. Properties:
   - Region: Russia
   - Restrict results to region - ON
   - Sites to search: \*.sledcom.ru/news/\*
4. cx = Search engine ID
5. Go to https://developers.google.com/custom-search/v1/overview
   Click Get a Key
   Select previously created search
   Copy key and use it as apiKey


Насчет лицензий: если у вас есть доступ к проекту и вы его хотите распространять - не возражаю. Можете это делать с любой копилефтной лицензией, которая совместима с лицензиями использованных библиотек. А мне просто лень выяснять этот момент ;)
