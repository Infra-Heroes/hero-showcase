# Build stage
FROM golang:1.26.1-alpine AS builder

WORKDIR /app

RUN go mod init my-awesome-app || true

COPY main.go ./
RUN go build -o server main.go

# Final stage
FROM alpine:latest
RUN apk add --no-cache ca-certificates

WORKDIR /root/
COPY --from=builder /app/server .

EXPOSE 3000

CMD ["./server"]
