#getting OS and Python image from DockerHub
FROM python:3.13.1-slim-bullseye

WORKDIR /docker

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python3", "-m", "flask", "--app", "predict_insurance", "run", "--host=0.0.0.0"]