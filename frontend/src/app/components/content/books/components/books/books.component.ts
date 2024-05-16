import { Component } from '@angular/core';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { ContentComponent } from '../../../../../common/components/content/content.component';

@Component({
  selector: 'app-books',
  standalone: true,
  imports: [SharedModule, ContentComponent],
  templateUrl: './books.component.html',
  styleUrl: './books.component.scss'
})
export class BooksComponent {

}
