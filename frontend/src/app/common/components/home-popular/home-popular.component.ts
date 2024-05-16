import { Component, Input } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';

@Component({
  selector: 'app-home-popular',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './home-popular.component.html',
  styleUrl: './home-popular.component.scss'
})
export class HomePopularComponent {
  @Input() routerUrl: string = "";
  @Input() contentType: string = "";
  @Input() iconClass: string = "";
}
