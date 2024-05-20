export class MovieLikesAndDislikesModel{
  data: {
    id: string
    userID: string
    movieID: string
    like: number
    dislike: number
    savedate: string
  }
  like: number = 0;
  dislike: number = 0;
}
