FROM ubuntu:22.04
ARG TOK

COPY scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN apt-get update && apt install -y vim git net-tools python3 pip iproute2 curl
RUN cd /root/ && git clone https://$TOK@github.com/carsonhwright/cdubz_flasker.git
RUN python3 -m venv .flasker && source .flasker/bin/activate && pip install flask

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]