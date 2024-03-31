import { Injectable } from '@angular/core';
import { GenericHttpService } from './generic-http.service';

@Injectable({
  providedIn: 'root'
})
export class DatabaseService {
  constructor(
    private _http: GenericHttpService
  ) { }

  getMovies(callBack: (res: any) => void) {
   this._http.get<any[]>('movies', res => callBack(res));
  }

  getMovie(id: number, callBack: (res: any) => void) {
   this._http.get<any>('detail/' + id.toString(), res => callBack(res));
  }
}
