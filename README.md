# Blackjack Game

This project is a Python implementation of the classic Blackjack card game.

## Rules of the Game
- The deck is unlimited in size.
- There are no jokers.
- Jack, Queen, and King are each valued at 10 points.
- The Ace can be valued at either 11 or 1, depending on which value is most favorable to the player.
- The game uses the following deck of cards:  
  `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- Each card in the deck has an equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer plays the role of the dealer.

## Objective
- The objective is to draw cards to get as close to 21 as possible without exceeding it, while beating the dealer's score.

## Exercise Information
- This game is part of the exercises from the **100 Days of Code: The Complete Python Pro Bootcamp** on Udemy.

## How to Play
- Run the game in your Python environment.
- The game will deal cards to both the player and the dealer.
- The player must decide whether to "hit" (draw a card) or "stand" (keep their current hand).
- The game ends when the player or dealer goes bust (exceeds 21) or decides to stand.
