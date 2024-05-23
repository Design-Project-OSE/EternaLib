import { Component, OnInit } from '@angular/core';
import { AuthComponent } from '../../../../common/components/auth/auth.component';
import { NgForm } from '@angular/forms';
import { SharedModule } from '../../../../common/shared/shared.module';
import { AuthService } from '../../services/auth.service';
import { ToastrService } from 'ngx-toastr';
import { RegisterModel } from '../../models/register.model';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [AuthComponent, SharedModule],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent implements OnInit {
  model: RegisterModel = new RegisterModel();

  constructor(
    private _auth: AuthService,
    private _toastr: ToastrService,
    private _router: Router
  ) { }

  ngOnInit() {
    this._auth.isAuthPages = true;
  }

  register(form: NgForm){
    if(form.valid){
      this._auth.register(this.model, res => {
        console.log(res);
        this._toastr.success(`Welcome ${res.full_name}`, "Registration Successful!");

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
