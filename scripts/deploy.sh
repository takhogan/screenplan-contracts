#!/usr/bin/env bash
# Cascade deploy: push schemas, then trigger each downstream package's own
# deploy script (which refreshes the schemas dep, regenerates types, tests,
# and pushes). Order matters — downstream deploys pull schemas from github,
# so schemas must be on github first.
set -euo pipefail

SCHEMAS_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PACKAGES_DIR="$(cd "$SCHEMAS_DIR/.." && pwd)"
TS_DIR="$PACKAGES_DIR/screenplan-contracts-ts"
PY_DIR="$PACKAGES_DIR/screenplan-contracts-py"

echo "==> [schemas] push"
cd "$SCHEMAS_DIR"
git add -A
if git diff --cached --quiet; then
  echo "[schemas] no changes to commit"
else
  git commit -m "npm run deploy commit $(date '+%Y-%m-%d %H:%M:%S')"
fi
git push origin main

echo "==> [ts] npm run deploy"
cd "$TS_DIR"
npm run deploy

echo "==> [py] make deploy"
cd "$PY_DIR"
make deploy

echo "==> cascade deploy complete"
