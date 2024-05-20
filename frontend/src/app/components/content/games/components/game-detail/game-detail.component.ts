import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { GameModel } from '../../models/game.model';
import { GameService } from '../../services/game.service';
import { ActivatedRoute } from '@angular/router';
import { CategoryModel } from '../../../models/category.model';

@Component({
  selector: 'app-game-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './game-detail.component.html',
  styleUrl: './game-detail.component.scss'
})
export class GameDetailComponent {
  gameUrl: string = "";
  gameId: string = "";
  game: GameModel = new GameModel(); // tıklanan oyunu tutacak

  gameCategories: CategoryModel[] = []; // tıklanan oyunun kategorilerini tutacak

  constructor(
    private _gameService: GameService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.gameUrl = res["url"];
      this.gameId = res["id"];
      this.getGameByUrl();
    });
  }

  getGameByUrl(){
    this._gameService.getGameByUrl(this.gameUrl, res => {
      this.game = res;

      for(let i = 0; i < this.game.categories.length; i++){
        this.getCategoryById(this.game.categories[i]);
      }
    });
  }

  getCategoryById(categoryId: any){
    this._gameService.getCategoryById(categoryId, res => {
      this.gameCategories.push(res);
    });
  }




  addComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
