import { Component, OnInit } from '@angular/core';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { BookModel } from '../../models/book.model';
import { CategoryModel } from '../../../models/category.model';
import { BookService } from '../../services/book.service';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [SharedModule, ContentComponent],
  templateUrl: './books.component.html',
  styleUrl: './books.component.scss'
})
export class BooksComponent implements OnInit {
  books: BookModel[] = [];
  categories: CategoryModel[] = [];

  constructor(
    private _bookService: BookService
  ){}

  ngOnInit(): void{
    this.getBooks();
    this.getAllCategoriesForBooks();
  }

  getBooks(){
    this._bookService.getBooks(res => {
      this.books = res;
      console.log(this.books);
    });
  }

  getAllCategoriesForBooks(){
    this._bookService.getAllCategoriesForBooks(res => {
      this.categories = res;
      console.log(this.categories);
    });
  }
}
