import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { BookModel } from '../../models/book.model';
import { BookService } from '../../services/book.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './book-detail.component.html',
  styleUrl: './book-detail.component.scss'
})
export class BookDetailComponent {
  bookUrl: string = "";
  book: BookModel = new BookModel();

  constructor(
    private _bookService: BookService,
    private _activates: ActivatedRoute
  ){
    this._activates.params.subscribe(res => {
      this.bookUrl = res["value"];
      this.getBookByUrl();
    });
  }

  getBookByUrl(){
    this._bookService.getBookByUrl(this.bookUrl, res => {
      this.book = res;
    });
  }

  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
