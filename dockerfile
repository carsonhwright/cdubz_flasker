FROM ubuntu:22.04
ARG TOK
SHELL ["/bin/bash", "-c"]
WORKDIR /root

COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY scripts/.bashrc-template /root/.bashrc
RUN apt-get update && apt install -y vim git net-tools python3 pip iproute2 curl python3.10-venv
RUN git clone https://$TOK@github.com/carsonhwright/cdubz_flasker.git
RUN python3 -m venv .flasker && source .flasker/bin/activate && pip install flask

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]