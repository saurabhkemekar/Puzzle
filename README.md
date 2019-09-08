# Puzzle
### Sudoku generator and solver and blackjack game

#### Sudoku generator 
First of all, the first row is filled with randomly arranged numbers from 1 to 9. Then the second row is filled by shifting the first row by 3 blocks. Similarly, the third row is filled by shifting the second row by 3 blocks in the same direction as previous. Thus a 3x3 box contains every number uniquely. The fourth and seventh rows are filled by shifting its previous row by 1 block. Remaining rows are filled by shifting their preceding row by 3 blocks. Thus every row, column, and 3x3 box contains a number only once. Now whole 9x9 sudoku is filled with numbers, hence a solution of is generated. Now we ask the user what should be the difficulty of sudoku. According to the difficulty we delete random numbers from sudoku. Harder the difficulty more numbers get deleted. Here deleted means replaced by zero. Hence sudoku is generated according to difficulty set by the user.

#### Sudoku solver
1) For solving a sudoku, we need to find an empty block. A function is defined which searches for 0 in sudoku and returns its row and column number.
2) Then one number starting from 1 to 9 is checked whether it is present in that row, column & 3x3 box. Three functions are defined for specially checking whether a number is present in a specific row, column & 3x3 box. 
3) If it is present in any of them then for the next number the same conditions are checked. Else the number is assigned in that block. Then the next empty block is searched and same process is followed.
4) If there is a block in which neither of the 9 numbers can be  assigned, then we go to the previous block in which number was assigned. and we check for  another number is possible in there we assign that number and again check for an empty block. Else we again go back to its preceding block in which number was assigned and change the number. 
5) This process is continued until the sudoku is solved. When a function cannot find zero in sudoku, we conclude that sudoku is solved completely and we print the solution and exit from the code.

### Result

 ##### sudoku generator ---------------------->-------- ---------------> ----------------------> Sudoku solver

    |0 0 8 |0 7 2 |6 0 0                                                  |3 9 8 |5 7 2 |6 1 4                                              
    |5 7 0 |0 1 4 |0 0 8                                                  |5 7 2 |6 1 4 |3 9 8 
    |0 1 0 |0 0 8 |5 7 0                                                  |6 1 4 |3 9 8 |5 7 2 
    ____________________                                                  _____________________ 
    |1 0 0 |9 8 5 |0 0 6                                                  |1 4 3 |9 8 5 |7 2 6                                                  
    |0 0 0 |7 0 6 |0 0 0                                                  |9 8 5 |7 2 6 |1 4 3  
    |0 2 0 |1 0 0 |9 8 0                                                  |7 2 6 |1 4 3 |9 8 5 
    ____________________                                                  ______________________
    |0 6 1 |4 0 0 |0 5 0                                                  |2 6 1 |4 3 9 |8 5 7  
    |4 0 0 |0 0 7 |2 0 1                                                  |4 3 9 |8 5 7 |2 6 1 
    |0 0 0 |0 0 1 |4 3 9                                                  |8 5 7 |2 6 1 |4 3 9   
    
    
   
   
  ### Black jack
 1) For the blackjack game, we store the player's data using a list of dictionaries, with each dictionary storing each player’s name, hands, bets, profits and so on.
 2) Then Each player is asked the amount that he would like to bet. Then we choose two cards randomly from a list for each player using the random module. 
3) The player is then asked to make his move, ie to hit, double down, stand or split. For splitting, we use two recursive function calls(one for each split hand) and for hitting, we use a single recursive function call. After the player has finished his move(either by standing, getting busted or a blackjack), the dealer makes his move according to the rules. 
4) Then, profits for each hand of each player is calculated and appended to the profit list of each player. Then the player is asked whether he wants to play another game. If he chooses, he can play another round or he could quit the game. If he quits the game, total profit or total loss(whatever may be the case) is displayed for each player. 


    
    
