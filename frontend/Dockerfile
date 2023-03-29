FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements /app
RUN pip install -r requirements
COPY . .
EXPOSE 8080
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]