FROM python:3.13.5-alpine3.21
COPY /app /app
WORKDIR app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "./app.py"]