FROM --platform=$BUILDPLATFORM python:3.11.3-slim-bullseye

COPY backend/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY alembic alembic
COPY alembic.ini .
COPY backend backend

CMD [ "alembic", "upgrade", "head", "&&", "uvicorn", "backend.app.main.routes:app", "--host", "0.0.0.0", "--port", "8000" ]