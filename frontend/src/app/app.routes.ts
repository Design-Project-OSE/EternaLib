import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'login',
    loadComponent:
        () => import('./components/auth/components/login/login.component')
        .then(c => c.LoginComponent)
  },
  {
    path: 'register',
    loadComponent:
        () => import('./components/auth/components/register/register.component')
        .then(c => c.RegisterComponent)
  },
  {
    path: '',
    loadComponent:
        () => import('./components/layout/layout.component')
        .then(c => c.LayoutComponent),
    children: [
      {
        path: '',
        loadComponent:
            () => import('./components/home/home.component')
            .then(c => c.HomeComponent)
      },
      {
        path: 'profile',
        loadComponent:
            () => import('./components/profile/components/profile/profile.component')
            .then(c => c.ProfileComponent)
      },
      {
        path: 'about-us',
        loadComponent:
            () => import('./components/about-us/about-us.component')
            .then(c => c.AboutUsComponent)
      },
      {
        path: 'contact-us',
        loadComponent:
            () => import('./components/contact-us/contact-us.component')
            .then(c => c.ContactUsComponent)
      },
      {
        path: 'profile/edit',
        loadComponent:
            () => import('./components/profile/components/profile-edit/profile-edit.component')
            .then(c => c.ProfileEditComponent)
      },
      {
        path: 'movies',
        loadComponent:
            () => import('./components/content/movies/components/movies/movies.component')
            .then(c => c.MoviesComponent)
      },
      {
        path: 'movies/detail/:value',
        loadComponent:
            () => import('./components/content/movies/components/movie-detail/movie-detail.component')
            .then(c => c.MovieDetailComponent)
      },
      {
        path: 'games',
        loadComponent:
            () => import('./components/content/games/components/games/games.component')
            .then(c => c.GamesComponent)
      },
      {
        path: 'games/detail/:value',
        loadComponent:
            () => import('./components/content/games/components/game-detail/game-detail.component')
            .then(c => c.GameDetailComponent)
      },
      {
        path: 'books',
        loadComponent:
            () => import('./components/content/books/components/books/books.component')
            .then(c => c.BooksComponent)
      },
      {
        path: 'books/detail/:value',
        loadComponent:
            () => import('./components/content/books/components/book-detail/book-detail.component')
            .then(c => c.BookDetailComponent)
      }
    ]
  }
];
