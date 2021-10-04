FROM python:3.7.5-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py .
COPY utils.py .
COPY /model ./model

RUN python -m spacy download en_core_web_sm
CMD ["python", "app.py"]
