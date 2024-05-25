import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../common/services/generic-http.service';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getMostPopularMoviesIds(callback: (res: string[]) => void) {
    this._http.get<string[]>('movies/list/top', res => callback(res));
  }

  getMostPopularGamesIds(callback: (res: string[]) => void) {
    this._http.get<string[]>('games/list/top', res => callback(res));
  }

  getMostPopularBooksIds(callback: (res: string[]) => void) {
    this._http.get<string[]>('books/list/top', res => callback(res));
  }
}
