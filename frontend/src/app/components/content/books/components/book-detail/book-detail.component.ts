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
import { AuthService } from '../../../../auth/services/auth.service';
import { UserModel } from '../../../../auth/models/user.model';

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

  comments: any[] = []; // tıklanan kitabın yorumlarını tutacak

  isLiked: boolean;
  isDisliked: boolean;

  currentUser = this._authService.getCurrentUser();

  constructor(
    private _bookService: BookService,
    private _toastr: ToastrService,
    private _activates: ActivatedRoute,
    private _authService: AuthService
  ){
    this._activates.params.subscribe(res => {
      this.bookUrl = res["url"];
      this.bookId = res["id"];
      this.getBookByUrl();
      this.getBookComments();
      this.getBookLikesAndDislikes();
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

  getBookLikesAndDislikes(){
    this._bookService.getBookLikesAndDislikes(res => {
      for(let i = 0; i < res.length; i++){
        if(res[i].bookID == this.bookId && res[i].userID == this.currentUser.id){
          this.isLiked = res[i].like;
          this.isDisliked = res[i].dislike;
        }
      }
    });
  }

  addLike(){
    let model = new BookAddLikeOrDislikeModel();
    model.bookID = this.bookId;
    model.userID = this.currentUser.id;

    if(!this.isLiked){
      model.like = true;
      model.dislike = false;
    } else {
      model.like = false;
      model.dislike = this.isDisliked;
    }

    this._bookService.addLikeOrDislike(model, res => {
      this.getBookByUrl();
      this.getBookLikesAndDislikes();
    });
  }

  addDislike(){
    let model = new BookAddLikeOrDislikeModel();
    model.bookID = this.bookId;
    model.userID = this.currentUser.id;

    if(!this.isDisliked){
      model.dislike = true;
      model.like = false;
    } else {
      model.dislike = false;
      model.like = this.isLiked;
    }

    this._bookService.addLikeOrDislike(model, res => {
      this.getBookByUrl();
      this.getBookLikesAndDislikes();
    });
  }



  getBookComments(){
    let model = { bookID: this.bookId }
    this._bookService.getBookComments(model, res => {
      this.comments = res;
      console.log(res);
    });
  }

  addComment(form: NgForm){
    let model = new BookAddCommentModel();
    model.bookID = this.bookId;
    model.userID = this.currentUser.id;
    model.comment = form.controls["comment"].value;

    this._bookService.addComment(model, res => {
      this._toastr.success("Your comment added succesfully.");
      this.getBookComments();
      form.reset();
    });
  }
}
