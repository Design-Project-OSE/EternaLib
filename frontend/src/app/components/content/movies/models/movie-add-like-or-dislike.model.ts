export class MovieAddLikeOrDislikeModel{
  userID: string = "";
  movieID: string = "";
  like: boolean;
  dislike: boolean;
}

// like butonuna basıldığında like=true
// dislike butonuna basıldığında ise dislike=true
// yapılarak ilgili adrese istek atılacak

// Butonlara tekrar basıldığında ise like=false ve dislike=false yapılacak
