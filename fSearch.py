import requests
import datetime
import html2text
import config
import custom_search_config as csc

baseURL = csc.baseURL
# List of queries used
qs = config.queries
# Custom search parameters
apiKey = csc.apiKey
cx = csc.cx

results = []


def info_from_item(this_item):
    link = this_item["link"]
    extra_stuff = ["?print=1", "?year=&month=&day=&type=main", "?type=news", "ion=60", chr(174)]
    for st in extra_stuff:
        link = link.replace(st, "")
    # get text
    text_full = requests.get(link).text
    # TODO improvement better text extraction
    news_text = html2text.html2text(text_full)
    # get region
    reg = link[link.index("://") + 3:link.index(".")]
    news_region = reg if reg != 'sledcom' else "region unknown"
    # get news id
    link_split = link.split("/")
    news_id = link_split[len(link_split) - 1] if link_split[len(link_split) - 1] != "" else link_split[
        len(link_split) - 2]
    return {
        "link": link,
        "snippet": this_item["snippet"],
        "text": news_text,
        "region": news_region,
        "id": news_id
    }


def string_from_date(date):
    m = str(date.month) if date.month > 9 else "0" + str(date.month)
    d = str(date.day) if date.day > 9 else "0" + str(date.day)
    y = str(date.year)
    return y + m + d


def get_dates_range():
    if config.date == "сегодня" or config.date == "now":
        dt_to = datetime.datetime.now()
    else:
        dt_to_list = config.date.split("-")
        dt_to = datetime.datetime(int(dt_to_list[0]), int(dt_to_list[1]), int(dt_to_list[2]))
    dt_from = dt_to - datetime.timedelta(7)
    return [dt_from, dt_to]


def create_date_restriction():
    dates_range = get_dates_range()
    dt_from = dates_range[0]
    dt_to = dates_range[1]
    return "&sort=date:r:" + string_from_date(dt_from) + ":" + string_from_date(dt_to)


def check_duplicates(items_list, item_to_add):
    has_duplicate = False
    for it in items_list:
        if it["id"] == item_to_add["id"] and it["region"] == item_to_add["region"]:
            has_duplicate = True
            break
    return has_duplicate


def check_date_in_range(item):
    dates_range = get_dates_range()
    item_date = ""
    # TODO improvement - get date out of document and check it's in range
    return True


def add_to_results(items_to_add):
    for item in items_to_add:
        res = info_from_item(item)
        has_duplicates = check_duplicates(results, res)
        dates_in_range = check_date_in_range(res)
        if dates_in_range and not has_duplicates:
            results.append(res)


# Iterating through queries
for q in qs:
    dates_r = create_date_restriction()
    # requestString = baseURL + apiKey + cx + "&q=site:*.sledcom.ru/news/* " + q + dates_r
    request_string = baseURL + apiKey + cx + "&q=" + q + dates_r
    search_response = requests.get(request_string)
    data = search_response.json()
    if "error" in data:
        print("Ошибка использования апи. Вероятно исчерпан лимит запросов за сутки. Попробуйте завтра.")
        print("Детали ошибки: ")
        print(data["error"]["message"])
        exit(1)
    print("Получена первая страница по запросу: " + q)
    total_results = int(data["searchInformation"]["totalResults"])
    print("Результатов по запросу: " + data["searchInformation"]["totalResults"])
    if total_results > 0:
        items = data["items"]
        add_to_results(items)
        if total_results > 10:
            i = 10
            while i < min([total_results, config.max_results]):
                request_string = baseURL + apiKey + cx + "&q=" + q + dates_r + '&start=' + str(i)
                search_response = requests.get(request_string)
                print("Получены результаты начиная с " + str(i) + "го по запросу: " + q)
                data = search_response.json()
                if "items" in data:
                    items = data["items"]
                    add_to_results(items)
                i = i + 10
print("Результаты получены без ошибок")
print("Создаем html файл...")
html = """<html><table border="1">
<tr><th>Id</th><th>Регион</th><th>Ссылка</th><th>Текст</th></tr>"""
""""link": link,
        "snippet": this_item["snippet"],
        "text": news_text,
        "region": news_region,
        "id": news_id"""
for row in results:
    html += "<tr><td>{}</td>".format(row["id"])
    html += "<td>{}</td>".format(row["region"])
    html += "<td><a href=\"{}\">{}</a></td>".format(row["link"], row["link"])
    html += "<td>{}</td>".format(row["snippet"])  # TODO improvement: full text as a tooltip or smth
    html += "</tr>"
html += "</table></html>"
print("HTML готов, записываем в файл...")
filename = str(datetime.datetime.now()).replace(":", "-").replace(".", "-") + ".html"
file = open(filename, "w")
file.write(html)
file.close()
print("Файл записан в текущую директорию. Имя файла: " + filename)
