import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-search-box",
  templateUrl: "./search-box.component.html",
  styleUrls: ["./search-box.component.css"]
})
export class SearchBoxComponent implements OnInit {
  citites = [
    "Abla",
    "Arad",
    "Argeș",
    "București",
    "Bacău",
    "Bihor",
    "Bistrița-Năsăud",
    "Botoșani",
    "Brăila"
  ];
  constructor() {}

  ngOnInit(): void {}
}
