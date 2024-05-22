export class GameAddLikeOrDislikeModel{
  userID: string = "";
  gameID: string = "";
  like: boolean;
  dislike: boolean;
}

// like butonuna basıldığında like=true
// dislike butonuna basıldığında ise dislike=true
// yapılarak ilgili adrese istek atılacak
