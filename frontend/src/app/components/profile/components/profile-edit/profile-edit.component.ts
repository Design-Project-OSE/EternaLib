import { Component, input } from '@angular/core';
import { SharedModule } from '../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { ProfileService } from '../../services/profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { ProfileUpdateModel } from '../../models/profile-update.model';
import { ChangePasswordModel } from '../../models/change-password.model';
import { SwalService } from '../../../../common/services/swal.service';
import { AuthService } from '../../../auth/services/auth.service';

@Component({
  selector: 'app-profile-edit',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './profile-edit.component.html',
  styleUrl: './profile-edit.component.scss'
})
export class ProfileEditComponent {
  updateProfile: ProfileUpdateModel = new ProfileUpdateModel();
  userId: string = "";
  username: string = "";

  selectedFile: File | null = null;
  profilePictureUrl: string | null = null;

  constructor(
    private _profileService: ProfileService,
    private _toastr: ToastrService,
    private _router: Router,
    private _swal: SwalService,
    private _authService: AuthService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.username = res["value"];
      this.userId = res["id"];
      this.getProfileByUserId(this.userId);
    });
  }

  onFileSelected(event: any) {
    const file = event.target.files[0];
    if (file) {
      this.selectedFile = file;
    }
  }

  onUpload() {
    if (this.selectedFile) {
      this._profileService.updateProfilePicture(this.userId, this.selectedFile, res => {
        this.profilePictureUrl = res.url;
        this.getProfileByUserId(this.userId);
        this._toastr.success(res.message);
      });
    } else {
      this._toastr.error('Please select a file');
    }
  }



  getProfileByUserId(id: string){
    let model = { userID: id };

    this._profileService.getProfileByUserId(model, res => {
      this.updateProfile = res;
      this.profilePictureUrl = res.profil_picture;
    });
  }


  editProfile(form: NgForm){
    if(form.valid){
      this.updateProfile.userID = this.userId;

      this._profileService.updateProfile(this.updateProfile, res => {
      console.log(res);
      this._toastr.success('Profile updated successfully');
      form.reset();
      this.getProfileByUserId(this.userId);
    });
    }
  }

  changePassword(form: NgForm){
    if(form.valid){
      let model = new ChangePasswordModel();
      model.userID = this.userId;
      model.current_password = form.controls['oldPassword'].value;
      model.new_password = form.controls['newPassword'].value;

      this._profileService.channgePassword(model, res => {
        this._toastr.success(res.message);
        form.reset();
        document.getElementById('closeModal').click();
      });
    }
  }

  deleteUser(){
    this._swal.callSwall("Are you sure you want to delete your account?","Delete Account", "Delete", () =>
      {
        let model = { userID: this.userId }
        this._profileService.deleteUser(model, res => {
        localStorage.removeItem('user');
        this._toastr.info(res.message);
        this._authService.isLoggedIn = false;
        this._router.navigateByUrl('/login');
      });
    });
  }
}
