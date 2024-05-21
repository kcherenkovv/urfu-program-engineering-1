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


def show_result(number_image, number_text, region):
    st.image(number_image)
    if number_text is None or len(number_text) == 0:
        st.subheader('Не удалось распознать номер на этом фрагменте')
    else:
        st.subheader(f'Распознанный номер: {number_text}')
        st.subheader(f'Регион: {region}')


def show_result_small(number_image):
    st.image(number_image)


def show_result_title():
    st.title("Результаты поиска:")
