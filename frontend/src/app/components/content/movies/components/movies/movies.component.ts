import { Component, OnInit } from '@angular/core';
import { ContentComponent } from '../../../../../common/components/content/content.component';
import { SharedModule } from '../../../../../common/shared/shared.module';
import { MovieService } from '../../services/movie.service';
import { MovieModel } from '../../models/movie.model';
import { CategoryModel } from '../../../models/category.model';
import { SearchModel } from '../../../../../common/models/search.model';
import { SearchService } from '../../../../../common/services/search.service';
import { NgxPaginationModule } from 'ngx-pagination';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [SharedModule, ContentComponent, NgxPaginationModule],
  templateUrl: './movies.component.html',
  styleUrl: './movies.component.scss'
})
export class MoviesComponent implements OnInit {
  movies: MovieModel[] = [];
  categories: CategoryModel[] = [];
  selectedCategory: string = "All";

  search: SearchModel = new SearchModel();

  pageNumber: number = 1;
  pageSize: number = 10;

  constructor(
    private _movieService: MovieService,
    private _searchService: SearchService
  ){}

  ngOnInit(): void{
    this.getMovies("");
    this.getAllCategoriesForMovies();
  }

  getMovies(query: string, categoryId: string = "All"){
    this.search.searchterm = query;

    if(this.selectedCategory == "All"){
      if(query == ""){
        this._movieService.getMovies(res => {
          this.movies = res;
        });
      } else {
        this._searchService.search(this.search, res => {
          this.movies = res.movies;
        });
      }
    } else {
      this._movieService.getMoviesByCategoryId(categoryId, res => {
        this.movies = res;
      });
    }
  }

  getAllCategoriesForMovies(){
    this._movieService.getAllCategoriesForMovies(res => {
      this.categories = res;
    });
  }
}
