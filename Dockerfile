FROM python:3.8-slim-buster
ADD ./src/requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD ./src /app/
RUN pip install -e /app/mycli
ENTRYPOINT ["python", "/app/mycli/mycli/main.py"]


