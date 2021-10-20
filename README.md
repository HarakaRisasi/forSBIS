
## Discription of elements (leng: RUS)

**google chrome only**

> main.py 

содержит необходимые настройки webdriver для управления Chrome.

> find_road.py

составляет маршрутный список для работы **page_scaner**.

так же получает список наименований требующихся далее для составления таблицы.

результат выполнения программы **page_scanner.py** требует форматирование полученных данных с помощью **filter.py**.

результат выполнения программы **filter.py** требует перемещения полученных данных в **map_road.py**.

#### Для работы find_road.py требуется:

> string_route_for_find_road.py 

запустить ЭТОТ вспомогательный модуль и выполнить внутренние инструкции.

> page_scanner.py 

сканирует каждую страницу ресурса.

считает количество валидных элементов.

сохраняет полученные данные в файл

> map_road.py 

служит для указания маршрута действия **page_scanner.py**

заполняется вручную от **find_road.py** 

- такой метод заполнения нужен для более гибкой настройки сканирования

> timing.py

реализует рандомные тайминги для обхода "recaptcha"

> start.py

**после доработки планируется** использовать для большей автоматизации процесса выполнения программ в целом

---

## Discription of elements (leng: ENG)

**google chrome only**

> main.py

Contains the necessary webdriver settings for managing Chrome.

> find_road.py

Compiles a route list for work **page_scaner**.

Also receives a list of items required later to compile the table.

Program execution result **page_scanner.py** requires formatting the received data with **filter.py**.

Program execution result **filter.py** requires moving the received data to **map_road.py**.

#### find_road.py requires:

> string_route_for_find_road.py

Run THIS auxiliary module and follow the internal instructions.

> page_scanner.py

Scans every page of the resource.

Counts the number of valid elements.

Saves the received data to a file.

> map_road.py

Serves to indicate the route of action **page_scanner.py**.

Manually populated by **find_road.py**.

- this filling method is needed for more flexible scan settings.

> timing.py

Implements random timings to bypass site protection.

> start.py

**after completion it is planned** to be used for greater automation of the program execution process as a whole.
