<div align="center">

# 🌟 Infra-Heroes App Showcase

**A curated collection of deployment-ready examples for the Infra-Heroes PaaS.**

[![Validate](https://github.com/Infra-Heroes/showcase/actions/workflows/validate.yml/badge.svg)](https://github.com/Infra-Heroes/showcase/actions/workflows/validate.yml)

This repository provides boilerplate code and configurations (`hero.toml`) to get your applications running on Infra-Heroes in seconds. Whether you're building a static frontend or a robust backend API, you'll find a starting point here.

[Explore Infra-Heroes](https://www.infra-heroes.de) • [Documentation](https://www.infra-heroes.de/docs) • [heroctl CLI](https://github.com/Infra-Heroes/heroctl)

</div>

---

## 📑 Table of Contents

- [Frontend & Static Sites](#-frontend--static-sites)
- [Backend & APIs](#-backend--apis)
- [Usage & Deployment](#-usage--deployment)
- [Validate Your Config](#-validate-your-config)

---

## 🎨 Frontend & Static Sites

Deploy high-performance web applications and static sites effortlessly.

| Framework / Language | Example Path | Description |
| :--- | :--- | :--- |
| **HTML Static** | [`/apps/html/html-static`](./apps/html/html-static) | A simple static HTML site served by NGINX. |
| **React + Vite** | [`/apps/javascript/react-vite`](./apps/javascript/react-vite) | A blazing fast modern React app bundled with Vite and served by NGINX. |
| **Next.js** | [`/apps/javascript/nextjs`](./apps/javascript/nextjs) | A production-ready Next.js SSR standalone build. |
| **SvelteKit** | [`/apps/javascript/sveltekit`](./apps/javascript/sveltekit) | A full-stack Svelte app built for Node.js. |
| **Vue + Nuxt** | [`/apps/javascript/vue-nuxt`](./apps/javascript/vue-nuxt) | An intuitive Vue framework for building universal applications. |

---

## ⚙️ Backend & APIs

Robust and scalable backend services written in your favorite languages.

| Framework / Language | Example Path | Description |
| :--- | :--- | :--- |
| **Go (Stdlib)** | [`/apps/go/go-http`](./apps/go/go-http) | A highly concurrent, dependency-free HTTP server in Go. |
| **Java Spring Boot** | [`/apps/java/java-springboot`](./apps/java/java-springboot) | Enterprise-grade REST API using Spring Boot. |
| **C# .NET Core** | [`/apps/csharp/csharp-dotnet`](./apps/csharp/csharp-dotnet) | A robust ASP.NET Core minimal API. |
| **Node.js Express** | [`/apps/javascript/nodejs-express`](./apps/javascript/nodejs-express) | A fast, unopinionated, minimalist web framework for Node.js. |
| **Python FastAPI** | [`/apps/python/python-fastapi`](./apps/python/python-fastapi) | High-performance Python API using ASGI and FastAPI. |
| **Python Flask** | [`/apps/python/python-flask`](./apps/python/python-flask) | A lightweight WSGI web application framework in Python. |
| **Python Django** | [`/apps/python/python-django`](./apps/python/python-django) | A high-level Python web framework that encourages rapid development. |
| **Rust Axum** | [`/apps/rust/rust-axum`](./apps/rust/rust-axum) | An incredibly fast, ergonomic, and modular web framework built with Tokio. |
| **Ruby on Rails** | [`/apps/ruby/ruby-rails`](./apps/ruby/ruby-rails) | A classic MVC web application framework optimized for developer happiness. |
| **PHP Laravel** | [`/apps/php/php-laravel`](./apps/php/php-laravel) | The PHP framework for web artisans, served with PHP-FPM. |

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
