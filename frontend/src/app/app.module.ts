import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LayoutsComponent } from './components/layouts/layouts.component';
import { LoginComponent } from './components/login/login.component';
import { NavbarComponent } from './components/layouts/navbar/navbar.component';
import { FooterComponent } from './components/layouts/footer/footer.component';
import { LoginFormComponent } from './components/login/login-form/login-form.component';
import { RegisterFormComponent } from './components/login/register-form/register-form.component';
import { LoginNavbarComponent } from './components/login/login-navbar/login-navbar.component';
import { LoginFooterComponent } from './components/login/login-footer/login-footer.component';
import { ContentComponent } from './components/content/content.component';
import { ContentDetailComponent } from './components/content/content-detail/content-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LayoutsComponent,
    LoginComponent,
    NavbarComponent,
    FooterComponent,
    LoginFormComponent,
    RegisterFormComponent,
    LoginNavbarComponent,
    LoginFooterComponent,
    ContentComponent,
    ContentDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
