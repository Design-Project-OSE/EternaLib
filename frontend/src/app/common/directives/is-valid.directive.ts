import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appIsValid]',
  standalone: true
})
export class IsValidDirective {
  @Input() appIsValid: boolean = false;

  constructor(
    private _el: ElementRef<any>
  ) { }

  @HostListener('keyup') keyup(){
    if(this.appIsValid){
      this._el.nativeElement.className = "form-control is-valid";
    } else{
      this._el.nativeElement.className = "form-control is-invalid";
    }
  }
}
