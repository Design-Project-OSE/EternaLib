import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../auth/services/auth.service';
import { AnimatedButtonComponent } from '../../../common/components/animated-button/animated-button.component';
import { LoginResponseModel } from '../../auth/models/login-response.model';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterModule, AnimatedButtonComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{
  currentUser: LoginResponseModel = new LoginResponseModel();

  constructor(
    public _auth: AuthService
  ){}

  ngOnInit(){
    this.getCurrentUser();
  }

  getCurrentUser(){
    this.currentUser = this._auth.getCurrentUser();
    console.log(this.currentUser);
 }
}
