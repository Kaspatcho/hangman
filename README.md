# Hangman
Jogo da forca feito com flask e js

![Exemplo](https://cdn.discordapp.com/attachments/746454307163078718/881667034784612402/unknown.png "jogo de site")


## retorno API flask
``` python
{
    "current_game": str, # string do jogo atual
    "error_count": int, # quantidade de erros
    "is_game_over": bool,
    "is_game_won": bool,
    "tip": str, # dica pro jogo
    "total_letters": int
}
```
