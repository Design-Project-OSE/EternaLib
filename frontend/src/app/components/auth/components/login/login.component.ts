import { Component } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [AuthComponent, SharedModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {

  login(form: NgForm){
    if(form.valid){
      console.log(form.value)
      console.log(form.controls["email"].value);
      console.log(form.controls["password"].value);
    }
  }

}
