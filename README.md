<div align="center">

# 🌟 Infra-Heroes App Showcase

**A curated collection of deployment-ready examples for the Infra-Heroes PaaS.**

[![Validate](https://github.com/Infra-Heroes/hero-showcase/actions/workflows/validate.yml/badge.svg)](https://github.com/Infra-Heroes/hero-showcase/actions/workflows/validate.yml)
[![status-badge](https://woodpecker.infra-heroes.de/api/badges/InfraHeroes/showcase/status.svg)](https://woodpecker.infra-heroes.de/repos/InfraHeroes/showcase)

This repository provides boilerplate code and configurations (`hero.toml`) to get your applications running on Infra-Heroes in seconds. Whether you're building a static frontend or a robust backend API, you'll find a starting point here.

[Explore Infra-Heroes](https://www.infra-heroes.de) • [Documentation](https://www.infra-heroes.de/docs) • [heroctl CLI](https://github.com/Infra-Heroes/heroctl)

</div>

---

## 📑 Table of Contents

- [Platform Features](#-platform-features)
- [Usage & Deployment](#-usage--deployment)
- [Validate Your Config](#-validate-your-config)

---

## 🛠️ Platform Features

Explore Infra-Heroes's powerful deployment features through these minimal configuration examples. These examples demonstrate the core capabilities of the `hero.toml` configuration file.

| Feature | Example Path | Description |
| :--- | :--- | :--- |
| **Volumes** | [`/features/volumes`](./features/volumes) | Demonstrates persistent storage mounts via `[[volumes]]`. |
| **Secrets** | [`/features/secrets`](./features/secrets) | Demonstrates injecting sensitive data using `secret:KEY`. |
| **Environment Variables** | [`/features/env-variables`](./features/env-variables) | Demonstrates configuring static environment variables. |
| **Autoscaling** | [`/features/autoscaling`](./features/autoscaling) | Demonstrates scale-out behavior using `min_replicas` and `max_replicas`. |
| **Scale to Zero** | [`/features/scale-to-zero`](./features/scale-to-zero) | Demonstrates serverless cold-start capability with `scale_to_zero = true`. |
| **Cold Start Benchmark** | [`/features/cold-start-benchmark`](./features/cold-start-benchmark) | Benchmark suite to measure cold starts and request latencies. |
| **Private Services** | [`/features/private-service`](./features/private-service) | Demonstrates internal-only networking using `private = true`. |
| **Custom Domains** | [`/features/custom-domains`](./features/custom-domains) | Demonstrates custom CNAMEs via `custom_domains`. |
| **Database (PostgreSQL)** | [`/features/database-postgres`](./features/database-postgres) | Demonstrates running a Postgres database with persistent volumes and secrets. |
| **Cache (Redis)** | [`/features/cache-redis`](./features/cache-redis) | Demonstrates running a private Redis cache using TCP healthchecks. |



---

## 🚀 Usage & Deployment

Deploying any of these examples is as simple as using the `heroctl` CLI!

1. **Install the CLI**:
   ```bash
   brew install Infra-Heroes/tap/heroctl
   # or download from GitHub releases
   ```

2. **Login to your account**:
   ```bash
   heroctl login
   ```

3. **Deploy the app**:
   Navigate to the example directory you want to deploy, and run:
   ```bash
   cd go-http
   heroctl deploy
   ```

That's it! `heroctl` will read the `hero.toml` file, package the context, and stream the build and deployment logs directly to your terminal.

---

## 🛡️ Validate Your Config

You can check if your `hero.toml` syntax is correct at any time using the local validation tool:

```bash
heroctl validate
```

We also provide a **GitHub Action** to automatically validate your configurations in your CI/CD pipelines! Add this to your `.github/workflows/validate.yml`:

```yaml
name: Validate hero.toml
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate hero.toml
        uses: Infra-Heroes/heroctl@main
        with:
          config_path: "hero.toml"
```
