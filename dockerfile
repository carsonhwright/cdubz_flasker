FROM ubuntu:22.04
ARG TOK

RUN apt-get update && apt install -y vim git net-tools python3 pip iproute2 curl
RUN cd /root/ && git clone https://$TOK@github.com/carsonhwright/cdubz_flasker.git