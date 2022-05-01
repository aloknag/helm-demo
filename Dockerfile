FROM python:3.8-alpine
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
CMD ["python",  "app.py"]
EXPOSE 8000