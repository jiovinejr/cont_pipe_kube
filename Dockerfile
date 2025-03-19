FROM python:3.11-slim

WORKDIR /app

COPY requirements.text ./

RUN pip install --no-cache-dir upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .
    
CMD [ "python", "-m", "src.main" ]