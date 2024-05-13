import { Component } from '@angular/core';
import { LoginService } from '../../../services/login.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {

  constructor(
    public _s: LoginService
  ){}


  isHomePage(){
    if(!this._s.isLoginPage){
      return "footer-default";
    } else {
      return "";
    }
  }
}
