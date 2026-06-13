FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PKOS_UPLOAD_DIR=/app/uploads \
    CHROMA_PERSIST_DIR=/app/chroma

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock* ./
RUN pip install --upgrade pip && \
    pip install "uv>=0.4.0" && \
    if [ -f uv.lock ]; then uv pip install --system --no-cache -r pyproject.toml; \
    else pip install -e /app; fi

COPY src/ ./src/
RUN mkdir -p /app/uploads /app/chroma && chmod -R 777 /app/uploads /app/chroma

EXPOSE 8501 8080

CMD ["streamlit", "run", "src/pkos/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
