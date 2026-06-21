# Contributing to Infra-Heroes Showcase

We'd love your help to grow our collection of examples!

## How to add a new example

1. Choose the language folder under `apps/` (or create a new one).
2. Create a folder for your framework or app type (e.g. `apps/go/go-fiber`).
3. Add a minimal `hero.toml` configuring the app deployment.
4. Add a `Dockerfile`.
5. Update the main `README.md` to include your new example in the list!

## Pre-commit Hooks
We use `pre-commit` to maintain code quality. Please install it before committing:
```bash
pip install pre-commit
pre-commit install
```
