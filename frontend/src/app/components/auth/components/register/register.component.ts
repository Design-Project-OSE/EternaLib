import { Component } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [AuthComponent, SharedModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent {

  register(form: NgForm){
    if(form.valid){
      console.log(form.value);
      console.log(form.controls["name"].value);
      console.log(form.controls["email"].value);
      console.log(form.controls["password"].value);
    }
  }
}
