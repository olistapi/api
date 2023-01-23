FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV FASTAPI main.py

ENV FASTAPI_HOST 0.0.0.0

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
