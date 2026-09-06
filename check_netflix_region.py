"""
check_netflix_region.py

Quick check: what country does your current network connection look like
it's coming from? Useful after connecting to a VPN, to confirm you're
actually showing up in the country you selected before opening Netflix.

Usage:
    python check_netflix_region.py

No API key required — uses a free public IP geolocation endpoint.
"""

import json
import urllib.request

ENDPOINT = "https://ipapi.co/json/"


def get_current_region():
    req = urllib.request.Request(ENDPOINT, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode())
    return {
        "ip": data.get("ip"),
        "country": data.get("country_name"),
        "country_code": data.get("country_code"),
        "region": data.get("region"),
        "city": data.get("city"),
    }


def main():
    try:
        info = get_current_region()
    except Exception as exc:
        print(f"Couldn't reach the geolocation service: {exc}")
        return

    print("Your connection currently looks like it's coming from:")
    print(f"  Country : {info['country']} ({info['country_code']})")
    print(f"  Region  : {info['region']}")
    print(f"  City    : {info['city']}")
    print(f"  IP      : {info['ip']}")
    print()
    print("If this doesn't match the VPN server you connected to,")
    print("reconnect and try a different server before opening Netflix.")


if __name__ == "__main__":
    main()
