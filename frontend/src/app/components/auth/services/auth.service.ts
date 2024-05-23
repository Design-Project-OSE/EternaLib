import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../common/services/generic-http.service';
import { Router } from '@angular/router';
import { LoginModel } from '../models/login.model';
import { RegisterModel } from '../models/register.model';
import { ToastrService } from 'ngx-toastr';
import { LoginResponseModel } from '../models/login-response.model';
import { UserModel } from '../models/user.model';
import { SwalService } from '../../../common/services/swal.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isAuthPages: boolean = false;
  isLoggedIn: boolean = false;

  constructor(
    private _http: GenericHttpService,
    private _toastr: ToastrService,
    private _swal: SwalService,
    private _router: Router
  ) { }

  login(model: LoginModel, callback: (res: LoginResponseModel) => void){
    this._http.post<LoginResponseModel>('login', model, res => callback(res));
  }

  register(model: RegisterModel, callback: (res: LoginResponseModel) => void){
    this._http.post<LoginResponseModel>('register', model, res => callback(res))
  }

  getUserById(model: any, callback: (res: UserModel) => void){
    this._http.post<UserModel>('account', model, res => callback(res));
  }

  IsUserLoggedIn(){
    let currentUrl = window.location.href;
    sessionStorage.setItem('redirectAfterLogin', currentUrl);
    if(!localStorage.getItem("user")){
      this._swal.callSwall("If you want to comment, you should create an account!","You don't have an account", "Create Account", () =>
        {
          this._router.navigateByUrl("/register");
        });
    }
  }

  // LoginResponseModel tipinde döndürür
  getCurrentUser(){
    if(typeof localStorage != 'undefined'){
      let userString = localStorage.getItem("user");
      let user = JSON.parse(userString);
      return user;
    }
  }

  logOut(){
    this._http.post<any>('logout', null, res => {
      this.isLoggedIn = false;
      let user = this.getCurrentUser();
      this._toastr.info(`Good Bye! ${user.userfullname}` ,"Çıkış Yapıldı");
      localStorage.removeItem("user");
      this._router.navigateByUrl('/login');
    });
  }
}
