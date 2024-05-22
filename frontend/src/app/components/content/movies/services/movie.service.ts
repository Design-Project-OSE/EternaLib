import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { MovieModel } from '../models/movie.model';
import { CategoryModel } from '../../models/category.model';
import { MovieCommentsModel } from '../models/movie-comments.model';
import { MovieLikesAndDislikesModel } from '../models/movie-likes-and-dislikes.model';
import { MovieAddCommentModel } from '../models/movie-add-comment.model';
import { MovieAddLikeOrDislikeModel } from '../models/movie-add-like-or-dislike.model';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getMovies(callback: (res: MovieModel[]) => void){
    this._http.get<MovieModel[]>('movies', res => callback(res));
  }

  getAllCategoriesForMovies(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>('movies/category', res => callback(res));
  }

  getMovieByUrl(url: string, callback: (res: MovieModel) => void){
    this._http.get<MovieModel>('movies/urlname/' + url, res => callback(res));
  }

  getCategoryById(categoryId: string, callback: (res: CategoryModel) => void){
    this._http.get<CategoryModel>('movies/get/id/category/' + categoryId, res => callback(res));
  } // id'si verilen kategoriyi getirir




  getMovieComments(model: any, callback: (res: MovieCommentsModel[]) => void){
    this._http.post<MovieCommentsModel[]>('movies/get/id/comment', model, res => callback(res));
  }



  addComment(comment: MovieAddCommentModel, callback: (res: MovieCommentsModel) => void){
    this._http.post<MovieCommentsModel>('movies/add/comment', comment, res => callback(res));
  }


  addLikeOrDislike(likeOrDislike: MovieAddLikeOrDislikeModel, callback: (res: MovieLikesAndDislikesModel) => void){
    this._http.post<MovieLikesAndDislikesModel>('movies/add/like', likeOrDislike, res => callback(res));
  }

  getMovieLikesAndDislikes(callback: (res: MovieAddLikeOrDislikeModel[]) => void){
    this._http.get<MovieAddLikeOrDislikeModel[]>('movies/like', res => callback(res));
  } // kitabı beğenenleri/beğenmeyenleri getirir
}
