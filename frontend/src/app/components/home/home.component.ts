import { Component } from '@angular/core';
import { SharedModule } from '../../common/shared/shared.module';
import { HomePopularComponent } from '../../common/components/home-popular/home-popular.component';
import { SearchService } from '../../common/services/search.service';
import { SearchModel } from '../../common/models/search.model';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [SharedModule, HomePopularComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  search: SearchModel = new SearchModel();

  constructor(
    private _searchService: SearchService
  ){}

  searchForContents(query: string) {
    this.search.searchterm = query;
    if(query !=""){
      this._searchService.search(this.search, res => {
        console.log(res);
        console.log(res.books);
        console.log(res.movies);
        console.log(res.games);
      });
    }
  }
}
