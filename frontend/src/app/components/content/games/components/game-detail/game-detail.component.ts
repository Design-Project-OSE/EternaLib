import { Component } from '@angular/core';
import { ContentDetailComponent } from '../../../../../common/components/content-detail/content-detail.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-game-detail',
  standalone: true,
  imports: [ContentDetailComponent, SharedModule],
  templateUrl: './game-detail.component.html',
  styleUrl: './game-detail.component.scss'
})
export class GameDetailComponent {

  sendComment(form: NgForm){
    console.log(form.value);
    console.log(form.controls["comment"].value);
  }
}
