import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { GameModel } from '../../models/game.model';
import { GameService } from '../../services/game.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-game-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './game-detail.component.html',
  styleUrl: './game-detail.component.scss'
})
export class GameDetailComponent {
  gameUrl: string = "";
  game: GameModel = new GameModel();

  constructor(
    private _gameService: GameService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.gameUrl = res["value"];
      this.getGameByUrl();
    });
  }

  getGameByUrl(){
    this._gameService.getGameByUrl(this.gameUrl, res => {
      this.game = res;
    });
  }




  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
