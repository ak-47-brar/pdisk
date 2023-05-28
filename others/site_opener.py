import requests
import time

def visit_link_with_proxy(link, proxy):
    try:
        response = requests.get(link, proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Visited {link} using proxy: {proxy}")
        else:
            print(f"Failed to visit {link} using proxy: {proxy}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to visit {link} using proxy: {proxy}. Exception: {e}")

def visit_link_with_proxies(link, proxy_file):
    with open(proxy_file, 'r') as f:
        proxies = f.read().splitlines()
    
    for proxy in proxies:
        visit_link_with_proxy(link, proxy)
        time.sleep(2)  # Delay for 2 seconds

# Usage example
proxy_file = 'proxy.txt'
link_to_visit = 'https://fs15.pdisk.pro:183/d/ji7whu7imezfofqkdibwbp3sxftpb7hdqlwpcrub6l3pkccnwvkv2r24ezjcymrwnozlbfl3/18693.mp4'

visit_link_with_proxies(link_to_visit, proxy_file)
