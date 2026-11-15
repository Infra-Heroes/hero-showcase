# M-pM-^_M-^WM-^DM-oM-8M-^O Managed Databases Example

This showcase feature shows `[[databases]]` in `hero.toml`: Postgres, MariaDB and Redis next to one app, created by `heroctl deploy`. A microVM runs one image, so each database is a private deployment of its own in the project, with a volume and a generated password; the app receives its connection URL as an environment variable.

## M-pM-^_M-^[M- M-oM-8M-^O Project Structure

- `app.py`: A tiny web server. `GET /check` connects to all three databases, writes a row (or increments a counter) and reports the result as JSON.
- `Dockerfile`: Python image with the three client libraries.
- `hero.toml`: The app plus three `[[databases]]` blocks. The URLs arrive as `DATABASE_URL`, `MYSQL_URL` and `REDIS_URL`.

## M-pM-^_M-^ZM-^@ Deployment & Usage

1. Deploy (creating the databases needs a token with scope `all`, which your normal login has):
   ```bash
   cd features/managed-databases
   heroctl deploy --project default
   ```
2. Open `https://feature-managed-databases.heroapp.run/check`. Every call adds a row to each SQL database and increments the Redis counter.
3. Deploy again: the databases are left alone, so the numbers keep growing. Restart Postgres with `heroctl deployments restart feature-managed-databases-db --project default`; its rows survive.
4. See and remove them:
   ```bash
   heroctl db list --project default
   heroctl db destroy feature-managed-databases-db --project default
   ```

Redis is a cache: it saves snapshots, so a restart can lose recent changes. Postgres and MariaDB keep their data.
