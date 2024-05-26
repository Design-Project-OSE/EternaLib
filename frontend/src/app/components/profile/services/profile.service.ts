import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../common/services/generic-http.service';
import { ProfileModel } from '../models/profile.model';
import { ProfileUpdateModel } from '../models/profile-update.model';
import { MessageResponseModel } from '../../../common/models/message.response.model';
import { ChangePasswordModel } from '../models/change-password.model';
import { ProfilePictureResponseModel } from '../models/profile-picture.response.model';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getProfileByUserId(model: any, callback: (res: ProfileModel) => void){
    this._http.post<ProfileModel>('account', model, res => callback(res));
  }

  getProfileByUsername(model: any, callback: (res: ProfileModel) => void){
    this._http.post<ProfileModel>('account/username', model, res => callback(res));
  }

  updateProfile(profile: ProfileUpdateModel, callback: (res: ProfileUpdateModel) => void){
    this._http.post<ProfileUpdateModel>('account/update', profile, res => callback(res));
  }


  channgePassword(model: ChangePasswordModel, callback: (res: MessageResponseModel) => void){
    this._http.post<MessageResponseModel>('changepassword ', model, res => callback(res));
  }

  deleteUser(model: any, callback: (res: MessageResponseModel) => void){
    this._http.post<MessageResponseModel>('delete', model, res => callback(res));
  }



  updateProfilePicture(userID: string, file: File, callback: (res: ProfilePictureResponseModel) => void) {
    const formData: FormData = new FormData();
    formData.append('userID', userID);
    formData.append('profil_picture', file, file.name);

    this._http.post<ProfilePictureResponseModel>('updateprofilpicture', formData, res => callback(res));
  }
}
