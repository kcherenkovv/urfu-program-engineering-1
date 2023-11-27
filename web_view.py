import io
import streamlit as st
from PIL import Image


def load_image():
    uploaded_file = st.file_uploader(
        label='Выберите изображение, на котором изображен автомобиль с номером')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def init():
    # Выводим заголовок страницы средствами Streamlit
    st.title('Поиск автомобильных номеров на изображении')


def show_result(img):
    st.image(img)


def show_result_title():
    st.title('Результат распознавания')

