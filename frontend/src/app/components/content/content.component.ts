import { Component } from '@angular/core';
import { LoginService } from '../../services/login.service';
import { DatabaseService } from '../../services/database.service';
import { get } from 'http';
import { Router } from '@angular/router';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent {

  movies: any[any];

  // api isteği deneme için
  constructor(
    private _databaseService: DatabaseService,
    private _router: Router
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
