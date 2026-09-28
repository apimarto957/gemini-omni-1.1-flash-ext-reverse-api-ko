#!/usr/bin/env bash
set -euo pipefail
: "${APIMART_KEY:?set APIMART_KEY}"

curl -sS -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer $APIMART_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model":"Omni-Flash-Ext","prompt":"a girl dancing in a sunny garden","duration":10,"resolution":"1080p","aspect_ratio":"9:16"}}'
