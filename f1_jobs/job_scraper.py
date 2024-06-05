# f1_jobs/job_scraper.py
import logging
from f1_jobs.website_parsers import parsers  # import the list of parsers

class JobScraper:
    def __init__(self):
        self.parsers = parsers

    def scrape_jobs(self):
        all_jobs = []
        for parser in self.parsers:
            try:
                jobs = parser['get_jobs']()
                all_jobs.extend(jobs)
            except Exception as e:
                logging.error(f"Error scraping jobs from {parser['name']}: {e}")
        return all_jobs
