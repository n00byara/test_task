FROM python:3.13.2
LABEL authors="MikhailAminov"

WORKDIR /usr/app
COPY requirements.txt /usr/app

RUN pip install -r requirements.txt
CMD ["python", "main.py"]