export class BookAddLikeOrDislikeModel{
  userID: string = "";
  bookID: string = "";
  like: boolean = false;
  dislike: boolean = false;
}

// like butonuna basıldığında like=true
// dislike butonuna basıldığında ise dislike=true
// yapılarak ilgili adrese istek atılacak
