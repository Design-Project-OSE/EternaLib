import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  isRegisterForm: boolean = false;
  isLoginPage: boolean = false;

  private url = 'https://api.themoviedb.org/3/discover/movie?api_key=a2c7a4725a20a6ac6a17a8712c37fca9';

  constructor(
    private _http: HttpClient
  ) { }

  getMovies() {
    return this._http.get(this.url);
  }
}
