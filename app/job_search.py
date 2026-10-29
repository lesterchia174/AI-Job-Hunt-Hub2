# job_search.py

# --- imports ---
import time
import requests
from dataclasses import dataclass, field

# --- constants ---
MCF_URL = "https://api.mycareersfuture.gov.sg/v2/search"
MCF_PAGE_SIZE = 100
MCF_DEFAULT_MAX_PAGES = 3
MCF_TIMEOUT = 15

# --- contract ---
@dataclass
class JobPosting:
    source: str
    title: str
    company: str
    url: str
    description: str
    location: str = ""
    salary: str = ""
    posted_date: str = ""
    employment_type: str = ""
    seniority: str = ""
    skills: list[str] = field(default_factory=list)
    raw: dict = field(default_factory=dict)

# --- public API for this portal ---
def search_mycareersfuture(
    keywords: str,
    max_results: int = 60,
    max_pages: int | None = None,
    sort_by: str = "new_posting_date",
    extra_filters: dict | None = None,
) -> tuple[list[JobPosting], dict]:
    ...   # full body from previous reply

# --- private mapper ---
def _map_mcf_job(j: dict) -> JobPosting:
    ...
