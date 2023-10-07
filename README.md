# Othello AI Game

Welcome to the Othello AI Game repository! This project showcases an interactive Othello (also known as Reversi) game where you can challenge a sophisticated AI opponent. The AI logic utilizes the minimax algorithm, ensuring a thrilling and challenging game experience. Dive in and see if you can outsmart the machine!

## Features

1. **Customized GUI**: Built from scratch, offering a clean and intuitive game interface.
2. **Standalone executable**: Easily play the game without the need for external dependencies.
3. **High-resolution images**: Enhances the game's visual aesthetics.
4. **Robust AI**: Implemented using the minimax algorithm, tailored to provide a formidable challenge.

## Repository Structure

- `Board.py`: Handles the logic and visual representation of the game board.
- `Button.py`: Manages the functionality and design of in-game buttons.
- `Piece.py`: Represents the game pieces and their movements.
- `graphics.py`: Contains various graphics-related utilities and resources.
- `Othello.py`: The main game script, where everything comes together.

## How to Play
- Player's toss a coin to decide who will play first. Each turn, the player places one piece on the board with their colour facing up.

- For the first four moves, the players must play to one of the four squares in the middle of the board and no pieces are captured or reversed.

- Each piece played must be laid adjacent to an opponent's piece so that the opponent's piece or a row of opponent's pieces is flanked by the new piece and another piece of the player's colour. All of the opponent's pieces between these two pieces are 'captured' and turned over to match the player's colour.

- It can happen that a piece is played so that pieces or rows of pieces in more than one direction are trapped between the new piece played and other pieces of the same colour. In this case, all the pieces in all viable directions are turned over.

- The game is over when neither player has a legal move (i.e. a move that captures at least one opposing piece) or when the board is full.

Source: https://www.mastersofgames.com/rules/reversi-othello-rules.htm

## Rules
- In Othello, the two colours are Black and White and Black always plays first
- In Othello, the four squares in the middle of the board start with four counters already placed - white top left and bottom right; black top right and bottom left. The reason for this is that In Reversi, the extra freedom can result in an opening that produces a less interesting game
  
Source: https://www.mastersofgames.com/rules/reversi-othello-rules.htm


### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/AmbitiousCommitte/Othello.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd [Repository Directory Name]
   ```
3. Run the Othello game:
   a.Option 1:
   -  Do this by click the Executable file

   b. Option 2:
   - Open the Othello.py and run the code
  
     
## How to Contribute

1. Fork this repository.
2. Clone your fork.
3. Create a new branch for your changes.
4. Implement and test your changes.
5. Push your changes to your fork on GitHub.
6. Create a pull request from your fork to this repository.


## Things could be added/ improve

- Make the game accessible online / through web
- Develope a better AI system
- Make it available for 1 vs 1 
---

Enjoy the game and good luck outsmarting the AI! If you have any feedback, issues, or suggestions, please open an issue or submit a pull request.
