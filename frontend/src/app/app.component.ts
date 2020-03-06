import { Component, OnInit } from "@angular/core";
import { User } from "src/assets/model/user";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent implements OnInit {
  title = "Recruit-Recruiters";
  loggedUser: User;
  otherTheme = false;

  ngOnInit() {
    this.loggedUser = JSON.parse(localStorage.getItem("User"));
  }

  changeTheme() {
    this.otherTheme = !this.otherTheme;
  }
}
