import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { BookModel } from '../models/book.model';
import { CategoryModel } from '../../models/category.model';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getBooks(callback: (res: BookModel[]) => void){
    this._http.get<BookModel[]>('book/', res => callback(res));
  }

  getBookCategories(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>('book/category', res => callback(res));
  }

  getBookByUrl(url: string, callback: (res: BookModel) => void){
    this._http.get<BookModel>('book/urlname/' + url, res => callback(res));
  }
}
