<p align="center">
  <a href="https://github.com/Harery/OCTALUM-PYLAB">
    <img src="https://img.shields.io/badge/OCTALUM--PYLAB-8%20Phases%20of%20Mastery-blue?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a2e" alt="OCTALUM-PYLAB">
  </a>
</p>

<h1 align="center">
  <pre>
  ██████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗███████╗██╗      ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██╔═══██╗██╔════╝██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     ██║   ██║█████╗  ███████║██╔████╔██║█████╗  ██║     ██║     ██║   ██║██║  ██║█████╗
██║     ██║   ██║██╔══╝  ██╔══██║██║╚██╔╝██║██╔══╝  ██║     ██║     ██║   ██║██║  ██║██╔══╝
╚██████╗╚██████╔╝███████╗██║  ██║██║ ╚═╝ ██║███████╗███████╗╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗
██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██║
██████╔╝██║   ██║███████║██████╔╝██████╔╝██║
██╔═══╝ ██║   ██║██╔══██║██╔══██╗██╔══██╗██║
██║     ╚██████╔╝██║  ██║██████╔╝██████╔╝███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝
  </pre>
</h1>

<p align="center">
  <em>Master Python Data Structures & Algorithms Through Guided Experimentation</em>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3120/">
    <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="https://docs.astral.sh/ruff/">
    <img src="https://img.shields.io/badge/Linter-Ruff-orange?logo=python&logoColor=white" alt="Ruff">
  </a>
  <a href="https://docs.pytest.org/">
    <img src="https://img.shields.io/badge/Testing-Pytest-green?logo=pytest&logoColor=white" alt="Pytest">
  </a>
  <a href="https://github.com/Harery/OCTALUM-PYLAB/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL%20v3-blue" alt="License">
  </a>
  <a href="https://github.com/Harery/OCTALUM-PYLAB/stargazers">
    <img src="https://img.shields.io/github/stars/Harery/OCTALUM-PYLAB?style=flat&logo=github&label=Stars" alt="GitHub Stars">
  </a>
  <a href="https://github.com/Harery/OCTALUM-PYLAB/actions/workflows/ci.yml">
    <img src="https://github.com/Harery/OCTALUM-PYLAB/actions/workflows/ci.yml/badge.svg" alt="CI Status">
  </a>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-learning-path">Learning Path</a> •
  <a href="#-directory-structure">Structure</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 **8-Phase Learning Path**
Structured progression from Python basics to advanced algorithms. Each phase builds on the previous, ensuring solid foundations before moving to complex topics.

</td>
<td width="50%">

### 🧩 **Pattern-Based Learning**
Master 15+ coding patterns (Sliding Window, Two Pointers, Fast & Slow, etc.) that solve 80% of LeetCode problems.

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Progress Tracking**
Gamified learning with XP points, streaks, achievements, and visual progress indicators. Track your journey from beginner to expert.

</td>
<td width="50%">

### 🎬 **Visual Algorithm Animations**
Watch algorithms come to life with Manim-powered visualizations. Perfect for understanding complex concepts.

</td>
</tr>
<tr>
<td width="50%">

### 🏆 **LeetCode Integration**
Structured challenges organized by difficulty with hints, solutions, and optimal approaches for 300+ problems.

</td>
<td width="50%">

### 🚀 **One-Click Setup**
Start coding in seconds with GitHub Codespaces. Fully configured dev environment with all tools pre-installed.

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Harery/OCTALUM-PYLAB?quickstart=1)

Click the button above to launch a fully configured development environment in your browser. No installation required!

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/Harery/OCTALUM-PYLAB.git
cd OCTALUM-PYLAB

# Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install --install-hooks

# Run the learning tracker
uv run python -m pylab.track

# Start coding!
uv run python build/foundations/01-python-basics/hello.py
```

### Verify Installation

```bash
# Run tests
uv run pytest verify/tests -v

# Run linter
uv run ruff check .

