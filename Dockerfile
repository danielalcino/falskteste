# Usa uma imagem base do Python
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependência
RUN pip install --no-cache-dir -r requirements.txt


# Expõe a porta que o app Flask usará
EXPOSE 8080

# Comando para iniciar a aplicação usando Gunicorn
ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]


