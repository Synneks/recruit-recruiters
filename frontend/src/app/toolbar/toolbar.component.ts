import { Component, Input, Output, EventEmitter } from "@angular/core";
import { User } from "src/assets/model/user";

@Component({
  selector: "app-toolbar",
  templateUrl: "./toolbar.component.html",
  styleUrls: ["./toolbar.component.css"]
})
export class ToolbarComponent {
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
