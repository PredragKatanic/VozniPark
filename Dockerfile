# Koristite službenu tiangolo/uvicorn-gunicorn-fastapi sliku kao osnovnu
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Postavite radni direktorij u kontejneru
WORKDIR /app

# Kopirajte requirements.txt u radni direktorij
COPY requirements.txt /tmp/requirements.txt

# Instalirajte Python ovisnosti
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Kopirajte cijeli app direktorij u radni direktorij kontejnera
COPY ./app /app
