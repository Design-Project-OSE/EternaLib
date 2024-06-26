import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { BookModel } from '../models/book.model';
import { CategoryModel } from '../../models/category.model';
import { BookCommentsModel } from '../models/book-comments.model';
import { BookLikesAndDislikesModel } from '../models/book-likes-and-dislikes.model';
import { BookAddCommentModel } from '../models/book-add-comment.model';
import { BookAddLikeOrDislikeModel } from '../models/book-add-like-or-dislike.model';
import { MessageResponseModel } from '../../../../common/models/message.response.model';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getBooks(callback: (res: BookModel[]) => void){
    this._http.get<BookModel[]>('books', res => callback(res));
  } // tüm kitapları getirir

  getAllCategoriesForBooks(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>('books/category', res => callback(res));
  } // kitaplar için olan tüm kategorileri getirir

  getBookByUrl(url: string, callback: (res: BookModel) => void){
    this._http.get<BookModel>('books/urlname/' + url, res => callback(res));
  } // url'si verilen kitabın detaylarını getirir

  getBookById(id: string, callback: (res: BookModel) => void){
    this._http.get<BookModel>('books/id/' + id, res => callback(res));
  } // id'si verilen kitabın detaylarını getirir


  getBooksByCategoryId(categoryId: string, callback: (res: BookModel[]) => void){
    let model = { catalogID: categoryId }
    this._http.post<BookModel[]>('books/category/get', model, res => callback(res));
  } // id'si verilen kategorideki kitapları getirir


  getCategoryById(categoryId: string, callback: (res: CategoryModel) => void){
    this._http.get<CategoryModel>('books/get/id/category/' + categoryId, res => callback(res));
  } // id'si verilen kategoriyi getirir


  getUsersLikedBooks(model: any, callback: (res: BookLikesAndDislikesModel[]) => void){
    this._http.post<BookLikesAndDislikesModel[]>('books/get/sid/like', model, res => callback(res));
  } // userID'ye göre kullanıcının beğendiği kitapları getirir

  deleteComment(model: any, callback: (res: MessageResponseModel) => void){
    this._http.post<MessageResponseModel>('books/comment/delete', model, res => callback(res));
  } // benzersiz id'si ve kullanıcı id'si verilen yorum siler



  getBookComments(model: any, callback: (res: BookCommentsModel[]) => void){
    this._http.post<BookCommentsModel[]>('books/get/id/comment', model, res => callback(res));
  }



  addComment(comment: BookAddCommentModel, callback: (res: BookCommentsModel) => void){
    this._http.post<BookCommentsModel>('books/add/comment', comment, res => callback(res));
  }

  addLikeOrDislike(likeOrDislike: BookAddLikeOrDislikeModel, callback: (res: BookLikesAndDislikesModel) => void){
    this._http.post<BookLikesAndDislikesModel>('books/add/like', likeOrDislike, res => callback(res));
  }

  getBookLikesAndDislikes(callback: (res: BookAddLikeOrDislikeModel[]) => void){
    this._http.get<BookAddLikeOrDislikeModel[]>('books/like', res => callback(res));
  } // kitabı beğenenleri/beğenmeyenleri getirir
}
