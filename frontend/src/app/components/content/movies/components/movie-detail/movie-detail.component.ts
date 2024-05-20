import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';
import { ActivatedRoute } from '@angular/router';
import { MovieModel } from '../../models/movie.model';
import { MovieCommentsModel } from '../../models/movie-comments.model';
import { CategoryModel } from '../../../models/category.model';
import { MovieAddLikeOrDislikeModel } from '../../models/movie-add-like-or-dislike.model';
import { MovieAddCommentModel } from '../../models/movie-add-comment.model';
import { ToastrService } from 'ngx-toastr';

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

  constructor(
    private _movieService: MovieService,
    private _toastr: ToastrService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.movieUrl = res["url"];
      this.movieId = res["id"];
      this.getMovieByUrl();
      this.getMovieComments();
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


  addLikeOrDislike(likeOrDislike: boolean){
    let model = new MovieAddLikeOrDislikeModel();
    model.movieID = this.movieId;

    if(likeOrDislike){
      model.like = true;
      model.dislike = false;
    } else {
      model.dislike = true;
      model.like = false;
    }

    this._movieService.addLikeOrDislike(model, res => {
      this.getMovieByUrl();
    });
  }


  getMovieComments(){
    let model = { movieID: this.movieId }
    this._movieService.getMovieComments(model, res => {
      this.comments = res;
    });
  }


  
  addComment(form: NgForm){
    let model = new MovieAddCommentModel();
    model.movieID = this.movieId;
    model.comment = form.controls["comment"].value;

    this._movieService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getMovieComments();
      form.reset();
    });
  }
}
