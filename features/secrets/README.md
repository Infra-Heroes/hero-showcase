# 🔑 Secrets Example

This showcase feature demonstrates injecting sensitive values into a service using the `secret:KEY` syntax in `hero.toml`, instead of hardcoding secrets in the config. <!-- pragma: allowlist secret -->

## 🛠️ Project Structure

- `main.py`: A Flask app that reads `API_KEY` and `DB_PASS` from the environment and reports whether they were resolved to real values or are still the raw `secret:KEY` placeholder.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `API_KEY = "secret:API_KEY"` and `DB_PASS = "secret:DB_PASS"` under `[env]`. <!-- pragma: allowlist secret -->

## 🚀 Deployment & Usage

1. Set the referenced secrets for the project:
   ```bash
   heroctl secrets set API_KEY=<your-api-key> DB_PASS=<your-db-password> --project default
   ```
2. Deploy the app:
   ```bash
   cd features/secrets
   heroctl deploy --project default
   ```
3. Open the deployed URL — it should show **"Vault Status: UNLOCKED"** with your real secret values, confirming Infra-Heroes resolved the `secret:KEY` references at deploy time. If you skip step 1, it reports **"LOCKED"** since the raw placeholder strings are never substituted.
