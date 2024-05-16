import { Component } from '@angular/core';
import { SharedModule } from '../../common/shared/shared.module';
import { HomePopularComponent } from '../../common/components/home-popular/home-popular.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [SharedModule, HomePopularComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

}
