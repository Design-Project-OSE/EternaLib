import { Component, HostListener } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <router-outlet></router-outlet>
    <button *ngIf="isShow" (click)="gotoTop()">
      <i class="backtotop fa-solid fa-circle-chevron-up"></i>
    </button>
  `,
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = "frontend"

  isShow: boolean = false;
  topPosToStartShowing = 100;

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
