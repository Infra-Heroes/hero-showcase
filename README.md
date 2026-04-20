# Infra Heroes Showcase

A collection of example applications configured for deployment via `heroctl`. Each example includes a `hero.toml` deployment descriptor and a `Dockerfile`.

## Examples Included

| Example | Runtime | Framework | Port |
| :--- | :--- | :--- | :--- |
| [Go HTTP](./go-http) | Go | Standard Library | 3000 |
| [Python Flask](./python-flask) | Python | Flask | 5000 |
| [Python FastAPI](./python-fastapi) | Python | FastAPI | 8000 |
| [Node.js Express](./nodejs-express) | Node.js | Express | 8080 |
| [Java Spring Boot](./java-springboot) | Java | Spring Boot | 8080 |

### Common `heroctl` commands

```bash
# Sign up
heroctl signup

# Login
heroctl login

# Build and deploy the current directory
heroctl deploy --project ${PROJECT_NAME}
```
