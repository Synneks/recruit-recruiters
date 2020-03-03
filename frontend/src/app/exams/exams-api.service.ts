import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { Observable } from "rxjs";
import { Exam } from "./exam.model";
import { API_URL } from "../env";
import "rxjs/add/operator/catch";

@Injectable({
  providedIn: "root"
})
export class ExamsApiService {
  constructor(private http: HttpClient) {}

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || "[ERROR] - Unable to complete request");
  }

  //GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http
      .get(`${API_URL}/exams`)
      .catch(ExamsApiService._handleError);
  }
}
