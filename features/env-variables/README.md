# 🔧 Environment Variables Example

This showcase feature demonstrates configuring static environment variables for a service through the `[env]` table in `hero.toml`.

## 🛠️ Project Structure

- `main.py`: A Flask app that lists every environment variable visible to the process in an HTML table.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `[env]` setting `LOG_LEVEL = "debug"` and `ENVIRONMENT = "production"`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/env-variables
   heroctl deploy --project default
   ```
2. Open the deployed URL — the table should show `LOG_LEVEL=debug` and `ENVIRONMENT=production` alongside the container's other default environment variables, confirming `hero.toml`'s `[env]` values were injected at runtime.
