import { Component, OnInit } from '@angular/core';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { BookModel } from '../../models/book.model';
import { CategoryModel } from '../../../models/category.model';
import { BookService } from '../../services/book.service';
import { SearchService } from '../../../../../common/services/search.service';
import { SearchModel } from '../../../../../common/models/search.model';
import { NgxPaginationModule } from 'ngx-pagination';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [SharedModule, ContentComponent, NgxPaginationModule],
  templateUrl: './books.component.html',
  styleUrl: './books.component.scss'
})
export class BooksComponent implements OnInit {
  books: BookModel[] = [];
  categories: CategoryModel[] = [];
  selectedCategory: string = "All";

  search: SearchModel = new SearchModel();

  pageNumber: number = 1;
  pageSize: number = 10;

  constructor(
    private _bookService: BookService,
    private _searchService: SearchService
  ){}

  ngOnInit(): void{
    this.getBooks("");
    this.getAllCategoriesForBooks();
  }

  getBooks(query: string, categoryId: string = "All"){
    this.search.searchterm = query;

    if(this.selectedCategory == "All"){
      if(query == ""){
        this._bookService.getBooks(res => {
          this.books = res;
        });
      } else {
        this._searchService.search(this.search, res => {
          this.books = res.books;
        });
      }
    } else {
      this._bookService.getBooksByCategoryId(categoryId, res => {
        this.books = res;
      });
    }
  }

  getAllCategoriesForBooks(){
    this._bookService.getAllCategoriesForBooks(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }
}
