import { Component, Input } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { SafeUrlPipe } from '../../pipes/safe-url.pipe';

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
  @Input() categories: string[] = [];
  @Input() trailer: string = "";
  @Input() bgImage: string = "";
  @Input() likeCount: string = "";
  @Input() poster: string = "";

  @Input() userRouteUrl: string = "";
  @Input() userName: string = "";
  @Input() userImage: string = "";
  @Input() userComment: string = "";
  @Input() userCommentDate: string = "";
}
