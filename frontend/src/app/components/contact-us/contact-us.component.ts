import { Component } from '@angular/core';
import { SharedModule } from '../../common/shared/shared.module';

@Component({
  selector: 'app-contact-us',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './contact-us.component.html',
  styleUrl: './contact-us.component.scss'
})
export class ContactUsComponent {

}
