# 📈 Autoscaling Example

This showcase feature demonstrates Infra-Heroes's horizontal autoscaling, driven by `min_replicas` and `max_replicas` in `hero.toml`.

## 🛠️ Project Structure

- `main.py`: A Flask app exposing a `/stress` endpoint that busy-loops the CPU for 10 seconds on a background thread.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `min_replicas = 2` and `max_replicas = 10`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/autoscaling
   heroctl deploy --project default
   ```
2. Open the deployed URL and click **"Spike CPU for 10 seconds"** a few times in a row (or hit `/stress` with a load-testing tool).
3. Watch the replica count in `heroctl status` — sustained CPU pressure should scale the service out toward `max_replicas`, and it should scale back down toward `min_replicas` once the spikes stop.
