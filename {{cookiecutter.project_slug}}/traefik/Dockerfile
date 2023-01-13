FROM traefik:v2.2.11
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
ARG BUILD_ENVIRONMENT
COPY ./traefik/traefik_${BUILD_ENVIRONMENT}.yml /etc/traefik/traefik.yml
