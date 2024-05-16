import { Component } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [AuthComponent],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {

}
