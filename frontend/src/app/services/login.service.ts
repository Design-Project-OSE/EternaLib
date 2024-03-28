import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  isRegisterForm: boolean = false;
  isLoginPage: boolean = false;
}
