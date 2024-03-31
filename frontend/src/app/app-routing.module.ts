import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { LayoutsComponent } from './components/layouts/layouts.component';
import { HomeComponent } from './components/home/home.component';
import { ContentComponent } from './components/content/content.component';
import { ContentDetailComponent } from './components/content/content-detail/content-detail.component';
import { ProfileComponent } from './components/profile/profile.component';

const routes: Routes = [
  {
    path: "login",
    component: LoginComponent
  },
  {
    path: "",
    component: LayoutsComponent,
    children: [
      {
        path: "",
        component: HomeComponent
      },
      {
        path: "home",
        component: HomeComponent
      },
      {
        path: "content",
        component: ContentComponent,
      },
      {
        path: "content/detail/:id",
        component: ContentDetailComponent
      },
      {
        path: "profile",
        component: ProfileComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
