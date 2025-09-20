#!/usr/bin/env bash

set -e

# Download OpenAPI spec
curl -o openapi/sports_app.json "https://hbl-cloud.kinexon.com/api-doc/sport-app"

# Set variables
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GEN_OUT="$ROOT/kinexon-client"
GEN_PKG="$GEN_OUT/kinexon_client"
VENDOR_DIR="$ROOT/src/_vendor"
TARGET="$VENDOR_DIR/kinexon_client"

# Clean previous vendor
if [ -d "$TARGET" ]; then
    rm -rf "$TARGET"
fi

# Activate virtual environment
VENV_PATH="$ROOT/.venv"
ACTIVATE_SCRIPT="$VENV_PATH/bin/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    source "$ACTIVATE_SCRIPT"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

# Run generator
openapi-python-client generate --path "openapi/sports_app.json" --config "openapi/config.yaml"

# Move generated code
mkdir -p "$VENDOR_DIR"
mv "$GEN_PKG" "$TARGET"

# Remove temporary folder
if [ -d "$GEN_OUT" ]; then
    rm -rf "$GEN_OUT"
fi

echo "Client regenerated at $TARGET"
