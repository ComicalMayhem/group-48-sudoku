# Sudoku-Project

## Fork Repository Instructions
### Steps:
1. When you go to the github repository we provided, on the top right hand corner of the screen, there is a button that says "Fork". That will fork the repo to your own github 
2. Use the link https://github.com/new/import to clone your forked repo to make it private. You will work on the project by adding your own files to this private repository.

# Group 48 Project Notes

I guess we can just use this repo as our main thing. Let's hope we don't run into too many merge conflicts. 

## Checklist to Completion
1. Button (probably just a rect) that resets the board state (reset_to_original function in Board class)
2. Binding Board.clear to some keypress. Maybe backspace or delete, or both. Essentially removing a sketched or placed number
3. Button to sumbit the board to the program. Leads to game lose or game win screen, probably should call Board.is_full, Board.find_empty, and Board.check_board. If it fails, maybe have something print to the pygame window and let the game continue?
4. Game over screen, with the result of the sudoku puzzle.
5. Idk if this is needed, but we could take all of sudoku.py, shove it into a main function inside of sudoku.py, then call the main function.

I've decided to be extra and make the window resizable, because it pisses me off when its not. I can do 1 and 3 if you don't want to deal with fixing a rect with respect to window size, though it shouldn't be too hard: the variable x should be bound to window width and y to window height. Multiplying these by some decimal should fix the position of a given rect relative to the window. Check how I did the easy, medium, and hard buttons for reference. 
