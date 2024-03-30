import { Component } from '@angular/core';
import { LoginService } from '../../services/login.service';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent {

  movies: any[any];

  // api isteği deneme için
  constructor(
    private loginService: LoginService
  ) {
    this.loginService.getMovies().subscribe({
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
