# Usa uma imagem base do Python
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt


# Expõe a porta que o app Flask usará
EXPOSE 8080

# Comando para iniciar a aplicação usando Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "KandeguesJobs.app:app"]
