import { CategoryModel } from "../../models/category.model";

export class MovieModel{
  id: string = "";
  name: string = "";
  urlname: string = "";
  production: string = "";
  about: string = "";
  categories: CategoryModel[] = [];
  release: string = "";
  imdb: string = "";
  metacritic: string = "";
  background: string = "";
  poster: string = "";
  trailer: string = "";
  savedate: string = "";
  isPublished: boolean = false;
  like: number = 0;
  dislike: number = 0;
  commentscount: number = 0;
}
