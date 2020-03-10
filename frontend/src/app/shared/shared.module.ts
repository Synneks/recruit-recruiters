import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { HeaderComponent } from "./components/header/header.component";
import { FooterComponent } from "./components/footer/footer.component";
import { FlexLayoutModule } from "@angular/flex-layout";
import { SearchBoxComponent } from './components/search-box/search-box.component';
import { MaterialDesignModule } from '../material-design.module';

@NgModule({
  declarations: [HeaderComponent, FooterComponent, SearchBoxComponent],
  imports: [
    CommonModule,
    FlexLayoutModule,
    MaterialDesignModule
  ],
  exports: [HeaderComponent, FooterComponent, SearchBoxComponent]
})
export class SharedModule {}
