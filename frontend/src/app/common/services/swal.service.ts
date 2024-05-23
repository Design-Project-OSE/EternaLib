import { Injectable } from '@angular/core';
import Swal from 'sweetalert2';

@Injectable({
  providedIn: 'root'
})
export class SwalService {

  callSwall(text: string, title: string, btnName: string, callback: () => void){
    Swal.fire({
      text: text,
      title: title,
      showConfirmButton: true,
      confirmButtonText: btnName,
      showCancelButton: true,
      cancelButtonText: 'Cancel',
      icon: 'warning',
      confirmButtonColor: "#d33",
      cancelButtonColor: "rgb(249, 99, 50)",
      color: "#4940d4",
      background: "#fff url('/assets/img/swalbg.jpg')",
      backdrop: "rgba(0,0,123,0.4)"
    })
    .then(res => {
      if(res.isConfirmed){
        callback();
      }
    });
  }
}
