#!/usr/bin/env bash

set -e

# Download OpenAPI spec for sports rest app
curl -o openapi/sports_app.json "https://hbl-cloud.kinexon.com/api-doc/sport-app"
# Download OpenAPI spec for statistics center
curl -o openapi/statistics_center.json "https://hbl-cloud.kinexon.com/api-doc/51-statistics-center"

# Set variables
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENDOR_DIR="$ROOT/src/_vendor"

# Activate virtual environment
VENV_PATH="$ROOT/.venv"
ACTIVATE_SCRIPT="$VENV_PATH/bin/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    source "$ACTIVATE_SCRIPT"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

# ── sports_app ────────────────────────────────────────────────────────────────
TARGET_SPORTS="$VENDOR_DIR/kinexon_client"
rm -rf "$TARGET_SPORTS"

python scripts/rename_operation_ids.py

openapi-python-client generate --path "openapi/sports_app.json" --config "openapi/config.yaml"
mkdir -p "$VENDOR_DIR"
mv "$ROOT/kinexon-client/kinexon_client" "$TARGET_SPORTS"
rm -rf "$ROOT/kinexon-client"
echo "sports_app client regenerated at $TARGET_SPORTS"

# ── statistics_center ─────────────────────────────────────────────────────────
TARGET_SC="$VENDOR_DIR/statistics_center_client"
rm -rf "$TARGET_SC"

# Strip non-HTTP paths and fix self-referential allOf schemas
python - <<'PYEOF'
import json

spec = json.load(open("openapi/statistics_center.json"))

# Drop ws:// and other non-HTTP paths
spec["paths"] = {p: v for p, v in spec["paths"].items() if p.startswith("/")}

# Fix schemas that use allOf only to reference themselves (malformed spec pattern)
for name, schema in spec.get("components", {}).get("schemas", {}).items():
    allof = schema.get("allOf")
    if not isinstance(allof, list):
        continue
    # Collect non-self-referencing parts
    parts = [
        p for p in allof
        if not (isinstance(p, dict) and p.get("$ref") == f"#/components/schemas/{name}")
    ]
    if len(parts) == 1 and "properties" in parts[0]:
        schema.pop("allOf")
        schema["properties"] = parts[0]["properties"]
    elif len(parts) == 0:
        schema.pop("allOf")

json.dump(spec, open("openapi/statistics_center_clean.json", "w"), indent=2)
PYEOF

openapi-python-client generate --path "openapi/statistics_center_clean.json" --config "openapi/statistics_center_config.yaml"
mv "$ROOT/statistics-center-client/statistics_center_client" "$TARGET_SC"
rm -rf "$ROOT/statistics-center-client" openapi/statistics_center_clean.json
echo "statistics_center client regenerated at $TARGET_SC"
