import { Component, OnInit } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';
import { AuthService } from '../../services/auth.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [AuthComponent, SharedModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnInit {

  constructor(
    private _auth: AuthService,
    private _toastr: ToastrService
  ) { }

  ngOnInit() {
    this._auth.isHomePage = false;
  }

  login(form: NgForm){
    if(form.valid){
      console.log(form.value)
      console.log(form.controls["email"].value);
      console.log(form.controls["password"].value);
    } else {
      if(form.controls["email"].invalid){
        this._toastr.error('Please enter a valid email');
      } else {
        this._toastr.error('Please enter a password');
      }
    }
  }

}
