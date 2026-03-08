from HSX import fetch_page
from Process import extract_titles, filter_titles

MAX_PAGES = 10
SEARCH_PHRASE = "bổ sung chứng khoán không đủ điều kiện giao dịch ký quỹ"


def collect_titles(max_pages: int):
    all_titles = []

    for page in range(1, max_pages + 1):
        try:
            news_list = fetch_page(page)

            if not news_list:
                print("No more data.")
                break

            titles = extract_titles(news_list)
            all_titles.extend(titles)

        except Exception as e:
            print(f"Error at page {page}: {e}")
            break

    return all_titles


def main():
    titles = collect_titles(MAX_PAGES)

    print("\n--- All Titles ---")
    for t in titles:
        print("-", t)

    filtered = filter_titles(titles, SEARCH_PHRASE)

    print("\n--- Filtered Titles ---")
    for t in filtered:
        print("-", t)


if __name__ == "__main__":
    main()