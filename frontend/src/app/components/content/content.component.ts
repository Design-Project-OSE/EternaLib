import { Component, OnInit } from '@angular/core';
import { DatabaseService } from '../../services/database.service';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent implements OnInit{

  public movies: any[any];

  // api isteği deneme için
  constructor(
    private _dbService: DatabaseService
  ) {}

  ngOnInit(): void {
    this.getMovies();
  }

  getMovies() {
    this._dbService.getMovies(res => this.movies = res);
    console.log(this.movies);
  }

  getMovie(id: number) {
    this._dbService.getMovie(id, res => this.movies = res);
  }
}
