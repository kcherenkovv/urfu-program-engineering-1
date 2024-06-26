[![Tests](https://github.com/kcherenkovv/urfu-program-engineering-2/actions/workflows/python-app.yml/badge.svg)](https://github.com/kcherenkovv/urfu-program-engineering-2/actions/workflows/python-app.yml)
# Распознавание автомобильных номеров и определение региона регистрации автомобиля

Проект по курсу "Программная инженерия 2" магистратуры УРФУ

## О проекте

### Описание работы
- Находит на изображении фрагменты с автомобильными номерами и показывает их
- Распознаёт символы на каждом фрагменте
- Проверяет, к какому региону относится изображенный номер и отображает наименование данного региона
  
### Используемые библиотеки и модели
- Для поиска номера использует модель из Hugging Face [keremberke/yolov5m-license-plate]
- Для распознавания текста используется модель из Hugging Face [microsoft/trocr-base-printed]
- Интерфейс пользователя - библиотека [streamlit]
- Для работы API - FastAPI и uvicorn
### Системные требования
- Компьютер и система удовлетворяющие требованиям PyTorch
  - Подробнее на офф. сайте: https://pytorch.org/get-started/locally/
  - 
### Как это выглядит
![screen1](https://github.com/kcherenkovv/urfu-program-engineering-2/blob/main/screens/Example.png)

### Как запустить WEB streamlit
- Установить PyTorch:    https://pytorch.org/get-started/locally/  
- Установить зависимости:    `pip install -r requirements_dev.txt`
- Запустить проект с помощью streamlit: 
  `streamlit run main.py`
- Через браузер открыть адрес, указанный в streamlit и загрузить изображение.
  - Примеры изображений есть в папке `/example_img`

### Как запустить API
- При необходимости можно запустить API. Оно работает в отдельном процессе на базе веб-сервера uvicorn
- Команда для запуска API: `uvicorn api:app`
- В API реализовано 2 метода: 
- - GET `/` - для проверки работы. Возвращает строку с приветствием.
- - POST `/recognize` - распознавание номеров на изображении. Он принимает единственный параметр - файл изображения и возвращает массив с распознанными
    на изображении номерами автомобилей.
- Пример запроса через CURL:
`curl -X 'POST' 'http://127.0.0.1:8000/recognize' -F 'file=@example_1.jpg;type=image/jpeg'`
 
### Демо-версия приложения в облаке STREAMLIT доступна по ссылке:
https://urfu-program-engineering-1-group-1-18.streamlit.app/

## Команда
- #### Кирилл Черенков
- #### Екатерина Таратута
- #### Михаил Вяткин
- #### Николай Шешин
- #### Серафим Загородний
  



  
