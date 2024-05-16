import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AuthService } from '../../auth/services/auth.service';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {

  constructor(
    private _auth: AuthService
  ){}

  isHomePage(){
    if(this._auth.isHomePage){
      return "footer-default";
    } else {
      return "";
    }
  }
}
