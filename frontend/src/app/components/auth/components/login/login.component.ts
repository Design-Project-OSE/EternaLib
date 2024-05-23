import { Component, OnInit } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';
import { AuthService } from '../../services/auth.service';
import { ToastrService } from 'ngx-toastr';
import { LoginModel } from '../../models/login.model';
import { Router } from '@angular/router';

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
    private _toastr: ToastrService,
    private _router: Router
  ) { }

  ngOnInit() {
    this._auth.isAuthPages = true;
  }

  login(form: NgForm){
    if(form.valid){
      let model = new LoginModel();
      model.email = form.controls["email"].value;
      model.password = form.controls["password"].value;

      this._auth.login(model, res => {
        console.log(res);

        this._toastr.success(`Welcome ${res.full_name}`, "Login Successful!");

        localStorage.setItem("user", JSON.stringify(res));

        let redirectUrl = sessionStorage.getItem('redirectAfterLogin');
        if (redirectUrl) {
            sessionStorage.removeItem('redirectAfterLogin');
            window.location.href = redirectUrl;
        } else {
          this._router.navigateByUrl("/");
        }

        this._auth.isLoggedIn = true;
      });
    }
  }
}
