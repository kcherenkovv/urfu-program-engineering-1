import numbers_detection as nd
import web_view

if __name__ == '__main__':
    model = nd.load_model()
    web_view.init()
    img = web_view.load_image()
    if img is not None:
        result_images = nd.process_image(model, img)
        if result_images is not None:
            web_view.show_result_title()
            for result_img in result_images:
                web_view.show_result(result_img)
