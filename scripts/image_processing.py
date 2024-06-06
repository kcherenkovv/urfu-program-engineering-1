from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import streamlit as st
import re

# Создаём класс для обработки изображений с помощью библиотеки transformers


class LicensePlateRecognizer:

    __processor = None
    __model = None

    def __init__(self):
        self.__processor = TrOCRProcessor.from_pretrained(
            "microsoft/trocr-base-printed"
        )
        self.__model = VisionEncoderDecoderModel.from_pretrained(
            "microsoft/trocr-base-printed"
        )

    def process_image(self, img):
        pixel_values = self.__processor(images=img,
                                        return_tensors="pt").pixel_values
        generated_ids = self.__model.generate(pixel_values)
        generated_text = self.__processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )[0]
        return self.post_process_plate_text(generated_text)

    def post_process_plate_text(self, plate_text):
        return re.sub(r'[\W_]+', '', plate_text)


# Применяем декоратор для кеширования результатов,
# чтобы избежать повторных вычислений

@st.cache_data
def get_instance():
    return LicensePlateRecognizer()
