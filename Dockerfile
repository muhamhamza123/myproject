FROM python:3.11-slim

LABEL maintainer="hamza <hamzasahi72000@gmail.com>"
LABEL project="Project DIWA"

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user (required by BinderHub)
ARG NB_USER=jovyan
ARG NB_UID=1000
RUN useradd --create-home --shell /bin/bash --uid ${NB_UID} ${NB_USER}

WORKDIR /home/${NB_USER}/repo
COPY --chown=${NB_USER}:${NB_USER} . .

USER ${NB_USER}

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--port=8888", \
     "--no-browser", \
     "--NotebookApp.token=''", \
     "--NotebookApp.password=''"]
