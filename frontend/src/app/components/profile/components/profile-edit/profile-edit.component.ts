import { Component } from '@angular/core';
import { SharedModule } from '../../../../common/shared/shared.module';
import { NgForm } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-profile-edit',
  standalone: true,
  imports: [SharedModule],
  templateUrl: './profile-edit.component.html',
  styleUrl: './profile-edit.component.scss'
})
export class ProfileEditComponent {
  constructor(
    private _toastr: ToastrService
  ){}

  editProfile(form: NgForm){
    if(form.valid){
      console.log(form.value);
      form.reset();
    } else {
      this._toastr.error('Please fill all the required fields');
    }
  }
}
