# Contributing to Infra-Heroes Showcase

We'd love your help to grow our collection of examples!

## How to add a new example

1. Create a new folder under `features/` for the capability you want to demonstrate (e.g. `features/my-new-feature`).
2. Add a minimal `hero.toml` configuring the deployment.
3. Add a `Dockerfile` and a simple Python Flask app (`main.py`) that actively showcases the feature via an HTTP endpoint.
4. Update the main `README.md` to include your new example in the "Platform Features" table!

## Pre-commit Hooks
We use `pre-commit` to maintain code quality. Please install it before committing:
```bash
pip install pre-commit
pre-commit install
```
