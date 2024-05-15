import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { IsValidDirective } from '../directives/is-valid.directive';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective
  ],
  exports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective
  ]
})
export class SharedModule { }
