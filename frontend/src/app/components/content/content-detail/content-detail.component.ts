import { Component, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DatabaseService } from '../../../services/database.service';
import { ContentComponent } from '../content.component';

@Component({
  selector: 'app-content-detail',
  templateUrl: './content-detail.component.html',
  styleUrl: './content-detail.component.scss'
})
export class ContentDetailComponent {

  route: ActivatedRoute = inject(ActivatedRoute);
  currentId = 1;
  movies: any[any];


  constructor(
    private _dbService: DatabaseService
  )
  {
    this.currentId = Number(this.route.snapshot.params['id']);
  }

  ngOnInit(): void {
    this.getMovies();
  }

  getMovies() {
    this._dbService.getMovies(res => this.movies = res);
  }
}
