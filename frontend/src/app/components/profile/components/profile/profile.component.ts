import { Component, OnInit } from '@angular/core';
import { SharedModule } from '../../../../common/shared/shared.module';
import { ProfileService } from '../../services/profile.service';
import { ProfileModel } from '../../models/profile.model';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { MovieModel } from '../../../content/movies/models/movie.model';
import { MovieService } from '../../../content/movies/services/movie.service';
import { GameModel } from '../../../content/games/models/game.model';
import { BookModel } from '../../../content/books/models/book.model';
import { GameService } from '../../../content/games/services/game.service';
import { BookService } from '../../../content/books/services/book.service';
import { AuthService } from '../../../auth/services/auth.service';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [SharedModule, RouterModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.scss'
})
export class ProfileComponent implements OnInit {
  username: string = "";
  userId: string = "";

  profile: ProfileModel = new ProfileModel();

  currentUser = this._auth.getCurrentUser();

  likedMovies: MovieModel[] = [];
  likedGames: GameModel[] = [];
  likedBooks: BookModel[] = [];

  constructor(
    private _profileService: ProfileService,
    private _auth: AuthService,
    private _movieService: MovieService,
    private _gameService: GameService,
    private _bookService: BookService,
    private _activated: ActivatedRoute
  ){
    this._activated.params.subscribe(res => {
      this.username = res["username"];
      this.userId = res["id"];
      this.getProfileByUserId(this.userId);
      this.getUsersLikedMovies();
      this.getUsersLikedGames();
      this.getUsersLikedBooks();
    });
  }

  ngOnInit(): void {

  }

  getProfileByUserId(id: string){
    let model = { userID: id };
    this._profileService.getProfileByUserId(model, res => {
      this.profile = res;
    });
  }



  getUsersLikedMovies(){
    let model = { userID: this.userId };
    this._movieService.getUsersLikedMovies(model, res => {
      res.forEach(movie => {
        this.getMovieById(movie.movieID);
      });
    });
  }
  getMovieById(id: string){
    this._movieService.getMovieById(id, res => {
      this.likedMovies.push(res);
    });
  }


  getUsersLikedGames(){
    let model = { userID: this.userId };
    this._gameService.getUsersLikedGames(model, res => {
      res.forEach(game => {
        this.getGameById(game.gameID);
      });
    });
  }
  getGameById(id: string){
    this._gameService.getGameById(id, res => {
      this.likedGames.push(res);
    });
  }


  getUsersLikedBooks(){
    let model = { userID: this.userId };
    this._bookService.getUsersLikedBooks(model, res => {
      res.forEach(book => {
        this.getBookById(book.bookID);
      });
    });
  }
  getBookById(id: string){
    this._bookService.getBookById(id, res => {
      this.likedBooks.push(res);
    });
  }



}
