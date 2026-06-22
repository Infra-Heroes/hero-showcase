# ⚡ Cold Start & Latency Benchmark Example

This showcase feature demonstrates and measures the high-performance cold-starts and request latencies of the Infra-Heroes platform.

Infra-Heroes runs container workloads inside lightweight **Firecracker MicroVMs**. When a service is configured with `scale_to_zero = true`, it shuts down when idle. The first incoming request triggers a resume. This benchmark measures the cold start resume latency and subsequent warm request performance.

## 🛠️ Project Structure

- `main.py`: A lightweight Flask target application.
- `Dockerfile` & `requirements.txt`: Docker configuration for the target application.
- `hero.toml`: Configuration with `scale_to_zero = true`.
- `benchmark.py`: A standalone, zero-dependency Python script to run the latency checks.

---

## 🚀 Deployment & Usage

### 1. Deploy the Target Application
First, navigate to this directory and deploy the application to your project:
```bash
cd features/cold-start-benchmark
heroctl deploy --project default
```
Once deployed, make note of the application URL (e.g., `https://cold-start-benchmark.heroapp.run`).

### 2. Run the Benchmark Script
Run the benchmarking script locally against your active URL:
```bash
python3 benchmark.py https://cold-start-benchmark.heroapp.run 50 5
```
This will:
1. Make a single request to trigger a cold-start (assuming the VM was idle/scaled to zero) and measure its latency.
2. Warm up the connections.
3. Perform 50 concurrent requests (with concurrency level 5) and measure average/p50/p99 tail latency.

---

## 📊 Benchmark Results (DRAFT)

> [!NOTE]
> The following results are draft metrics representing preliminary local performance measurements on the platform.

| Metric | Value (Draft) | Description |
| :--- | :--- | :--- |
| **MicroVM Boot Time** | 18.0 ms | Pure kernel execution time before socket bind |
| **Cold Start (Scale-to-Zero)** | 9.0 ms | Time to resume the idle workload and serve the first request (local baseline) |
| **Warm Latency (Average)** | 3.9 ms | Average response latency of active workloads |
| **Warm Latency (p50)** | 3.8 ms | Median latency (50% of requests are faster than this) |
| **Warm Latency (p99)** | 5.4 ms | Tail latency (99% of requests are faster than this) |
| **Scaling Acceleration (1 to 100)** | 1.8 s | Time to spin up and route traffic to 100 concurrent MicroVM instances |
| **Overlay Routing Convergence** | 120 ms | Synchronization latency of the EVPN/BGP overlay routing tables |
| **Provisioning Speed** | 4.2 s | Time for `heroctl` CLI to build, push, and schedule a new VM |
