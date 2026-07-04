# 💤 Scale-to-Zero Example

This showcase feature demonstrates serverless-style scale-to-zero behavior via `scale_to_zero = true` in `hero.toml`.

## 🛠️ Project Structure

- `main.py`: A Flask app that sleeps for 3 seconds during startup to simulate a heavier boot, so a cold start is easy to notice.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `scale_to_zero = true` and `max_replicas = 3`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/scale-to-zero
   heroctl deploy --project default
   ```
2. Leave the service idle for a few minutes so Infra-Heroes scales it down to zero replicas.
3. Send a request to the URL again — you should see roughly a 3-second delay before the page loads, which is the platform resuming the workload from zero. Subsequent requests while it stays warm should be fast.

See [`cold-start-benchmark`](../cold-start-benchmark) for a script that measures this latency numerically instead of by eye.
