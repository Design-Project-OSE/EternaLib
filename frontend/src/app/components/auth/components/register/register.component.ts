import { Component } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [AuthComponent],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent {

}
