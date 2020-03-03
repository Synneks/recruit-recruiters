from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/exams')
def get_exams():
    # fetching from the database
    session = Session()
    exam_objects = session.query(Exam).all()

    # transforming into JSON-serializable objects
    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201


# from time import time

# import pandas
# from pyshorteners import Shortener

# from ejobs import job_service as ejobs_job_service
# from indeed import job_service as indeed_job_service
# from hipo import job_service as hipo_job_service


# def shorten_application_link(shortener, application_link):
#     short_url = shortener.short(application_link)
#     return short_url


# def get_jobs(job_name, job_location):
#     print("[INFO] - Extracting ro.indeed.com offers...")
#     start = time()
#     indeed_offers = indeed_job_service.get_job_offers(job_name, job_location)
#     end = time()
#     print(f"[INFO] - Extracted {len(indeed_offers)} offers from ro.indeed.com in {end - start} seconds")

#     print("[INFO] - Extracting ejobs.ro offers...")
#     start = time()
#     ejobs_offers = ejobs_job_service.get_job_offers(job_name, job_location)
#     end = time()
#     print(f"[INFO] - Extracted {len(ejobs_offers)} offers from ejobs.ro in {end - start} seconds")

#     print("[INFO] - Extracting hipo.ro offers...")
#     start = time()
#     hipo_offers = hipo_job_service.get_job_offers(job_name, job_location)
#     end = time()
#     print(f"[INFO] - Extracted {len(hipo_offers)} offers from hipo.ro in {end - start} seconds")

#     return indeed_offers + ejobs_offers + hipo_offers


# jobs = get_jobs(job_name="Java", job_location="Cluj-Napoca")
# # TODO get more jobs as in go on the next page of results
# print("[INFO] - Shortening links...")
# shortener = Shortener('Tinyurl', timeout= 9000)
# for job in jobs:
#     shortened_link = shorten_application_link(shortener, job.get_application_link())
#     job.set_application_link(shortened_link)

# df = pandas.DataFrame(jobs)
# df.to_csv("jobs.csv", index=False, header=False)
# print("[INFO] - Job offers scraped")
