import requests
from bs4 import BeautifulSoup

from JobOffer import JobOffer


def get_job_offers_ejobs(job_title, job_location):
    # TODO poti cauta doar dupa locatie si fara job title https://www.ejobs.ro/locuri-de-munca/brasov/
    # TODO poti cauta doar job_title fara locatie https://www.ejobs.ro/locuri-de-munca/cluj-napoca/?cauta=Java
    ejobs_url = f"https://www.ejobs.ro/locuri-de-munca/{job_location}/?cauta={job_title}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/79.0.3945.130 Safari/537.36"}
    page = requests.get(ejobs_url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    job_list = soup.find(id="job-app-list")
    job_card_tags = job_list.find_all("div", {"class": "jobitem-inner"})
    job_offers = create_job_offers(job_card_tags)
    return job_offers


def create_job_offers(job_card_tags):
    job_offers = []
    for job_card_tag in job_card_tags:
        title = job_card_tag.find("a", {"class": "title dataLayerItemLink"}).get_text()
        company_name = job_card_tag.find("a", {"class": "company"}).get_text().strip()
        application_url = get_application_link(job_card_tag)
        job_offer = JobOffer(title, company_name, application_url)
        job_offers.append(job_offer)
    return job_offers


def get_application_link(job_card_tag):
    button_text = job_card_tag.find("a", {"class": "ebtn"})
    if button_text.attrs["title"] == "Aplică extern":
        return button_text.attrs["data-external-url"]
    else:
        title_tag = job_card_tag.find("a", {"class": "title dataLayerItemLink"})
        return title_tag.attrs["href"]
