import yolov5
import os_tools as ost


def load_model():
    model = yolov5.load('keremberke/yolov5m-license-plate')
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 1000  # maximum number of detections per image
    return model


def process_image(model, img_path):
    ost.remove_folder('results/')
    results = model(img_path, size=640)
    results = model(img_path, augment=True)
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    results.save(save_dir='results/')
    return results

