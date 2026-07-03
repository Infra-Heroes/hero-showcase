# 🐘 PostgreSQL Database Example

This showcase feature demonstrates running a stateful PostgreSQL database on Infra-Heroes with a persistent volume, injected secrets, and a private TCP health check.

## 🛠️ Project Structure

- `Dockerfile`: Runs the official `postgres:15-alpine` image directly — no application code needed.
- `hero.toml`: Configuration with `private = true`, `health_check_type = "tcp"` against port `5432`, a `[[volumes]]` mount at `/var/lib/postgresql/data`, and `POSTGRES_PASSWORD` injected via `secret:DB_PASS`.

## 🚀 Deployment & Usage

1. Set the `DB_PASS` secret for the project (see the [`secrets`](../secrets) example for how secret injection works):
   ```bash
   heroctl secrets set DB_PASS=<your-password> --project default
   ```
2. Deploy the database:
   ```bash
   cd features/database-postgres
   heroctl deploy --project default
   ```
3. From another private-networked service in the project, connect at `database-postgres:5432` with user `hero`, database `herodb`, and the password you set.
4. Redeploy or restart the service and confirm data persists across restarts, thanks to the `pg-data` volume mount.
