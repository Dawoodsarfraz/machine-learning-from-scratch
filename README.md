# Machine Learning From Scratch

A learning-focused repository where machine learning algorithms and the mathematics behind them are implemented **from first principles**, without relying on high-level ML libraries. The goal is to understand *why* each algorithm works, not just how to call it.

## Goals

- Build a deep, intuitive understanding of core ML concepts.
- Implement algorithms step by step using only fundamental tools (e.g., NumPy).
- Connect the underlying math (probability, linear algebra, calculus, optimization) to working code.
- Document trade-offs, assumptions, edge cases, and common misconceptions.

## Topics (planned)

- Probability and statistics foundations (conditional probability, Bayes' rule, independence)
- Linear regression and gradient descent
- Logistic regression
- k-Nearest Neighbors
- Naive Bayes
- Decision trees and ensembles
- k-Means clustering
- Neural networks and backpropagation

> This list will grow as the repository evolves.

## Run in Google Colab

No local setup is needed. Click a badge to open the notebook directly in Google Colab.

| Notebook | Open in Colab |
|---|---|
| K-Nearest Neighbours | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Dawoodsarfraz/machine-learning-from-scratch/blob/main/k-nearest-neighbours/k-nearest-neighbours.ipynb) |
| Decision Tree | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Dawoodsarfraz/machine-learning-from-scratch/blob/main/decision-tree/decision-tree.ipynb) |

Colab already includes NumPy and Matplotlib. If a notebook needs another package, add a cell at the top:

```python
!pip install <package-name>
```

## Platform Support

This project was developed and tested on **Ubuntu (Linux)**, where it is known to work. It has **not been tested on Windows or macOS**, so you may run into platform-specific issues there (for example, path separators, shell commands, or package builds).

**Found a problem on Windows or macOS?** Contributions are welcome. Please open an issue, or better, submit a pull request that fixes the problem or updates this README with the correct instructions. See [Contributing](#contributing) below.

Commands that differ by platform:

| Task | Ubuntu / Linux | | |
|---|---|---|---|
| Install `uv` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Activate environment (optional) | `source .venv/bin/activate` |
| View folder contents | `ls` |

`git clone`, `uv sync`, and `uv run` use the same syntax on every platform. Windows and macOS rows above come from the official `uv` documentation and are **untested for this project**.

## Prerequisites

- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/) (fast Python package and project manager)

Install `uv` if you do not have it (Ubuntu / Linux; see [Platform Support](#platform-support) for other systems):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/Dawoodsarfraz/machine-learning-from-scratch.git
cd machine-learning-from-scratch

# 2. Install the exact dependencies and Python version
uv sync

# 3. Run code
uv run main.py
```

`uv sync` creates the virtual environment (`.venv/`) automatically and installs the locked dependencies from `pyproject.toml` and `uv.lock`. You can optionally activate the environment with:

```bash
source .venv/bin/activate
```

### Python is installed for you

You do **not** need to install Python or tools such as `pyenv` beforehand. If the Python version required by this project (see `.python-version` and `pyproject.toml`) is not found on your machine, `uv` downloads and installs it automatically during `uv sync` or `uv run`. An internet connection is required for the first run.

To manage Python versions manually with `uv`:

```bash
uv python list              # show available and installed versions
uv python install 3.12      # install a specific version
```

## Project Structure

```text
machine-learning-from-scratch/
├── .gitignore            # Files Git should ignore
├── .python-version       # Pinned Python version
├── ref-material/         # Reference books and study material
├── decision-tree/        # Decision tree implementation and notebook
├── k-nearest-neighbours/ # k-NN implementation and notebook
├── main.py               # Entry point
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock               # Locked dependency versions
└── README.md             # This file
```

| File | Purpose |
|---|---|
| `.python-version` | Python version used by this project, so `uv` selects the same interpreter everywhere. |
| `pyproject.toml` | Project name, version, required Python version, and dependencies. |
| `uv.lock` | Exact resolved versions of every dependency for reproducible installs. |
| `main.py` | Starter script. |

Each algorithm lives in its own folder (currently `k-nearest-neighbours/` and `decision-tree/`; more will follow) with code, notes, and a notebook.

## Contributing

This is a personal learning project. Suggestions, corrections, and issues are welcome.

To contribute, especially to fix Windows or macOS issues:

1. Fork the repository on GitHub.
2. Create a branch: `git checkout -b fix/windows-setup`
3. Make your change (for example, update this `README.md` with working instructions for your platform).
4. Commit and push: `git commit -m "Fix Windows setup instructions"` then `git push origin fix/windows-setup`
5. Open a pull request describing your operating system, the problem you hit, and how your change fixes it.

## Author

Email: [dawoodsarfraz.cs@gmail.com](mailto:dawoodsarfraz.cs@gmail.com)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Dawoodsarfraz/machine-learning-from-scratch?tab=MIT-1-ov-file)