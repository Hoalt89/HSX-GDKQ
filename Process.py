from typing import List


def extract_titles(news_list: list) -> List[str]:
    """
    Extract titles from news items.
    """
    titles = []
    for item in news_list:
        title = item.get("title")
        if title:
            titles.append(title)

    return titles


def filter_titles(titles: List[str], phrase: str) -> List[str]:
    """
    Filter titles containing a keyword.
    """
    phrase = phrase.lower()
    return [title for title in titles if phrase in title.lower()]