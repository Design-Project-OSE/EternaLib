import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../common/services/generic-http.service';
import { ProfileModel } from '../models/profile.model';
import { ProfileUpdateModel } from '../models/profile-update.model';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getProfileByUserId(model: any, callback: (res : ProfileModel) => void){
    this._http.post<ProfileModel>('account', model, res => callback(res));
  }

  updateProfile(profile: ProfileUpdateModel, callback: (res: ProfileUpdateModel) => void){
    this._http.post<ProfileUpdateModel>('account/update', profile, res => callback(res));
  }
}
