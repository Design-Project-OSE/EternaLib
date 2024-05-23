import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../auth/services/auth.service';
import { AnimatedButtonComponent } from '../../../common/components/animated-button/animated-button.component';
import { LoginResponseModel } from '../../auth/models/login-response.model';
import { ProfileModel } from '../../profile/models/profile.model';
import { ProfileService } from '../../profile/services/profile.service';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterModule, AnimatedButtonComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{
  currentUser: LoginResponseModel = new LoginResponseModel();

  profile: ProfileModel = new ProfileModel();

  constructor(
    public _auth: AuthService,
    private _profileService: ProfileService
  ){}

  ngOnInit(){
    this.getCurrentUser();
    this.getProfileByUserId();
  }

  getCurrentUser(){
    this.currentUser = this._auth.getCurrentUser();
    console.log(this.currentUser);
 }

 getProfileByUserId(){
  let model = { userID: this.currentUser.id };
  this._profileService.getProfileByUserId(model, res => {
    this.profile = res;
  });
}
}
