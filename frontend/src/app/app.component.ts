import { CommonModule } from '@angular/common';
import { Component, HostListener, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NgxSpinnerModule } from 'ngx-spinner';
import { AuthService } from './components/auth/services/auth.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, NgxSpinnerModule],
  template: `
    <router-outlet></router-outlet>
    <button class="backtotop" *ngIf="isShow" (click)="gotoTop()">
      <i class="fa-solid fa-circle-chevron-up"></i>
    </button>
    <ngx-spinner bdColor = "rgba(0, 0, 0, 0.8)" type = "loading-screen" [fullScreen] = "true">
      <div class="🤚">
        <div class="👉"></div>
        <div class="👉"></div>
        <div class="👉"></div>
        <div class="👉"></div>
        <div class="🌴"></div>
        <div class="👍"></div>
    </div>
    </ngx-spinner>
  `,
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  isShow: boolean = false;
  topPosToStartShowing = 100;

  constructor(
    private _auth: AuthService
  ){}

  ngOnInit(): void {
    if(typeof localStorage != 'undefined'){
      if(localStorage.getItem("user")){
        this._auth.isLoggedIn = true;
      } else {
        this._auth.isLoggedIn = false;
      }
    }
  }

  @HostListener('window:scroll')
  checkScroll() {
    const scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;

    if (scrollPosition >= this.topPosToStartShowing) {
      this.isShow = true;
    } else {
      this.isShow = false;
    }
  }

  gotoTop() {
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  }
}
