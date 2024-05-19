import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { GameModel } from '../models/game.model';
import { CategoryModel } from '../../models/category.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getGames(callback: (res: GameModel[]) => void) {
    this._http.get<GameModel[]>(`games/`, res => callback(res));
  }

  getGameCategories(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>(`games/category`, res => callback(res));
  }

  getGameByUrl(url: string, callback: (res: GameModel) => void){
    this._http.get<GameModel>('games/urlname/' + url, res => callback(res));
  }
}
