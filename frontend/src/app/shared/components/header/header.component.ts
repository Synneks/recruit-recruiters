import { Component, OnInit, Input, Output, EventEmitter } from "@angular/core";
import { User } from "src/assets/model/user";

@Component({
  selector: "app-header",
  templateUrl: "./header.component.html",
  styleUrls: ["./header.component.css"]
})
export class HeaderComponent {
  @Input() loggedUser: User;
  @Output() themeChangerEvent = new EventEmitter();

  constructor() {}
  //TODO add loggedUser variable that is a User

  goToLink(url: string) {
    window.open(url);
  }

  themeChanged() {
    this.themeChangerEvent.emit();
  }
}
