import { Component, OnInit } from '@angular/core';
import { User } from 'src/assets/model/user';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.css']
})
export class DefaultComponent implements OnInit {
  loggedUser: User;
  otherTheme = false;

  ngOnInit() {
    this.loggedUser = JSON.parse(localStorage.getItem("User"));
  }

  changeTheme() {
    this.otherTheme = !this.otherTheme;
  }

}
