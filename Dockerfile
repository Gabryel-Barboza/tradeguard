# Imagem otimizada do python
FROM python:3.13.12-slim-bookworm

# Instalação de libs para build de pacotes específicos python
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Criando diretório app principal
WORKDIR /app

# Instalando dependências python
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiando restante dos módulos
COPY . .
