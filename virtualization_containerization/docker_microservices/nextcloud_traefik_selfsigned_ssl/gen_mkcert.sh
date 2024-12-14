#!/bin/sh
# If it's the firt install of mkcert, run
mkcert -install

# Generate certificate for domain "docker.localhost", "domain.local" and their sub-domains
mkcert -cert-file certs/local-cert.pem -key-file certs/local-key.pem "*.localhost" "traefik.localhost" "nextcloud.localhost" "*.nextcloud.localhost" "whoami.localhost"