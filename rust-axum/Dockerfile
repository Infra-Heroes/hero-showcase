FROM rust:1-alpine AS builder
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
COPY src ./src
RUN cargo build --release || true

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/target/release/rust-axum-app .
EXPOSE 3000
CMD ["./rust-axum-app"]
