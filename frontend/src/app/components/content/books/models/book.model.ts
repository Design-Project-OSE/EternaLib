import { CategoryModel } from "../../models/category.model";

export class BookModel{
  id: string = "";
  name: string = "";
  urlname: string = "";
  production: string = "";
  about: string = "";
  categories: CategoryModel[] = [];
  release: string = "";
  background: string = "";
  poster: string = "";
  savedate: string = "";
  isPublished: boolean = false;
  like: number = 0;
}
