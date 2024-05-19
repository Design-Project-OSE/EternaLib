import { Injectable } from '@angular/core';
import { GenericHttpService } from '../../../../common/services/generic-http.service';
import { MovieModel } from '../models/movie.model';
import { CategoryModel } from '../../models/category.model';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(
    private _http: GenericHttpService
  ) { }

  getMovies(callback: (res: MovieModel[]) => void){
    this._http.get<MovieModel[]>('movies/', res => callback(res));
  }

  getMovieCategories(callback: (res: CategoryModel[]) => void){
    this._http.get<CategoryModel[]>('movie/category', res => callback(res));
  }

  getMovieByUrl(url: string, callback: (res: MovieModel) => void){
    this._http.get<MovieModel>('movies/urlname/' + url, res => callback(res));
  }
}
