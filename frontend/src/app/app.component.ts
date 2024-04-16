import { Component, HostListener } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <router-outlet></router-outlet>
    <button class="backtotop" *ngIf="isShow" (click)="gotoTop()">
      <i class=" fa-solid fa-circle-chevron-up"></i>
    </button>
    <ngx-spinner bdColor = "rgba(0, 0, 0, 0.8)" size = "medium" color = "#fff" type = "square-jelly-box" [fullScreen] = "true"><p style="color: white" > Please wait... </p></ngx-spinner>
  `,
  styleUrl: './app.component.scss'
})
export class AppComponent {

  // Sayfanın en üstüne scroll yapmak için
  // constructor(private router: Router) {
  //   this.router.events.subscribe(event => {
  //     if (event instanceof NavigationEnd) {
  //       window.scrollTo(0, 0);
  //     }
  //   });
  // }

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
