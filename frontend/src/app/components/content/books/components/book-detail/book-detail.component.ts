import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { BookModel } from '../../models/book.model';
import { BookService } from '../../services/book.service';
import { ActivatedRoute } from '@angular/router';
import { CategoryModel } from '../../../models/category.model';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './book-detail.component.html',
  styleUrl: './book-detail.component.scss'
})
export class BookDetailComponent {
  bookUrl: string = "";
  bookId: string = "";
  book: BookModel = new BookModel(); // tıklanan kitabı tutacak

  bookCategories: CategoryModel[] = []; // tıklanan kitabın kategorilerini tutacak

  constructor(
    private _bookService: BookService,
    private _activates: ActivatedRoute
  ){
    this._activates.params.subscribe(res => {
      this.bookUrl = res["url"];
      this.bookId = res["id"];
      this.getBookByUrl();
    });
  }

  getBookByUrl(){
    this._bookService.getBookByUrl(this.bookUrl, res => {
      this.book = res;

      for(let i = 0; i < this.book.categories.length; i++){
        this.getCategoryById(this.book.categories[i]);
      }
    });
  }

  getCategoryById(categoryId: any){
    this._bookService.getCategoryById(categoryId, res => {
      this.bookCategories.push(res);
    });
  }




  
  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
