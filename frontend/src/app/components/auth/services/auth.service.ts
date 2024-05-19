import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../common/services/generic-http.service';
import { Router } from '@angular/router';
import { LoginModel } from '../models/login.model';
import { RegisterModel } from '../models/register.model';
import { ToastrService } from 'ngx-toastr';
import { LoginResponseModel } from '../models/login-response.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isAuthPages: boolean = false;
  isLoggedIn: boolean = false;

  constructor(
    private _http: GenericHttpService,
    private _toastr: ToastrService,
    private _router: Router
  ) { }

  login(model: LoginModel, callback: (res: LoginResponseModel) => void){
    this._http.post<LoginResponseModel>('api/login', model, res => callback(res));
  }

  register(model: RegisterModel, callback: (res: LoginResponseModel) => void){
    this._http.post<LoginResponseModel>('register', model, res => callback(res))
  }


  getCurrentUser(){
    let userString = localStorage.getItem("user");
    let user = JSON.parse(userString);
    return user;
  }

  logOut(){
    let userString = localStorage.getItem("user");
    let user = JSON.parse(userString);

    this._toastr.info(`Good Bye! ${user.userfullname}` ,"Çıkış Yapıldı");
    localStorage.removeItem("user");
    this.isLoggedIn = false;
  }


}
