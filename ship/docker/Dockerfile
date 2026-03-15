FROM python:3.12-slim

LABEL maintainer="OCTALUME <octalume@harery.com>"
LABEL description="OCTALUM-PYLAB Learning Environment"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml ./
RUN uv pip install --system -e .[dev,docs,notebooks]

COPY . .

RUN chmod +x ship/scripts/*.py

EXPOSE 8000 8888

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)"

CMD ["bash"]
