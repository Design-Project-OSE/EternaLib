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
    this.getGameCategories();
  }

  getGames(){
    this._gameService.getGames(res => {
      this.games = res;
      console.log(this.games);
    });
  }

  getGameCategories(){
    this._gameService.getGameCategories(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }

  

}
