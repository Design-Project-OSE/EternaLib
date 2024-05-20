import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { GameModel } from '../../models/game.model';
import { GameService } from '../../services/game.service';
import { ActivatedRoute } from '@angular/router';
import { CategoryModel } from '../../../models/category.model';
import { GameCommentsModel } from '../../models/game-comments.model';
import { ToastrService } from 'ngx-toastr';
import { GameAddLikeOrDislikeModel } from '../../models/game-add-like-or-dislike.model';
import { GameAddCommentModel } from '../../models/game-add-comment.model';

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

  comments: GameCommentsModel[] = []; // tıklanan oyunun yorumlarını tutacak

  constructor(
    private _gameService: GameService,
    private _toastr: ToastrService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.gameUrl = res["url"];
      this.gameId = res["id"];
      this.getGameByUrl();
      this.getGameComments();
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

  addLikeOrDislike(likeOrDislike: boolean){
    let model = new GameAddLikeOrDislikeModel();
    model.gameID = this.gameId;

    if(likeOrDislike){
      model.like = true;
      model.dislike = false;
    } else {
      model.dislike = true;
      model.like = false;
    }

    this._gameService.addLikeOrDislike(model, res => {
      this.getGameByUrl();
    });
  }

  getGameComments(){
    let model = { gameID: this.gameId }
    this._gameService.getGameComments(model, res => {
      this.comments = res;
    });
  }

  addComment(form: NgForm){
    let model = new GameAddCommentModel();
    model.gameID = this.gameId;
    model.comment = form.controls["comment"].value;

    this._gameService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getGameComments();
      form.reset();
    });
  }
}
