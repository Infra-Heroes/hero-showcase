# 🔒 Private Service Example

This showcase feature demonstrates internal-only networking on Infra-Heroes using `private = true`, which keeps a service off the public load balancer.

## 🛠️ Project Structure

- `main.py`: A Flask app that reports the caller's `remote_addr` and `X-Forwarded-For` header, useful for confirming how traffic reaches the service.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `private = true` and an HTTP health check at `/health`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/private-service
   heroctl deploy --project default
   ```
2. Confirm `heroctl deploy` does **not** return a public URL for this service — that's expected, since `private = true` removes it from the public load balancer.
3. From another service in the same project, curl it over the internal network at `private-service:8080` and confirm you get a response, proving the service is reachable internally even though it has no public endpoint.
