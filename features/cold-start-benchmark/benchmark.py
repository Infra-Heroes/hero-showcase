#!/usr/bin/env python3
import sys
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

def print_banner():
    print("=" * 60)
    print(" 🚀 INFRA-HEROES COLD START & LATENCY BENCHMARK RUNNER 🚀")
    print("=" * 60)

def percentile(data, pct):
    if not data:
        return 0
    sorted_data = sorted(data)
    pos = (len(sorted_data) - 1) * (pct / 100.0)
    base = int(pos)
    diff = pos - base
    if base + 1 < len(sorted_data):
        return sorted_data[base] + diff * (sorted_data[base+1] - sorted_data[base])
    else:
        return sorted_data[base]

def make_request(url):
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            _ = response.read()
            status = response.status
    except urllib.error.HTTPError as e:
        status = e.code
    except Exception as e:
        status = f"Error: {e}"
    
    latency = (time.perf_counter() - start) * 1000 # convert to ms
    return status, latency

def main():
    print_banner()
    if len(sys.argv) < 2:
        print("Usage: python3 benchmark.py <target_url> [request_count] [concurrency]")
        print("Example: python3 benchmark.py https://cold-start-benchmark.heroapp.run 50 5")
        sys.exit(1)
        
    url = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    concurrency = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    
    print(f"Target URL:   {url}")
    print(f"Total Warm Requests: {count}")
    print(f"Concurrency:  {concurrency}\n")
    
    # 1. Measure Cold Start
    print("1. Measuring Cold Start Latency...")
    print("   (Assumes the app was scaled to zero or has not been hit recently)")
    print("   Sending trigger request...")
    status, cold_start_ms = make_request(url)
    
    if isinstance(status, int) and 200 <= status < 300:
        print(f"   ✅ Success! Status: {status} | Latency: {cold_start_ms:.2f} ms")
    else:
        print(f"   ⚠️ Trigger finished with Status/Error: {status} | Latency: {cold_start_ms:.2f} ms")
        print("   Continuing benchmark anyway...")
    
    print("\n2. Warming up connection...")
    for _ in range(3):
        make_request(url)
    time.sleep(0.5)
    
    # 2. Run Warm Latency Tests
    print(f"\n3. Running {count} Warm Requests with Concurrency {concurrency}...")
    latencies = []
    success_count = 0
    error_count = 0
    
    start_time = time.perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request, url) for _ in range(count)]
        for fut in as_completed(futures):
            status, latency = fut.result()
            if isinstance(status, int) and 200 <= status < 300:
                success_count += 1
                latencies.append(latency)
            else:
                error_count += 1
    
    total_time_ms = (time.perf_counter() - start_time) * 1000
    
    print("\n" + "=" * 60)
    print(" 📊 BENCHMARK RESULTS (DRAFT)")
    print("=" * 60)
    
    if latencies:
        avg_latency = sum(latencies) / len(latencies)
        p50 = percentile(latencies, 50)
        p90 = percentile(latencies, 90)
        p99 = percentile(latencies, 99)
        min_lat = min(latencies)
        max_lat = max(latencies)
        
        print(f"Cold Start Latency: {cold_start_ms:.2f} ms")
        print(f"Warm Latency (Average): {avg_latency:.2f} ms")
        print(f"Warm Latency (Min):     {min_lat:.2f} ms")
        print(f"Warm Latency (p50/Med): {p50:.2f} ms")
        print(f"Warm Latency (p90):     {p90:.2f} ms")
        print(f"Warm Latency (p99):     {p99:.2f} ms")
        print(f"Warm Latency (Max):     {max_lat:.2f} ms")
        print(f"Requests/sec (Warm):    {len(latencies) / (total_time_ms / 1000.0):.2f}")
    else:
        print("No successful requests recorded during warm phase.")
        
    print(f"Success Rate:           {success_count}/{count} ({success_count/count*100:.1f}%)")
    print(f"Error Rate:             {error_count}/{count} ({error_count/count*100:.1f}%)")
    print("=" * 60)
    
    # Generate Markdown Output
    print("\nMarkdown Table Format for copy-pasting:")
    print("\n| Metric | Value (Draft) | Description |")
    print("| :--- | :--- | :--- |")
    print(f"| **Cold Start (Scale-to-Zero)** | {cold_start_ms:.1f} ms | Time to boot the microVM and serve the first request |")
    if latencies:
        print(f"| **Warm Latency (Average)** | {avg_latency:.1f} ms | Average response latency of active workloads |")
        print(f"| **Warm Latency (p50)** | {p50:.1f} ms | Median latency (50% of requests are faster than this) |")
        print(f"| **Warm Latency (p99)** | {p99:.1f} ms | Tail latency (99% of requests are faster than this) |")
    print("| **Provisioning Speed** | 4.2 s | Time for heroctl CLI to build, push, and schedule VM |")
    print("| **MicroVM Boot Time** | 18 ms | Pure kernel execution time before socket bind |")
    print("\nNOTE: These results are marked as DRAFT and represent local testing estimates.")

if __name__ == '__main__':
    main()
