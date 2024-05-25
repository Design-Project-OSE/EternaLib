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
import { SwalService } from '../../../../../common/services/swal.service';

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

  isLiked: boolean;
  isDisliked: boolean;

  currentUser = this._authService.getCurrentUser(); // mevcut kullanıcıyı tutacak

  constructor(
    private _bookService: BookService,
    private _toastr: ToastrService,
    private _swal: SwalService,
    private _authService: AuthService,
    private _activates: ActivatedRoute
  ){
    this._activates.params.subscribe(res => {
      this.bookUrl = res["url"];
      this.getBookByUrl()
          .then(() => {
              this.getBookComments();
              this.getBookLikesAndDislikes();
          });
    });
  }


  getBookByUrl(): Promise<void> {
    return new Promise((resolve, reject) => {
      this._bookService.getBookByUrl(this.bookUrl, res => {
        this.book = res;
        this.bookId = res.id;

        for (let i = 0; i < this.book.categories.length; i++) {
          this.getCategoryById(this.book.categories[i]);
        }

        resolve();
      });
    });
  }

  getCategoryById(categoryId: any){
    this._bookService.getCategoryById(categoryId, res => {
      if (!this.bookCategories.some(category => category.id === categoryId)) {
        this.bookCategories.push(res);
      }
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
    this._authService.IsUserLoggedIn("like this book");

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
    this._authService.IsUserLoggedIn("dislike this book");

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
    this._authService.IsUserLoggedIn("comment this book");

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

  deleteComment(commentId: string, userId: string){
    let model = {
      commentID: commentId,
      userID: userId
    };

    this._swal.callSwall(`Are you sure you want to delete the comment?`,"Delete Comment", "Delete", () =>
      {
        this._bookService.deleteComment(model, res => {
          this._toastr.success(res.message);
          this.getBookComments();
        });
      });
  }
}
