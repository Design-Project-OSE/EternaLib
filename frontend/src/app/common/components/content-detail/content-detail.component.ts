import { Component, Input } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { SafeUrlPipe } from '../../pipes/safe-url.pipe';
import { CategoryModel } from '../../../components/content/models/category.model';

@Component({
  selector: 'app-content-detail',
  standalone: true,
  imports: [SharedModule, SafeUrlPipe],
  templateUrl: './content-detail.component.html',
  styleUrl: './content-detail.component.scss'
})
export class ContentDetailComponent {
  @Input() name: string = "";
  @Input() release: string = "";
  @Input() description: string = "";
  @Input() imdb: string = "";
  @Input() metacritic: string = "";
  @Input() categories: CategoryModel[] = [];
  @Input() trailer: string = "";
  @Input() bgImage: string = "";
  @Input() poster: string = "";
}
