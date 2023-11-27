import yolov5
from PIL import Image
import streamlit as st


@st.cache_data
def load_model():
    model = yolov5.load('keremberke/yolov5m-license-plate')
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image
    return model


def process_image(model, img):
    results = model(img, size=640)
    results = model(img, augment=True)
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    # numpy_image = results.render()[0]
    # output_image = Image.fromarray(numpy_image)
    numpy_images = results.crop(save=False)
    # print(numpy_images[0])

    output_imgs = list()
    for numpy_img in numpy_images:
        output_imgs.append(Image.fromarray(numpy_img['im']))
    # print(output_imgs)
    return output_imgs

