import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../../common/shared/shared.module';

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './movie-detail.component.html',
  styleUrl: './movie-detail.component.scss'
})
export class MovieDetailComponent {

  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
