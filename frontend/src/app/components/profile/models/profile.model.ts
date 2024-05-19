import { BookModel } from "../../content/books/models/book.model";
import { GameModel } from "../../content/games/models/game.model";
import { MovieModel } from "../../content/movies/models/movie.model";

export class ProfileModel{
  id: string = "";
  full_name: string = "";
  about: string = "";
  profile_picture: string = "";
  liked_games: GameModel[] = [];
  liked_movies: MovieModel[] = [];
  liked_books: BookModel[] = [];
  x_link: string = "";
  instagram_link: string = "";
  facebook_link: string = "";
  linkedin_link: string = "";
}
