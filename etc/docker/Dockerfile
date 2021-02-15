# explicitly use Debian for maximum cross-architecture compatibility
FROM debian:buster-slim

RUN set -eux;                                                   \
	      apt-get update;                                         \
	      apt-get install -y --no-install-recommends              \
                ca-certificates                                 \
                curl                                            \
                python3.7                                       \
                python3-setuptools                              \
                python3-pip                                     \
                python3-wheel                                   \
                file;                                           \
    rm -rf /var/lib/apt/lists/*;


WORKDIR /opt/is
COPY src/ src
COPY etc/conf/options.json options.json
COPY setup.py . 
RUN pip3 install .
CMD ["is-tester-multiarch-rpc"]