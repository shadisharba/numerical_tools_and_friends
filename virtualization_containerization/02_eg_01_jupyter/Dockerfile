FROM python:3.12

ARG DEBIAN_FRONTEND=noninteractive

RUN apt -y update
RUN apt -y -qq install curl wget

# Download the latest installer
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh


# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.cargo/bin/:$PATH"

COPY requirements.txt .

RUN mkdir -p src
RUN mkdir -p data_lfs

# RUN uv python install 3.11.5
# RUN uv venv /opt/venv
RUN uv pip install --system --no-cache -r requirements.txt

# # Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
# ENV TINI_VERSION v0.6.0
# ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
# RUN chmod +x /usr/bin/tini
# ENTRYPOINT ["/usr/bin/tini", "--"]

# CMD ["/pyenv/versions/3.8.5/bin/jupyter-notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
CMD ["/bin/bash"]
