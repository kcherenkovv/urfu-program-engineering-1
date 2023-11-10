# Распознавание автомобильных номеров
Проект по курсу "Программная инженерия 1" магистратуры УРФУ
## О проекте
### Описание
- Находит на изображении автомобильный номер и показывает его
- Язык проекта - python
- Для поиска номера использует модель из Hugging Face keremberke/yolov5m-license-plate
- Интерфейс пользователя - библиотека streamlit
### Системные требования
- Компьютер и система удовлетворяющие требованиям PyTorch
  - Подробнее на офф. сайте: https://pytorch.org/get-started/locally/
### Как это выглядит
![alt text](https://github.com/Alex-mur/urfu-program-engineering-1/blob/main/screens/scr1.JPG)

### Как запустить
- Установить PyTorch:    https://pytorch.org/get-started/locally/  
- Установить зависимости:    `pip install yolov5 streamlit Image`
- Запустить проект с помощью streamlit: 
  `streamlit run main.py`
- Через браузер открыть адрес, указанный в streamlit и загрузить изображение.
  - Примеры изображений есть в папке `/example_img`



  
