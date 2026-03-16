# Installation

Follow these steps to set up OCTALUM-PYLAB on your machine.

## Option 1: Using pip

```bash
# Clone the repository
git clone https://github.com/Harery/OCTALUM-PYLAB.git
cd OCTALUM-PYLAB

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

## Option 2: Using uv (Recommended)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/Harery/OCTALUM-PYLAB.git
cd OCTALUM-PYLAB

# Sync dependencies
uv sync --all-extras
```

## Option 3: GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Harery/OCTALUM-PYLAB)

Click the button above for an instant, pre-configured environment.

## Verify Installation

```bash
# Run tests
pytest verify/tests -v

# Run linter
ruff check .

# Run type checker
pyright build/

# Run learning tracker
python -m pylab.track
```

## Project Structure

```
OCTALUM-PYLAB/
├── build/           # Learning content (implementations)
├── verify/          # Tests and coverage
├── learn/           # Notebooks and resources
├── ship/            # Scripts and tools
├── record/          # Documentation
└── pyproject.toml   # Project configuration
```

## Troubleshooting

### Common Issues

1. **pip not found**
   ```bash
   python -m ensurepip --upgrade
   ```

2. **Permission denied**
   ```bash
   pip install -e ".[dev]" --user
   ```

3. **Tests failing**
   ```bash
   pip install pytest pytest-cov -U
   ```

## Next Steps

- [Roadmap](roadmap.md) - See the complete learning path
