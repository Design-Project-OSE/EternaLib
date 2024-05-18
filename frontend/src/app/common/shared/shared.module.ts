import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { IsValidDirective } from '../directives/is-valid.directive';
import { CustomCardComponent } from '../components/custom-card/custom-card.component';
import { AnimatedButtonComponent } from '../components/animated-button/animated-button.component';
import { SocialButtonsComponent } from '../components/social-buttons/social-buttons.component';



@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective,
    CustomCardComponent,
    AnimatedButtonComponent,
    SocialButtonsComponent
  ],
  exports: [
    CommonModule,
    FormsModule,
    RouterModule,
    IsValidDirective,
    CustomCardComponent,
    AnimatedButtonComponent,
    SocialButtonsComponent
  ]
})
export class SharedModule { }
