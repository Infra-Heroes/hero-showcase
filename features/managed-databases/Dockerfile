FROM python:3.14-alpine
RUN pip install --no-cache-dir psycopg2-binary pymysql redis
COPY app.py /app.py
CMD ["python", "-u", "/app.py"]
