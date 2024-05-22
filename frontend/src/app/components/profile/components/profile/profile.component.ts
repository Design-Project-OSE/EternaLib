import { Component } from '@angular/core';
import { SharedModule } from '../../../../common/shared/shared.module';
import { ProfileService } from '../../services/profile.service';
import { ProfileModel } from '../../models/profile.model';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent {
  username: string = "";
  userId: string = "";

  profile: ProfileModel = new ProfileModel();

  constructor(
    private _profileService: ProfileService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.username = res["username"];
      this.userId = res["id"];
      this.getProfileByUserId(this.userId);
    });
  }

  getProfileByUserId(id: string){
    let model = { userID: id};

    this._profileService.getProfileByUserId(model, res => {
      this.profile = res;
      console.log(res);
    });
  }
}
