FROM python:3.9.7-slim
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/list/*
COPY . /app
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt && \
    chmod +x entrypoint.sh
RUN useradd -m appuser && chown -R appuser /app
USER appuser
CMD ["/app/entrypoint.sh"]