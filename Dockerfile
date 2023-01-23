FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONUNBUFFERER 1

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
