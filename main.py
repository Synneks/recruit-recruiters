from time import time

import pandas
from pyshorteners import Shortener

from ejobs import job_service as ejobs_job_service
from indeed import job_service as indeed_job_service


def shorten_application_link(application_link):
    shortener = Shortener('Tinyurl')
    short_url = shortener.short(application_link)
    return short_url


def get_jobs(job_name, job_location):
    print("Extracting ro.indeed.com offers...")
    start = time()
    indeed_offers = indeed_job_service.get_job_offers_indeed(job_name, job_location)
    end = time()
    print(f"Extracted offers from ro.indeed.com in {end - start} seconds")
    print("Extracting ejobs.ro offers...")
    start = time()
    ejobs_offers = ejobs_job_service.get_job_offers_ejobs(job_name, job_location)
    end = time()
    print(f"Extracted offers from ejobs.ro in {end - start} seconds")
    return indeed_offers + ejobs_offers


jobs = get_jobs(job_name="Manager", job_location="Cluj-Napoca")
# TODO get more jobs as in go on the next page of results
print("Shortening links...")
for job in jobs:
    shortened_link = shorten_application_link(job.get_application_link())
    job.set_application_link(shortened_link)
df = pandas.DataFrame(jobs)
df.to_csv("jobs.csv", index=False, header=False)
print("Job offers scraped")
