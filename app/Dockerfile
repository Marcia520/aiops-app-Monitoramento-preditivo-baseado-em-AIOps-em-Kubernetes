# Imagem base leve do Python
FROM python:3.9-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar lista de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
