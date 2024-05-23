import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';
import { ActivatedRoute, Router } from '@angular/router';
import { MovieModel } from '../../models/movie.model';
import { MovieCommentsModel } from '../../models/movie-comments.model';
import { CategoryModel } from '../../../models/category.model';
import { MovieAddLikeOrDislikeModel } from '../../models/movie-add-like-or-dislike.model';
import { MovieAddCommentModel } from '../../models/movie-add-comment.model';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from '../../../../auth/services/auth.service';
import { SwalService } from '../../../../../common/services/swal.service';

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './movie-detail.component.html',
  styleUrl: './movie-detail.component.scss'
})
export class MovieDetailComponent {
  movieUrl: string = "";
  movieId: string = "";
  movie: MovieModel = new MovieModel(); // tıklanan filmi tutacak

  movieCategories: CategoryModel[] = []; // tıklanan filmin kategorilerini tutacak

  comments: MovieCommentsModel[] = []; // tıklanan filmin yorumlarını tutacak

  isLiked: boolean;
  isDisliked: boolean;

  currentUser = this._authService.getCurrentUser();

  constructor(
    private _movieService: MovieService,
    private _toastr: ToastrService,
    private _authService: AuthService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.movieUrl = res["url"];
      this.movieId = res["id"];
      this.getMovieByUrl();
      this.getMovieComments();
      this.getMovieLikesAndDislikes();
    });
  }


  getMovieByUrl(){
    this._movieService.getMovieByUrl(this.movieUrl, res => {
      this.movie = res;

      for(let i = 0; i < this.movie.categories.length; i++){
        this.getCategoryById(this.movie.categories[i]);
      }
    });
  }

  getCategoryById(categoryId: any){
    this._movieService.getCategoryById(categoryId, res => {
      this.movieCategories.push(res);
    });
  }

  getMovieLikesAndDislikes(){
    this._movieService.getMovieLikesAndDislikes(res => {
      for(let i = 0; i < res.length; i++){
        if(res[i].movieID == this.movieId && res[i].userID == this.currentUser.id){
          this.isLiked = res[i].like;
          this.isDisliked = res[i].dislike;
        }
      }
    });
  }


  addLike(){
    this._authService.IsUserLoggedIn();

    let model = new MovieAddLikeOrDislikeModel();
    model.movieID = this.movieId;
    model.userID = this.currentUser.id;

    if(!this.isLiked){
      model.like = true;
      model.dislike = false;
    } else {
      model.like = false;
      model.dislike = this.isDisliked;
    }

    this._movieService.addLikeOrDislike(model, res => {
      this.getMovieByUrl();
      this.getMovieLikesAndDislikes();
    });
  }

  addDislike(){
    this._authService.IsUserLoggedIn();

    let model = new MovieAddLikeOrDislikeModel();
    model.movieID = this.movieId;
    model.userID = this.currentUser.id;

    if(!this.isDisliked){
      model.dislike = true;
      model.like = false;
    } else {
      model.dislike = false;
      model.like = this.isLiked;
    }

    this._movieService.addLikeOrDislike(model, res => {
      this.getMovieByUrl();
      this.getMovieLikesAndDislikes();
    });
  }


  getMovieComments(){
    let model = { movieID: this.movieId }
    this._movieService.getMovieComments(model, res => {
      this.comments = res;
      console.log(res);
    });
  }



  addComment(form: NgForm){
    this._authService.IsUserLoggedIn();

    let model = new MovieAddCommentModel();
    model.movieID = this.movieId;
    model.userID = this.currentUser.id;
    model.comment = form.controls["comment"].value;

    this._movieService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getMovieComments();
      form.reset();
    });
  }
}
