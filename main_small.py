import numbers_detection as nd
import web_view


if __name__ == '__main__':
    # Инициализация модели поиска номеров
    nd_model = nd.load_model()
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
                web_view.show_result_small(number_image)
