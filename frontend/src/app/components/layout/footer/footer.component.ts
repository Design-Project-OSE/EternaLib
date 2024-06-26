import { Component } from '@angular/core';
import { AuthService } from '../../auth/services/auth.service';
import { SharedModule } from '../../../common/shared/shared.module';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.scss'
})
export class FooterComponent {

  constructor(
    public _auth: AuthService
  ){}

  isHomePage(){
    if(!this._auth.isAuthPages){
      return "footer-default";
    } else {
      return "";
    }
  }
}
