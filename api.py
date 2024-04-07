from fastapi import FastAPI, UploadFile
import numbers_detection as nd
import image_processing as textocr
from PIL import Image
import io

app = FastAPI()
# Инициализация модели поиска номеров
nd_model = nd.load_model()
# Инициализация модели распознавания текста
ocr = textocr.get_instance()


@app.get("/")
def hello():
    return {"message": "Welcome to the ALPR app"}


@app.post("/recognize")
async def recognize(file: UploadFile):
    image_data = file.file.read()
    img = Image.open(io.BytesIO(image_data))
    result = list()
    if img is not None:
        # Поиск номеров на изображении
        result_images = nd.process_image(nd_model, img)
        if result_images is not None:
            for number_image in result_images:
                # Распознавание текста на изображении номера
                number_text = ocr.process_image(number_image)
                result.append(number_text)
    return result
