import { Component } from '@angular/core';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {

  isHomePage(){
    if(true){
      return "footer-default";
    } else {
      return "";
    }
  }
}
