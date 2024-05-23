import { Injectable } from '@angular/core';
import { GenericHttpService } from './generic-http.service';
import { SearchModel } from '../models/search.model';
import { SearchResponseModel } from '../models/search-response.model';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(
    private http: GenericHttpService
  ) { }

  search(model: SearchModel, callback: (res: SearchResponseModel) => void) {
    this.http.post<SearchResponseModel>('search/', model, res => callback(res));
  }
}
