# mcf_client.py

import requests

MCF_URL = "https://api.mycareersfuture.gov.sg/v2/search"
MCF_PAGE_SIZE = 100
MCF_TIMEOUT = 15


def fetch_page(
    keywords: str,
    page: int,
    limit: int = MCF_PAGE_SIZE,
    sort_by: str = "new_posting_date",
    extra_filters: dict | None = None,
) -> dict:
    """
    Fetch a single page of MCF search results.
    Returns the parsed JSON dict.
    Raises on HTTP error so the caller can decide whether to abort or skip.
    """
    url = f"{MCF_URL}?limit={limit}&page={page}"
    payload = {
        "search": keywords.strip(),
        "sortBy": [sort_by],
        "page": page,
    }
    if extra_filters:
        payload.update(extra_filters)

    r = requests.post(
        url,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=MCF_TIMEOUT,
    )
    r.raise_for_status()
    return r.json()
