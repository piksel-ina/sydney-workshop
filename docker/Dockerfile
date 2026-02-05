FROM ubuntu:26.04

# Update package lists and install Python 3
# Do some cleanup, to minimise image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD square.py /app/square.py

WORKDIR /app

CMD ["python3", "square.py", "--help"]
