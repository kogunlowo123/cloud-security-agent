#!/bin/bash
set -euo pipefail
echo "Setting up Cloud Security Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
