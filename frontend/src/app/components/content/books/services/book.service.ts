import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { BookModel } from '../models/book.model';
import { CategoryModel } from '../../models/category.model';
import { AuthService } from '../../../auth/services/auth.service';
import { BookCommentsModel } from '../models/book-comments.model';
import { BookLikesAndDislikesModel } from '../models/book-likes-and-dislikes.model';
import { BookAddCommentModel } from '../models/book-add-comment.model';
import { BookAddLikeOrDislikeModel } from '../models/book-add-like-or-dislike.model';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  currentUser = this._authService.getCurrentUser();

  constructor(
    private _http: GenericHttpService,
    private _authService: AuthService
  ) { }

  getBooks(callback: (res: BookModel[]) => void){
    this._http.get<BookModel[]>('books/', res => callback(res));
  }

  getAllCategoriesForBooks(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>('books/category', res => callback(res));
  }

  getBookByUrl(url: string, callback: (res: BookModel) => void){
    this._http.get<BookModel>('books/urlname/' + url, res => callback(res));
  }

  getCategoryById(categoryId: string, callback: (res: CategoryModel) => void){
    this._http.get<CategoryModel>('books/get/id/category/' + categoryId, res => callback(res));
  } // id'si verilen kategoriyi getirir




  getBookComments(model: any, callback: (res: BookCommentsModel[]) => void){
    this._http.post<BookCommentsModel[]>('books/get/id/comment', model, res => callback(res));
  }

  // getBookLikesAndDislikes(bookId: string, callback: (res: BookLikesAndDislikesModel) => void){
  //   this._http.post<BookLikesAndDislikesModel>('books/get/like', bookId, res => callback(res));
  // }




  //--------------------------------------------------
  addComment(comment: BookAddCommentModel, callback: (res: BookCommentsModel) => void){
    comment.userID = this.currentUser.userid;
    this._http.post<BookCommentsModel>('books/add/comment', comment, res => callback(res));
  }

  addLikeOrDislike(likeOrDislike: BookAddLikeOrDislikeModel, callback: (res: BookLikesAndDislikesModel) => void){
    likeOrDislike.userID = this.currentUser.userid;
    this._http.post<BookLikesAndDislikesModel>('books/add/like', likeOrDislike, res => callback(res));
  }
}
