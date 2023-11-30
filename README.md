# Распознавание автомобильных номеров
Проект по курсу "Программная инженерия 1" магистратуры УРФУ
## О проекте
### Описание работы
- Находит на изображении фрагменты с автомобильными номерами и показывает их
- Распознаёт символы на каждом фрагменте
### Используемые библиотеки и модели
- Для поиска номера использует модель из Hugging Face [keremberke/yolov5m-license-plate]
- Для распознавания текста используется модель из Hugging [Face microsoft/trocr-base-printed]
- Интерфейс пользователя - библиотека [streamlit]
- Для работы API - FastAPI и uvicorn
### Системные требования
- Компьютер и система удовлетворяющие требованиям PyTorch
  - Подробнее на офф. сайте: https://pytorch.org/get-started/locally/
### Как это выглядит
![screen1](https://github.com/Alex-mur/urfu-program-engineering-1/blob/main/screens/scr1.JPG)

### Как запустить WEB streamlit
- Установить PyTorch:    https://pytorch.org/get-started/locally/  
- Установить зависимости:    `pip install -r requirements.txt`
- Запустить проект с помощью streamlit: 
  `streamlit run main.py`
- Через браузер открыть адрес, указанный в streamlit и загрузить изображение.
  - Примеры изображений есть в папке `/example_img`

### Как запустить API
- При необходимости можно запустить API. Оно работает в отдельном процессе на базе веб-сервера uvicorn
- Команда для запуска API: `uvicorn api:app`
- В API есть только один метод POST:  `/recognize`.
Он принимает единственный параметр - изображение в формате [multipart/form-data] и возвращает массив с распознанными
на изображении номерами.
- Пример запроса через CURL:
`curl -X 'POST' 'http://127.0.0.1:8000/recognize' -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@example_3.jpg;type=image/jpeg'`
 
### Что планируется сделать
- Выложить готовое решение на хостинг для доступа через интернет.

## Команда
- #### Алексей Муравьев
- #### Екатерина Таратута
- ####
- ####



  
