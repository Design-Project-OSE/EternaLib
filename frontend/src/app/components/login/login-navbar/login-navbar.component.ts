import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-navbar',
  templateUrl: './login-navbar.component.html',
  styleUrl: './login-navbar.component.scss'
})
export class LoginNavbarComponent {
  constructor(
    private _router: Router
  ){}

  goHome(){
    this._router.navigateByUrl("/home");
  }
}
