import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { GameModel } from '../models/game.model';
import { CategoryModel } from '../../models/category.model';
import { GameCommentsModel } from '../models/game-comments.model';
import { GameLikesAndDislikesModel } from '../models/game-likes-and-dislikes.model';
import { GameAddCommentModel } from '../models/game-add-comment.model';
import { GameAddLikeOrDislikeModel } from '../models/game-add-like-or-dislike.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getGames(callback: (res: GameModel[]) => void) {
    this._http.get<GameModel[]>(`games`, res => callback(res));
  }

  getAllCategoriesForGames(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>(`games/category`, res => callback(res));
  }

  getGameByUrl(url: string, callback: (res: GameModel) => void){
    this._http.get<GameModel>('games/urlname/' + url, res => callback(res));
  }

  getCategoryById(categoryId: string, callback: (res: CategoryModel) => void){
    this._http.get<CategoryModel>('games/get/id/category/' + categoryId, res => callback(res));
  } // id'si verilen kategoriyi getirir



  getGameComments(model: any, callback: (res: GameCommentsModel[]) => void){
    this._http.post<GameCommentsModel[]>('games/get/id/comment', model, res => callback(res));
  }


  addComment(comment: GameAddCommentModel, callback: (res: GameCommentsModel) => void){
    this._http.post<GameCommentsModel>('games/add/comment', comment, res => callback(res));
  }

  addLikeOrDislike(likeOrDislike: GameAddLikeOrDislikeModel, callback: (res: GameLikesAndDislikesModel) => void){
    this._http.post<GameLikesAndDislikesModel>('games/add/like', likeOrDislike, res => callback(res));
  }

  getGameLikesAndDislikes(callback: (res: GameAddLikeOrDislikeModel[]) => void){
    this._http.get<GameAddLikeOrDislikeModel[]>('games/like', res => callback(res));
  } // oyunu beğenenleri/beğenmeyenleri getirir
}
