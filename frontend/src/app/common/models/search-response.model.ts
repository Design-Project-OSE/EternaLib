import { BookModel } from "../../components/content/books/models/book.model";
import { GameModel } from "../../components/content/games/models/game.model";
import { MovieModel } from "../../components/content/movies/models/movie.model";

export class SearchResponseModel{
  movies: MovieModel[] = [];
  books: BookModel[] = [];
  games: GameModel[] = [];
}
