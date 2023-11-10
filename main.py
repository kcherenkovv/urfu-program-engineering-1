import numbers_detection as nd
import web_view
from PIL import Image

if __name__ == '__main__':
    model = nd.load_model()
    web_view.init()
    img = web_view.load_image()
    if img is not None:
        nd.process_image(model, img)
        web_view.show_result(Image.open('results/image0.jpg'))
