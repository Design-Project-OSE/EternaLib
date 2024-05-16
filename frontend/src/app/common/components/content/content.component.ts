import { Component, Input } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';

@Component({
  selector: 'app-content',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './content.component.html',
  styleUrl: './content.component.scss'
})
export class ContentComponent {
  @Input() question: string = "";
  @Input() contentTypee: string = "";
  @Input() categoriess: string[] = [];
}
