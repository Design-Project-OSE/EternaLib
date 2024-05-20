import { Component, OnInit } from '@angular/core';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { GameModel } from '../../models/game.model';
import { CategoryModel } from '../../../models/category.model';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-games',
  standalone: true,
  imports: [SharedModule, ContentComponent],
  templateUrl: './games.component.html',
  styleUrl: './games.component.scss'
})
export class GamesComponent implements OnInit {
  games: GameModel[] = [];
  categories: CategoryModel[] = [];

  constructor(
    private _gameService: GameService
  ){}

  ngOnInit(): void{
    this.getGames();
    this.getAllCategoriesForGames();
  }

  getGames(){
    this._gameService.getGames(res => {
      this.games = res;
      console.log(this.games);
    });
  }

  getAllCategoriesForGames(){
    this._gameService.getAllCategoriesForGames(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }



}
