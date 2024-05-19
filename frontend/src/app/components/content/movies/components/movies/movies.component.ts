import { Component, OnInit } from '@angular/core';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';
import { MovieModel } from '../../models/movie.model';
import { CategoryModel } from '../../../models/category.model';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [SharedModule, ContentComponent],
  templateUrl: './movies.component.html',
  styleUrl: './movies.component.scss'
})
export class MoviesComponent implements OnInit {
  movies: MovieModel[] = [];
  categories: CategoryModel[] = [];

  constructor(
    private _movieService: MovieService
  ){}

  ngOnInit(): void{
    this.getMovies();
    this.getMovieCategories();
  }

  getMovies(){
    this._movieService.getMovies(res => {
      this.movies = res;
      console.log(this.movies);
    });
  }

  getMovieCategories(){
    this._movieService.getMovieCategories(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }
}
