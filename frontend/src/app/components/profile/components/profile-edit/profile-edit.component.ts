import { Component } from '@angular/core';
import { SharedModule } from '../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { ProfileService } from '../../services/profile.service';
import { ActivatedRoute } from '@angular/router';
import { ProfileUpdateModel } from '../../models/profile-update.model';

@Component({
  selector: 'app-profile-edit',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './profile-edit.component.html',
  styleUrl: './profile-edit.component.scss'
})
export class ProfileEditComponent {
  profile: ProfileUpdateModel = new ProfileUpdateModel();
  userId: string = "";
  username: string = "";


  constructor(
    private _profileService: ProfileService,
    private _toastr: ToastrService,
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
    });
  }

  editProfile(form: NgForm){
    if(form.valid){
      this.profile.userID = this.userId;

      this._profileService.updateProfile(this.profile, res => {
        console.log(res);
        this._toastr.success('Profile updated successfully');
        form.reset();
      });
    } else {
      this._toastr.error('Please fill all the required fields');
    }
  }
}
