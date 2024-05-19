import { CategoryModel } from "../../models/category.model";

export class GameModel{
  id: string = "";
  name: string = "";
  urlname: string = "";
  production: string = "";
  about: string = "";
  categories: CategoryModel[] = [];
  release: string = "";
  imdb: string = "";
  metascritic: string = "";
  background: string = "";
  poster: string = "";
  trailer: string = "";
  savedate: string = "";
  isPublished: boolean = false;
  like: number = 0;
}
