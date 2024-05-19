import { Component, OnInit } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';
import { AuthService } from '../../services/auth.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [AuthComponent, SharedModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent implements OnInit {

  constructor(
    private _auth: AuthService,
    private _toastr: ToastrService
  ) { }

  ngOnInit() {
    this._auth.isHomePage = false;
  }

  register(form: NgForm){
    if(form.valid){
      console.log(form.value);
      console.log(form.controls["name"].value);
      console.log(form.controls["email"].value);
      console.log(form.controls["password"].value);
    } else {
      this._toastr.error('Please fill all the required fields');
    }
  }
}
