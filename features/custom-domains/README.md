# 🌐 Custom Domains Example

This showcase feature demonstrates routing traffic to an Infra-Heroes service via custom CNAMEs, configured through `custom_domains` in `hero.toml`.

## 🛠️ Project Structure

- `main.py`: A Flask app that renders the `Host` header of the incoming request, so you can confirm which domain served the request.
- `Dockerfile` & `requirements.txt`: Container build for the app.
- `hero.toml`: Configuration with `custom_domains = ["api.example.com", "app.example.com"]`.

## 🚀 Deployment & Usage

1. Deploy the app:
   ```bash
   cd features/custom-domains
   heroctl deploy --project default
   ```
2. Point a CNAME for your own domain (instead of the placeholder `api.example.com` / `app.example.com`) at the hostname `heroctl` prints after deploy.
3. Visit your domain — the page should echo back the `Host` header you connected with, confirming the custom domain routed correctly through the platform's load balancer.
