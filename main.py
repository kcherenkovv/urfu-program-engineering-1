import numbers_detection as nd
import web_view
from PIL import Image

if __name__ == '__main__':
    model = nd.load_model()
    web_view.init()
    img = web_view.load_image()
    if img is not None:
        img.save("upload/car_image.jpg")
        nd.process_image(model, 'upload/car_image.jpg')
        web_view.show_result(Image.open('results/car_image.jpg'))
