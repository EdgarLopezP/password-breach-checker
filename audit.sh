#!/usr/bin/env bash
set -euo pipefail

echo "=== STATUS (Git) ==="
git status -sb || true
echo

echo "=== REMOTO ==="
git remote -v || true
echo

echo "=== WORKFLOWS (GitHub Actions) ==="
if [ -d ".github/workflows" ]; then
  ls -R .github/workflows
else
  echo "No workflows encontrados"
fi
echo

echo "=== TESTS (pytest) ==="
PYTHONPATH=. pytest -q || echo "⚠️ Tests fallaron"
echo

echo "=== ESTRUCTURA DEL PROYECTO (3 niveles) ==="
if command -v tree >/dev/null 2>&1; then
  tree -L 3
else
  echo "(sin 'tree') mostrando con 'find':"
  find . -maxdepth 3 -print | sed 's|^\./||'
fi
