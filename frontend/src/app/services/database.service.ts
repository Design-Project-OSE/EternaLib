import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {

  constructor(
    private _http: HttpClient
  ) { }

  getMovies() {
    return this._http.get('http://127.0.0.1:5000/movies');
  }

  getMovie(id: number) {
    return this._http.get('http://127.0.0.1:5000/detail/' + id.toString());
  }
}
