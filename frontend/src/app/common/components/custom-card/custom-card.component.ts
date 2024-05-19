import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-custom-card',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './custom-card.component.html',
  styleUrl: './custom-card.component.scss'
})
export class CustomCardComponent {
  @Input() name: string = "";
  @Input() imageUrl: string = "";
  @Input() routerUrl: string = "";
  @Input() likeCount: string = "";
  @Input() commentCount: string = "";
}
