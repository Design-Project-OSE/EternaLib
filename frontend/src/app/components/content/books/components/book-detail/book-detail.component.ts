import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './book-detail.component.html',
  styleUrl: './book-detail.component.scss'
})
export class BookDetailComponent {

  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }

}