# Run type checker
uv run pyright build/
```

---

## 📚 Learning Path

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                         OCTALUM-PYLAB 8-PHASE JOURNEY                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Phase 1: FOUNDATIONS          Phase 5: PATTERNS                             ║
║  ├── Python Basics            ├── Sliding Window                             ║
║  ├── Control Flow             ├── Two Pointers                               ║
║  └── Functions                ├── Fast & Slow Pointers                       ║
║       ↓                            ├── Merge Intervals                        ║
║                                    └── Cyclic Sort                            ║
║  Phase 2: DATA STRUCTURES           ↓                                         ║
║  ├── Arrays & Lists                                                     ║
║  ├── Strings                  Phase 6: ALGORITHMS                            ║
║  ├── Hash Tables              ├── Searching                                  ║
║  ├── Linked Lists             ├── Sorting                                    ║
║  ├── Stacks & Queues          ├── Recursion                                  ║
║  ├── Trees                    └── Dynamic Programming                        ║
║  └── Graphs                        ↓                                         ║
║       ↓                                                                   ║
║                                Phase 7: CHALLENGES                           ║
║  Phase 3: ALGORITHMS           ├── LeetCode Easy                             ║
║  ├── Searching                 ├── LeetCode Medium                           ║
║  ├── Sorting                   ├── LeetCode Hard                             ║
║  └── Recursion                 └── System Design                             ║
║       ↓                            ↓                                         ║
║                                                                              ║
║  Phase 4: ADVANCED DS          Phase 8: MASTERY                              ║
║  ├── Heaps                    ├── Optimize Solutions                         ║
║  ├── Trie                     ├── Mock Interviews                           ║
║  ├── Segment Trees             └── Real-world Projects                       ║
║  └── Disjoint Sets                                                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### Phase Details

| Phase | Focus | Topics | Est. Time |
|-------|-------|--------|-----------|
| **1** | Foundations | Python basics, control flow, functions | 2 weeks |
| **2** | Data Structures | Arrays, strings, hash tables, linked lists, trees, graphs | 4 weeks |
| **3** | Basic Algorithms | Searching, sorting, recursion | 3 weeks |
| **4** | Advanced DS | Heaps, trie, segment trees, disjoint sets | 3 weeks |
| **5** | Patterns | 15+ coding patterns for interviews | 4 weeks |
| **6** | Advanced Algorithms | DP, graph algorithms, greedy | 4 weeks |
| **7** | Challenges | 300+ LeetCode problems | Ongoing |
| **8** | Mastery | Optimization, mock interviews, projects | Ongoing |

---

## 📁 Directory Structure

```
OCTALUM-PYLAB/
├── 📥 intake/                 # Getting started & onboarding
│   └── README.md
│
├── 🏗️ build/                  # Core learning content
│   ├── foundations/           # Phase 1: Python fundamentals
│   │   ├── 01-python-basics/
│   │   ├── 02-control-flow/
│   │   └── 03-functions/
│   ├── data-structures/       # Phase 2-4: DS implementations
│   │   ├── 01-arrays-lists/
│   │   ├── 02-strings/
│   │   ├── 03-hash-tables/
│   │   ├── 04-linked-lists/
│   │   ├── 05-stacks-queues/
│   │   ├── 06-trees/
│   │   ├── 07-graphs/
│   │   └── 08-advanced/
│   ├── algorithms/            # Phase 3, 6: Algorithm implementations
│   │   ├── 01-searching/
│   │   ├── 02-sorting/
│   │   ├── 03-recursion/
│   │   ├── 04-dynamic-programming/
│   │   ├── 05-graph-algorithms/
│   │   ├── 06-greedy/
│   │   └── 07-string-algorithms/
│   ├── patterns/              # Phase 5: Coding patterns
│   │   ├── sliding-window/
│   │   ├── two-pointers/
│   │   ├── fast-slow-pointers/
│   │   ├── merge-intervals/
│   │   ├── cyclic-sort/
│   │   └── ... (10+ more)
│   └── challenges/            # Phase 7: LeetCode problems
│       ├── leetcode-easy/
│       ├── leetcode-medium/
│       ├── leetcode-hard/
│       └── system-design/
│
├── 🔬 verify/                 # Testing & quality assurance
│   ├── tests/                 # Test suites
│   └── coverage/              # Coverage reports
│
├── 🚀 ship/                   # Deployment & tooling
│   ├── .devcontainer/         # GitHub Codespaces config
│   ├── docker/                # Docker configurations
│   └── scripts/               # Utility scripts
│
├── 📚 learn/                  # Resources & visualizations
│   ├── cheatsheets/           # Quick reference guides
│   ├── notebooks/             # Jupyter notebooks
│   └── visualizations/        # Algorithm animations
│
├── 📜 record/                 # Documentation
│   └── docs/                  # MkDocs source
│
├── 🔐 govern/                 # Security & compliance
│
├── .github/                   # GitHub configurations
│   ├── workflows/             # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── pyproject.toml             # Project configuration
├── .python-version            # Python version (3.12)
└── README.md                  # This file
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Contribution Steps

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feat/amazing-feature`)
3. **Commit** your changes using conventional commits
4. **Push** to your branch
5. **Open** a Pull Request

### Code Style

This project uses:
- **Ruff** for linting and formatting
- **Pyright** for type checking
- **Pytest** for testing

```bash
# Format code
uv run ruff format .

# Check linting
uv run ruff check .

# Type check
uv run pyright build/

# Run tests
uv run pytest verify/tests -v
```

---

## 📈 Progress & Stats

| Metric | Count |
|--------|-------|
| 📝 Learning Modules | 50+ |
| 🧩 Coding Patterns | 15+ |
| 🏆 LeetCode Problems | 300+ |
| 📊 Visual Animations | 100+ |
| ✅ Test Coverage | Growing |

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

```
OCTALUM-PYLAB - Master Python Data Structures & Algorithms
Copyright (C) 2026 OCTALUME

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

---

## 🙏 Acknowledgments

- **Python Software Foundation** for the amazing language
- **LeetCode** for the problem platform
- **Design Gurus** for pattern-based learning inspiration
- **The Open Source Community** for continuous support

---

<p align="center">
  <a href="https://github.com/Harery/OCTALUM-PYLAB">
    <img src="https://img.shields.io/badge/Powered%20By-OCTALUME-8A2BE2?style=for-the-badge" alt="Powered by OCTALUME">
  </a>
</p>

<p align="center">
  <i>Bringing Light to Every Phase of Development</i>
</p>

<p align="center">
  <a href="https://github.com/Harery/OCTALUM-PYLAB/issues">Report Bug</a> •
  <a href="https://github.com/Harery/OCTALUM-PYLAB/issues">Request Feature</a> •
  <a href="https://github.com/Harery/OCTALUM-PYLAB/discussions">Discussions</a>
</p>

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/Harery">OCTALUME</a>
</p>
