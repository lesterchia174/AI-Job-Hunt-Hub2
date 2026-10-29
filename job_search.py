# job_search.py
import requests
from dataclasses import dataclass, field

MCF_URL = "https://api.mycareersfuture.gov.sg/v2/search"


@dataclass
class JobPosting:
    title: str
    company: str
    url: str
    description: str
    location: str = ""
    salary: str = ""
    posted_date: str = ""
    skills: list[str] = field(default_factory=list)


def search_mycareersfuture(keywords: str, max_results: int = 40) -> list[JobPosting]:
    """Search MyCareersFuture. Returns a list of JobPosting."""
    results: list[JobPosting] = []
    page = 0

    while len(results) < max_results:
        url = f"{MCF_URL}?limit=100&page={page}"
        payload = {"search": keywords.strip(), "sortBy": ["new_posting_date"]}

        try:
            r = requests.post(url, json=payload, timeout=15)
            r.raise_for_status()
            jobs = r.json().get("results", [])
        except Exception as e:
            raise RuntimeError(f"Search failed: {e}")

        if not jobs:
            break

        for j in jobs:
            company = (j.get("postedCompany") or {}).get("name", "")
            salary = j.get("salary") or {}
            salary_str = salary.get("range", "") if isinstance(salary, dict) else ""
            skills = [s.get("skill", "") for s in (j.get("skills") or []) if isinstance(s, dict)]

            results.append(JobPosting(
                title=j.get("title", ""),
                company=company,
                url=j.get("absoluteUrl", ""),
                description=j.get("description", ""),
                location=j.get("location", ""),
                salary=salary_str,
                posted_date=j.get("newPostingDate", ""),
                skills=skills,
            ))
            if len(results) >= max_results:
                break

        if len(jobs) < 100:
            break
        page += 1

    return results
