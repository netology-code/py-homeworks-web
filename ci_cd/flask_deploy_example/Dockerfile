FROM python:3.7
COPY ./app /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD ["gunicorn", "app:app"]
