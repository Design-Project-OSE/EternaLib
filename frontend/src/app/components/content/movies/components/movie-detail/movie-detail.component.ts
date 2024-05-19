import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';
import { ActivatedRoute } from '@angular/router';
import { MovieModel } from '../../models/movie.model';

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './movie-detail.component.html',
  styleUrl: './movie-detail.component.scss'
})
export class MovieDetailComponent {
  movieUrl: string = "";
  movie: MovieModel = new MovieModel();

  constructor(
    private _movieService: MovieService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.movieUrl = res["value"];
      this.getMovieByUrl();
    });
  }

  getMovieByUrl(){
    this._movieService.getMovieByUrl(this.movieUrl, res => {
      this.movie = res;
    });
  }




  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
