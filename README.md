# AutoMAX Documentation

Sphinx source for the [AutoMAX](https://github.com/Optimization-AI/AutoMAX) documentation.

## Build locally

```bash
pip install sphinx furo myst-parser sphinx-copybutton
sphinx-build -b html docs docs/_build/html
open docs/_build/html/index.html
```

## Structure

```
docs/
├── conf.py                  # Sphinx configuration
├── index.rst                # Root page
├── intro/
│   ├── quickstart.rst
│   ├── installation.rst
│   ├── configuration.rst
│   ├── automax_search.rst
│   ├── loss_optimizer_pairs.rst
│   ├── hyperparameter_format.rst
│   └── cli_overrides.rst
├── recipes/
│   ├── index.rst
│   ├── auroc.rst
│   ├── auprc.rst
│   ├── opauc.rst
│   └── tpauc.rst
├── api/
│   └── index.rst
└── _static/
    └── custom.css
```

## Deploy

Pushing to `main` triggers the GitHub Actions workflow in
`.github/workflows/docs.yml`, which builds the docs and deploys them to
GitHub Pages automatically.

**One-time setup:** Go to your repo → Settings → Pages → Source → select
**GitHub Actions**.
