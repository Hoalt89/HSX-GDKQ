import requests

BASE_URL = (
    "https://api.hsx.vn/n/api/v1/1/news/newstype/-1/1"
    "?pageSize=30&startDate=2025-09-08&endDate=2026-03-08"
)


def fetch_page(page_index: int) -> list:
    """
    Fetch news list from HSX API for a given page.
    """
    url = f"{BASE_URL}&pageIndex={page_index}"
    print(f"Fetching: {url}")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data.get("data", {}).get("list", [])