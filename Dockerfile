FROM python:3.11-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

# I'm leaving this in here because having the --reolad is nice for local dev
# it isn't a good idea for production but keeping it to show I used it
#CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000", "--reload"]
