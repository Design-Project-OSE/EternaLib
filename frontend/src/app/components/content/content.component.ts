import { Component } from '@angular/core';
import { DatabaseService } from '../../services/database.service';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent {

  index: number;
  movies: any[any];

  // api isteği deneme için
  constructor(
    private _databaseService: DatabaseService
  ) {
    this.getMovies();
  }

  getMovies() {
    this._databaseService.getMovies().subscribe({
      next: (data) => {
        this.movies = data;
        console.log(this.movies);
      },
      error: (error) => {
        console.log(error);
      }
    });
  }
}
