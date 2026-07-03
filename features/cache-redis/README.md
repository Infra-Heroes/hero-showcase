# 🧠 Redis Cache Example

This showcase feature demonstrates running a private, internal-only cache service on Infra-Heroes using a stock `redis:7-alpine` image and a TCP health check.

## 🛠️ Project Structure

- `Dockerfile`: Runs the official `redis:7-alpine` image directly — no application code needed.
- `hero.toml`: Configuration with `private = true` and `health_check_type = "tcp"` against port `6379`.

## 🚀 Deployment & Usage

1. Deploy the service:
   ```bash
   cd features/cache-redis
   heroctl deploy --project default
   ```
2. Because `private = true`, the service is only reachable from other services in the same project over the internal network — it will not get a public URL.
3. From another private-networked service in the project, connect with any Redis client at `cache-redis:6379` (service name resolves via internal DNS) and confirm reads/writes work, e.g.:
   ```bash
   redis-cli -h cache-redis -p 6379 ping
   ```
