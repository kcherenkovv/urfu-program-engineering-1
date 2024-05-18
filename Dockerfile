FROM python:3.8-slim

WORKDIR /app

COPY . /app

COPY requirements_all.txt /app/requirements_all.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

RUN pip install -r /app/requirements_all.txt

CMD ["streamlit", "run", "/app/main.py"]