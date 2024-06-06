import pytest
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from unittest.mock import patch
from scripts.find_region import find_region
from scripts.image_processing import LicensePlateRecognizer
from scripts.numbers_detection import load_model, process_image
from scripts.web_view import load_image
import io
import os


# Тесты для find_region.py
def test_find_region_exists():
    assert find_region('01ABCD777') == 'Москва'


def test_find_region_not_found():
    assert find_region('99XYZ800') == 'Регион не найден'


# Тесты для image_processing.py
def test_image_processing():
    recognizer = LicensePlateRecognizer()
    image = Image.open(os.path.join('example_img', 'test.jpg'))  # Путь к изображению для теста
    result = recognizer.process_image(image)
    assert result == 'M666MM777'


# Тест для web_view.py
def test_load_image():
    with open(os.path.join('example_img', 'example_1.jpg'), 'rb') as file:
        test_image = file.read()
    with patch('streamlit.file_uploader') as mock_file_uploader:
        mock_file_uploader.return_value = io.BytesIO(test_image)
        result = load_image()
        assert isinstance(result, JpegImageFile)


def test_process_image():
    model = load_model()
    image = Image.open(os.path.join('example_img', 'example_1.jpg'))  # Путь к изображению для теста
    result = process_image(model, image)
    assert len(result) > 0


# Запуск всех тестов
if __name__ == '__main__':
    pytest.main()
