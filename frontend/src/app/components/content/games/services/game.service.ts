import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { GameModel } from '../models/game.model';
import { CategoryModel } from '../../models/category.model';
import { GameCommentsModel } from '../models/game-comments.model';
import { GameLikesAndDislikesModel } from '../models/game-likes-and-dislikes.model';
import { AuthService } from '../../../auth/services/auth.service';
import { GameAddCommentModel } from '../models/game-add-comment.model';
import { GameAddLikeOrDislikeModel } from '../models/game-add-like-or-dislike.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {
  currentUser = this._authService.getCurrentUser();

  constructor(
    private _http: GenericHttpService,
    private _authService: AuthService
  ) { }

  getGames(callback: (res: GameModel[]) => void) {
    this._http.get<GameModel[]>(`games/`, res => callback(res));
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



  getGameComments(gameId: string, callback: (res: GameCommentsModel[]) => void){
    this._http.post<GameCommentsModel[]>('games/get/id/comment', gameId, res => callback(res));
  }

  // getGameLikesAndDislikes(gameId: string, callback: (res: GameLikesAndDislikesModel) => void){
  //   this._http.post<GameLikesAndDislikesModel>('games/get/like', gameId, res => callback(res));
  // }


  //---------------------------------------------
  addComment(comment: GameAddCommentModel, callback: (res: GameCommentsModel) => void){
    comment.userID = this.currentUser.userid;
    this._http.post<GameCommentsModel>('games/add/comment', comment, res => callback(res));
  }

  addLikeOrDislike(likeOrDislike: GameAddLikeOrDislikeModel, callback: (res: GameLikesAndDislikesModel) => void){
    likeOrDislike.userID = this.currentUser.userid;
    this._http.post<GameLikesAndDislikesModel>('games/add/like', likeOrDislike, res => callback(res));
  }
}
