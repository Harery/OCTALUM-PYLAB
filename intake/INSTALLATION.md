# Installation Guide

Set up your OCTALUM-PYLAB development environment.

## Option 1: GitHub Codespaces (Recommended)

The fastest way to start — no local installation required!

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Harery/OCTALUM-PYLAB)

1. Click the button above
2. Sign in to GitHub (if not already)
3. Wait for environment to provision (~2 minutes)
4. Start coding!

**What's included:**
- Python 3.12
- All extensions pre-installed
- Pre-commit hooks configured
- Ready to run tests

---

## Option 2: Local Development

### Step 1: Clone the Repository

```bash
git clone https://github.com/Harery/OCTALUM-PYLAB.git
cd OCTALUM-PYLAB
```

### Step 2: Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

### Step 3: Create Virtual Environment

```bash
# Create venv and install all dependencies
uv sync --all-extras
```

### Step 4: Install Pre-commit Hooks

```bash
uv run pre-commit install --install-hooks
```

### Step 5: Verify Installation

```bash
# Check Python
uv run python --version

# Run tests
uv run pytest verify/tests -v

# Check linting
uv run ruff check .

# Check types
uv run pyright build/
```

---

## Option 3: Docker (Advanced)

```bash
# Build the image
docker build -t octalum-pylab -f ship/docker/Dockerfile .

# Run container
docker run -it -v $(pwd):/app octalum-pylab
```

---

## Post-Installation

### Configure Git

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Enable Shell Completion (uv)

```bash
# Add to your shell config (~/.bashrc, ~/.zshrc, etc.)
eval "$(uv generate-shell-completion bash)"  # or zsh, fish
```

### VS Code Settings

Recommended settings are included in `.vscode/settings.json`. To use:

1. Open project in VS Code
2. When prompted, install recommended extensions
3. Settings will be applied automatically

---

## Troubleshooting

### "uv: command not found"

Add uv to your PATH:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"
```

### "Python version mismatch"

Ensure Python 3.10+ is installed:

```bash
# Check available Python versions
uv python list

# Install Python 3.12
uv python install 3.12
```

### "Permission denied"

On Unix systems, you may need:

```bash
chmod +x .githooks/*
```

### Tests failing

1. Ensure all dependencies are installed: `uv sync --all-extras`
2. Clear cache: `uv cache clean`
3. Reinstall: `rm -rf .venv && uv sync`

---

## Next Steps

1. Read the [Roadmap](ROADMAP.md) to understand the learning path
2. Check out [PROGRESS.md](../PROGRESS.md) to track your journey
3. Start with Phase 1 in `build/foundations/`

---

*Questions? [Open a discussion](https://github.com/Harery/OCTALUM-PYLAB/discussions)*
