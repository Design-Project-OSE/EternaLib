import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { IsValidDirective } from '../directives/is-valid.directive';
import { CustomCardComponent } from '../components/custom-card/custom-card.component';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective,
    CustomCardComponent
  ],
  exports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective,
    CustomCardComponent
  ]
})
export class SharedModule { }
