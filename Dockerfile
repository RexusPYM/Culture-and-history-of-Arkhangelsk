FROM python:3.11-slim-bullseye

RUN mkdir culture_and_history
WORKDIR culture_and_history

ADD requirements.txt /culture_and_history/
RUN pip install -r requirements.txt

ADD . /culture_and_history/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]