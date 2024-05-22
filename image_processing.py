from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import streamlit as st

#Создаём класс для обработка изображений с помощью библиотеки transofrmers
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
        return generated_text

#Применяем декоратор для кеширования результатов, чтобы избежать повторных вычислений
@st.cache_data
def get_instance():
    return LicensePlateRecognizer()
