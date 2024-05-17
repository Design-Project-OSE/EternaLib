import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class GenericHttpService {
  apiUrl: string = 'http://127.0.0.1:8000';

  constructor(
    private _http: HttpClient,
    private _toastr: ToastrService,
    private _spinner: NgxSpinnerService
  ) { }

  get<T>(url: string, callback: (res: T) => void){
    this._spinner.show();
    this._http.get<T>(`${this.apiUrl}/${url}`).subscribe({
      next: (res: T) => {
        callback(res);
        this._spinner.hide();
      },
      error: (err: HttpErrorResponse) => {
        console.log(err);
        this._toastr.error(err.error.message);
        this._spinner.hide();
      }
    });
  }

  post<T>(url: string, model: any, callback: (res: T) => void){
    this._spinner.show();
    this._http.post<T>(`${this.apiUrl}/${url}`, model, {}).subscribe({
      next: (res: T) => {
        callback(res);
        this._spinner.hide();
      },
      error: (err: HttpErrorResponse) => {
        console.log(err);
        this._toastr.error(err.error.message);
        this._spinner.hide();
      }
    });
  }
}
