import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AuthService } from '../../auth/services/auth.service';
import { AnimatedButtonComponent } from '../../../common/components/animated-button/animated-button.component';
import { LoginResponseModel } from '../../auth/models/login-response.model';
import { ProfileModel } from '../../profile/models/profile.model';
import { ProfileService } from '../../profile/services/profile.service';
import { SearchService } from '../../../common/services/search.service';
import { SearchModel } from '../../../common/models/search.model';
import { MovieModel } from '../../content/movies/models/movie.model';
import { BookModel } from '../../content/books/models/book.model';
import { GameModel } from '../../content/games/models/game.model';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterModule, AnimatedButtonComponent],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit{
  currentUser: LoginResponseModel = new LoginResponseModel();

  profile: ProfileModel = new ProfileModel();

  search: SearchModel = new SearchModel();

  allMovies: MovieModel[] = [];
  allBooks: BookModel[] = [];
  allGames: GameModel[] = [];

  constructor(
    public _auth: AuthService,
    private _profileService: ProfileService,
    private _searchService: SearchService
  ){}

  ngOnInit(){
    this.getCurrentUser();
    this.getProfileByUserId();
  }

  searchForContents(query: string) {
    this.search.searchterm = query;
    if(query !=""){
      this._searchService.search(this.search, res => {
        this.allMovies = res.movies;
        this.allBooks = res.books;
        this.allGames = res.games;
      });
    } else {
      this.allMovies = [];
      this.allBooks = [];
      this.allGames = [];
    }
  }


  getCurrentUser(){
    this.currentUser = this._auth.getCurrentUser();
    console.log(this.currentUser);
 }

 getProfileByUserId(){
  let model = { userID: this.currentUser.id };
  this._profileService.getProfileByUserId(model, res => {
    this.profile = res;
  });
}
}
