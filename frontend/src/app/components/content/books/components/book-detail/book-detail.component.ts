import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { BookModel } from '../../models/book.model';
import { BookService } from '../../services/book.service';
import { ActivatedRoute } from '@angular/router';
import { CategoryModel } from '../../../models/category.model';
import { BookCommentsModel } from '../../models/book-comments.model';
import { ToastrService } from 'ngx-toastr';
import { BookAddLikeOrDislikeModel } from '../../models/book-add-like-or-dislike.model';
import { BookAddCommentModel } from '../../models/book-add-comment.model';

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

  comments: BookCommentsModel[] = []; // tıklanan kitabın yorumlarını tutacak

  constructor(
    private _bookService: BookService,
    private _toastr: ToastrService,
    private _activates: ActivatedRoute
  ){
    this._activates.params.subscribe(res => {
      this.bookUrl = res["url"];
      this.bookId = res["id"];
      this.getBookByUrl();
      this.getBookComments();
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


  addLikeOrDislike(likeOrDislike: boolean){
    let model = new BookAddLikeOrDislikeModel();
    model.bookID = this.bookId;

    if(likeOrDislike){
      model.like = true;
      model.dislike = false;
    } else {
      model.dislike = true;
      model.like = false;
    }

    this._bookService.addLikeOrDislike(model, res => {
      this.getBookByUrl();
    });
  }

  getBookComments(){
    let model = { bookID: this.bookId }
    this._bookService.getBookComments(model, res => {
      this.comments = res;
    });
  }




  addComment(form: NgForm){
    let model = new BookAddCommentModel();
    model.bookID = this.bookId;
    model.comment = form.controls["comment"].value;

    this._bookService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getBookComments();
      form.reset();
    });
  }
}
