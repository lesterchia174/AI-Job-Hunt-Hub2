# tests/test_mcf.py
# Run:  python -m tests.test_mcf

from job_search import search_mycareersfuture


def main():
    print("Searching MyCareersFuture for 'data analyst'...")
    results, diag = search_mycareersfuture("data analyst", max_results=10)

    print(f"\npages_fetched = {diag['pages_fetched']}")
    if diag.get("errors"):
        print("errors:")
        for e in diag["errors"]:
            print("  -", e)

    print(f"\n{len(results)} results:\n")
    for i, j in enumerate(results, 1):
        print(f"{i:2d}. {j.title}")
        print(f"    company:  {j.company}")
        print(f"    url:      {j.url}")
        print(f"    salary:   {j.salary or '—'}")
        print(f"    posted:   {j.posted_date or '—'}")
        print(f"    location: {j.location or '—'}")
        print(f"    desc len: {len(j.description)}")
        print()

    # Sanity assertions
    assert len(results) > 0, "Expected at least one result"
    assert all(j.title for j in results), "Every posting should have a title"
    assert all(j.company for j in results), "Every posting should have a company"
    assert all(j.url.startswith("http") for j in results), "Every URL should be absolute"


if __name__ == "__main__":
    main()
