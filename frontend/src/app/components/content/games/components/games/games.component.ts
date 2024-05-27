import { Component, OnInit } from '@angular/core';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { GameModel } from '../../models/game.model';
import { CategoryModel } from '../../../models/category.model';
import { GameService } from '../../services/game.service';
import { SearchService } from '../../../../../common/services/search.service';
import { SearchModel } from '../../../../../common/models/search.model';
import { NgxPaginationModule } from 'ngx-pagination';

@Component({
  selector: 'app-games',
  standalone: true,
  imports: [SharedModule, ContentComponent, NgxPaginationModule],
  templateUrl: './games.component.html',
  styleUrl: './games.component.scss'
})
export class GamesComponent implements OnInit {
  games: GameModel[] = [];
  categories: CategoryModel[] = [];
  selectedCategory: string = "All";

  search: SearchModel = new SearchModel();

  pageNumber: number = 1;
  pageSize: number = 10;

  constructor(
    private _gameService: GameService,
    private _searchService: SearchService
  ){}

  ngOnInit(): void{
    this.getGames("");
    this.getAllCategoriesForGames();
  }

  getGames(query: string, categoryId: string = "All"){
    this.search.searchterm = query;

    if(this.selectedCategory == "All"){
      if(query == ""){
        this._gameService.getGames(res => {
          this.games = res;
        });
      } else {
        this._searchService.search(this.search, res => {
          this.games = res.games;
        });
      }
    } else {
      this._gameService.getGamesByCategoryId(categoryId, res => {
        this.games = res;
      });
    }
  }

  getAllCategoriesForGames(){
    this._gameService.getAllCategoriesForGames(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }
}
