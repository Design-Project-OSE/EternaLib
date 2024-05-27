import { Component, OnInit } from '@angular/core';
import { SharedModule } from '../../common/shared/shared.module';
import { HomePopularComponent } from '../../common/components/home-popular/home-popular.component';
import { HomeService } from './services/home.service';
import { MovieModel } from '../content/movies/models/movie.model';
import { GameModel } from '../content/games/models/game.model';
import { BookModel } from '../content/books/models/book.model';
import { MovieService } from '../content/movies/services/movie.service';
import { GameService } from '../content/games/services/game.service';
import { BookService } from '../content/books/services/book.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [SharedModule, HomePopularComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit{

  mostPopularMoviesIds: string[] = [];
  mostPopularGamesIds: string[] = [];
  mostPopularBooksIds: string[] = [];

  mostPopularMovies: MovieModel[] = [];
  mostPopularGames: GameModel[] = [];
  mostPopularBooks: BookModel[] = [];

  constructor(
    private _homeService: HomeService,
    private _movieService: MovieService,
    private _gameService: GameService,
    private _bookService: BookService
  ){}

  ngOnInit(): void {
    this.getMostPopularMovies();
    this.getMostPopularGames();
    this.getMostPopularBooks();
  }

  getMostPopularMovies() {
    this._homeService.getMostPopularMoviesIds(res => {
      this.mostPopularMoviesIds = res;

      this.mostPopularMoviesIds.forEach(id => {
        this._movieService.getMovieById(id, movie => {
          this.mostPopularMovies.push(movie);
        });
      });
    });
  }

  getMostPopularGames() {
    this._homeService.getMostPopularGamesIds(res => {
      this.mostPopularGamesIds = res;

      this.mostPopularGamesIds.forEach(id => {
        this._gameService.getGameById(id, game => {
          this.mostPopularGames.push(game);
        });
      });
    });
  }

  getMostPopularBooks() {
    this._homeService.getMostPopularBooksIds(res => {
      this.mostPopularBooksIds = res;

      this.mostPopularBooksIds.forEach(id => {
        this._bookService.getBookById(id, book => {
          this.mostPopularBooks.push(book);
        });
      });
    });
  }
}
