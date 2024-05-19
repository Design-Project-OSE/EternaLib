import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../auth/services/auth.service';
import { AnimatedButtonComponent } from '../../../common/components/animated-button/animated-button.component';
import { UserModel } from '../../auth/models/user.model';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterModule, AnimatedButtonComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{
  currentUserFullName: string = "";

  constructor(
    public _auth: AuthService
  ){}

  ngOnInit(){
    this.getCurrentUser();
  }

  getCurrentUser(){
    this.currentUserFullName = this._auth.getCurrentUser().userfullname;
 }

}
