import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-social-buttons',
  standalone: true,
  imports: [],
  templateUrl: './social-buttons.component.html',
  styleUrl: './social-buttons.component.scss'
})
export class SocialButtonsComponent {
  @Input() instagram: string = "";
  @Input() x: string = "";
  @Input() linkedin: string = "";
  @Input() facebook: string = "";
}
