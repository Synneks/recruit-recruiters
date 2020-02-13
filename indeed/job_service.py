import requests
from bs4 import BeautifulSoup

from JobOffer import JobOffer


def get_job_offers_indeed(job_title, job_location):
    result_from_indeed = requests.get(f"https://ro.indeed.com/jobs?q={job_title}&l={job_location}")
    src_code = result_from_indeed.content
    soup = BeautifulSoup(src_code, "html.parser")
    job_card_tags = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    job_offers = create_job_offers(job_card_tags)
    return job_offers


def create_job_offers(job_card_tags):
    job_offers = []
    for job_card_tag in job_card_tags:
        title_tag = job_card_tag.find("a")
        application_url = get_application_link(title_tag.attrs["href"])
        company_name = job_card_tag.find("span", {"class": "company"}).get_text().strip()
        title = title_tag.get_text().strip()
        job_offer = JobOffer(title, company_name, application_url)
        job_offers.append(job_offer)
    return job_offers


def get_application_link(job_card_link):
    job_card_link = "http://ro.indeed.com" + job_card_link
    page = requests.get(job_card_link)
    soup = BeautifulSoup(page.content, "html.parser")
    button = soup.find("a", {"class": "icl-Button"})
    if button.text == "Depuneți candidatura pe site-ul companiei":
        return button.attrs["href"]
    else:
        return job_card_link

# TODO cazul in care nu sunt locuri de munca sa afisez/retrunez ceva calumea
# arr = get_job_offers_indeed("QA", "Barlad")
# for a in arr:
#     print(a, "\n")
