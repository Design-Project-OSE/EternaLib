import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getAll(callback: (res: any[]) => void){
    this._http.get<any[]>('movies/all', res => callback(res));
  }

  getCategories(callback: (res: any[]) => void){
    this._http.get<any[]>('movies/category', res => callback(res));
  }
}
