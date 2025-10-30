FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml ./

# Install dependencies
RUN uv sync

# Copy application files
COPY predict_hw.py pipeline_v1.bin ./
 
EXPOSE 8000

ENTRYPOINT ["uv", "run", "uvicorn", "predict_hw:app", "--host", "0.0.0.0", "--port", "8000"]