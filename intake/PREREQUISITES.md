# Prerequisites

Before starting OCTALUM-PYLAB, ensure you have the following:

## Required

### Python 3.10+

```bash
# Check your Python version
python --version
# Should show Python 3.10.x or higher
```

If you need to install Python:
- **Windows**: [python.org/downloads](https://www.python.org/downloads/)
- **macOS**: `brew install python@3.12`
- **Linux**: `sudo apt install python3.12`

### Git

```bash
# Check Git installation
git --version
```

Install from [git-scm.com](https://git-scm.com/)

### Code Editor

**Recommended**: Visual Studio Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension
3. Install the Ruff extension

## Recommended

### Package Manager: uv

Fast Python package manager (10-100x faster than pip):

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### VS Code Extensions

| Extension | Purpose |
|-----------|---------|
| Python | Language support |
| Pylance | Type checking |
| Ruff | Linting & formatting |
| Even Better TOML | pyproject.toml support |
| Markdown All in One | README preview |

## Knowledge Prerequisites

### Minimum (Phase 1)

- Basic computer literacy
- Understanding of files and directories
- Ability to run commands in terminal

### Recommended (Phase 2+)

- Basic programming concepts (variables, functions)
- Understanding of control flow (if/else, loops)
- Familiarity with command line

## Hardware Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| RAM | 4 GB | 8 GB+ |
| Storage | 1 GB | 5 GB+ |
| Internet | Required for setup | Broadband |

## Account Requirements

- **GitHub** — For Codespaces and contributions
- **LeetCode** — For practice problems (free account)

## Quick Check

Run this command to verify your setup:

```bash
python --version && git --version && code --version
```

All three should output version numbers.

---

*Ready? Proceed to [Installation](INSTALLATION.md)*
