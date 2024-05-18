import { Component, OnInit } from '@angular/core';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [SharedModule, ContentComponent],
  templateUrl: './movies.component.html',
  styleUrl: './movies.component.scss'
})
export class MoviesComponent implements OnInit {
  movies: any[any] = [];
  categories:any[any]=[];

  constructor(
    private _movieService: MovieService
  ){}

  ngOnInit(){
    
  }

  getAll(){
    this._movieService.getAll(res => {
      this.movies = res;
      console.log(this.movies);
    });
  }

  getCategories(){
    this._movieService.getCategories(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }


}
