import requests
import time

def check_proxy(proxy):
    try:
        response = requests.get('https://www.google.com', proxies={'https': proxy}, timeout=10)
        if response.status_code == 200:
            return True, response.elapsed.total_seconds()
    except:
        pass
    return False, None

def main():
    filename = "http_proxies.txt"
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()

    valid_proxies = []
    invalid_proxies = []

    print(f"Total proxies: {len(proxies)}")

    start_time = time.time()

    for i, proxy in enumerate(proxies, start=1):
        proxy = proxy.strip()
        is_valid, latency = check_proxy(proxy)
        if is_valid:
            valid_proxies.append((proxy, latency))
        else:
            invalid_proxies.append(proxy)

        elapsed_time = time.time() - start_time
        average_time_per_proxy = elapsed_time / i
        remaining_proxies = len(proxies) - i
        remaining_time = remaining_proxies * average_time_per_proxy

        eta_str = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
        print(f"ETA: {eta_str}")

    print(f"Valid proxies: {len(valid_proxies)}")
    for proxy, latency in valid_proxies:
        print(f"Proxy: {proxy}, Latency: {latency} seconds")

    print(f"Invalid proxies: {len(invalid_proxies)}")
    for proxy in invalid_proxies:
        print(f"Proxy: {proxy}, Invalid")

    if valid_proxies:
        with open('valid_proxies.txt', 'w') as valid_file:
            valid_file.write('\n'.join([proxy for proxy, _ in valid_proxies]))
        print("Valid proxies saved to 'valid_proxies.txt'")

if __name__ == '__main__':
    main()
