import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { GameModel } from '../models/game.model';
import { CategoryModel } from '../../models/category.model';
import { GameCommentsModel } from '../models/game-comments.model';
import { GameLikesAndDislikesModel } from '../models/game-likes-and-dislikes.model';
import { GameAddCommentModel } from '../models/game-add-comment.model';
import { GameAddLikeOrDislikeModel } from '../models/game-add-like-or-dislike.model';
import { MessageResponseModel } from '../../../../common/models/message.response.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getGames(callback: (res: GameModel[]) => void) {
    this._http.get<GameModel[]>(`games`, res => callback(res));
  } // tüm oyunları getirir

  getAllCategoriesForGames(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>(`games/category`, res => callback(res));
  } // oyunlar için olan tüm kategorileri getirir

  getGameByUrl(url: string, callback: (res: GameModel) => void){
    this._http.get<GameModel>('games/urlname/' + url, res => callback(res));
  } // url'si verilen oyunun detaylarını getirir

  getGameById(id: string, callback: (res: GameModel) => void){
    this._http.get<GameModel>('games/id/' + id, res => callback(res));
  } // id'si verilen oyunun detaylarını getirir


  getGamesByCategoryId(categoryId: string, callback: (res: GameModel[]) => void){
    let model = { catalogID: categoryId }
    this._http.post<GameModel[]>('games/category/get', model, res => callback(res));
  } // id'si verilen kategorideki oyunları getirir


  getCategoryById(categoryId: string, callback: (res: CategoryModel) => void){
    this._http.get<CategoryModel>('games/get/id/category/' + categoryId, res => callback(res));
  } // id'si verilen kategoriyi getirir


  getUsersLikedGames(model: any, callback: (res: GameLikesAndDislikesModel[]) => void){
    this._http.post<GameLikesAndDislikesModel[]>('games/get/sid/like', model, res => callback(res));
  } // userID'ye göre kullanıcının beğendiği oyunları getirir

  deleteComment(model: any, callback: (res: MessageResponseModel) => void){
    this._http.post<MessageResponseModel>('games/comment/delete', model, res => callback(res));
  } // benzersiz id'si ve kullanıcı id'si verilen yorum siler



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
