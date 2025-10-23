FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Porta padrão do Flask
EXPOSE 5000

CMD ["python", "app.py"]
