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
import { AuthService } from '../../../../auth/services/auth.service';

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

  isLiked: boolean;
  isDisliked: boolean;

  currentUser = this._authService.getCurrentUser();

  constructor(
    private _gameService: GameService,
    private _toastr: ToastrService,
    private _authService: AuthService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.gameUrl = res["url"];
      this.gameId = res["id"];
      this.getGameByUrl();
      this.getGameComments();
      this.getGameLikesAndDislikes();
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

  getGameLikesAndDislikes(){
    this._gameService.getGameLikesAndDislikes(res => {
      for(let i = 0; i < res.length; i++){
        if(res[i].gameID == this.gameId && res[i].userID == this.currentUser.id){
          this.isLiked = res[i].like;
          this.isDisliked = res[i].dislike;
        }
      }
    });
  }

  addLike(){
    this._authService.IsUserLoggedIn("like this game");

    let model = new GameAddLikeOrDislikeModel();
    model.gameID = this.gameId;
    model.userID = this.currentUser.id;

    if(!this.isLiked){
      model.like = true;
      model.dislike = false;
    } else {
      model.like = false;
      model.dislike = this.isDisliked;
    }

    this._gameService.addLikeOrDislike(model, res => {
      this.getGameByUrl();
      this.getGameLikesAndDislikes();
    });
  }

  addDislike(){
    this._authService.IsUserLoggedIn("dislike this game");

    let model = new GameAddLikeOrDislikeModel();
    model.gameID = this.gameId;
    model.userID = this.currentUser.id;

    if(!this.isDisliked){
      model.dislike = true;
      model.like = false;
    } else {
      model.dislike = false;
      model.like = this.isLiked;
    }

    this._gameService.addLikeOrDislike(model, res => {
      this.getGameByUrl();
      this.getGameLikesAndDislikes();
    });
  }

  getGameComments(){
    let model = { gameID: this.gameId }
    this._gameService.getGameComments(model, res => {
      this.comments = res;
      console.log(res);
    });
  }

  addComment(form: NgForm){
    this._authService.IsUserLoggedIn("comment this game");

    let model = new GameAddCommentModel();
    model.gameID = this.gameId;
    model.userID = this.currentUser.id;
    model.comment = form.controls["comment"].value;

    this._gameService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getGameComments();
      form.reset();
    });
  }
}
