#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_asns/ tests/

black democritus_asns/ tests/

mypy democritus_asns/ tests/

pylint --fail-under 9 democritus_asns/*.py

flake8 democritus_asns/ tests/

bandit -r democritus_asns/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_asns/ tests/
