FROM python:3.13-slim

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir uv 
RUN uv sync --frozen

# Set PYTHONPATH to include src directory
ENV PYTHONPATH=/app/src

# Activate the virtual environment in PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000 
CMD ["uvicorn", "website.main:app", "--host", "0.0.0.0", "--port", "8000"]
 