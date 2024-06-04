import scripts.numbers_detection as nd
import scripts.web_view as web_view
import scripts.image_processing as ocr
from scripts.find_region import find_region


if __name__ == '__main__':
    # Инициализация модели поиска номеров
    nd_model = nd.load_model()
    # Инициализация модели распознавания текста
    ocr = ocr.get_instance()
    # Отрисовка заголовка страницы
    web_view.init()
    # Получение изображения от пользователя
    img = web_view.load_image()

    if img is not None:
        # Поиск номеров на изображении
        result_images = nd.process_image(nd_model, img)
        if result_images is not None:
            # Отрисовка заголовка раздела с результатами
            web_view.show_result_title()
            for number_image in result_images:
                # Распознавание текста на изображении номера
                number_text = ocr.process_image(number_image)
                region = find_region(number_text)
                # Отрисовка результата - изображение
                # номера и распознанный на нём текст
                web_view.show_result(number_image, number_text, region)
                

