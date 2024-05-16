import { Component, Input } from '@angular/core';
import { NavbarComponent } from '../../../components/layout/navbar/navbar.component';
import { FooterComponent } from '../../../components/layout/footer/footer.component';
import { SharedModule } from '../../shared/shared.module';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [SharedModule, NavbarComponent, FooterComponent],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.scss'
})
export class AuthComponent {
  @Input() loginOrRegister: string = "";
  @Input() routeUrl: string = "";
  @Input() leftText: string = "";
}
