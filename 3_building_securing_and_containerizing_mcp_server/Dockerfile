FROM python:3.12-slim-bookworm

# Copy uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:0.6.16 /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Create a virtual environment and install dependencies
RUN uv venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies using uv in the virtual environment
RUN uv pip install -r requirements.txt
RUN uv pip install "mcp[cli]"

# Copy application code
COPY server.py .
COPY mcpreadme.md .

# Set environment variables
ENV PORT=8080
ENV HOST="0.0.0.0"

# Expose port
EXPOSE 8080

# Run the application
CMD ["uv", "run", "server.py"] 