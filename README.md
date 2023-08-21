# TIC TAC TOE

`[Low Level Design]` [Scaler]("https://github.com/scaleracademy/Skill-ShowDown-System-Design-Challenge")

## `Problem Statement`

    Create a Low-Level Design for a common TicTacToe game with the following constraints as shared.

```
  Input = 2 C C u1 X 3 || 2 C C u2 O 3 || 2 C u2 O 3
```
`Note -` *It is assumed that the input for computer should be like this. C C is recommended to write to represent a computer. But if there is only C then also it will handle computer. But no Symbol will we assign to the human player if not provided and it will validate and give warning accordingly.*

``` markdown
# Test cases I have considered.
```
<Pre>
    <a href="#case1">1. Validate Number of Players.</a>
    <a href="#case2">2. Validate Computer.</a>
    <a href="#case3">3. Undo</a>
    <a href="#case4">4. Validate Symbol</a>
    <a href="#case5">5. Validate PlayerID.</a>
</Pre>
<b id="case1">Case 1 -</b> `Validate Number of players`

```
    input = "2 u1 X u2 O 3"

Number of players is 2 so there should be only 2 player id and symbols. More than that will return warning.

    => "Number of players and playerID's are not matching"  
```

<b id="case2">Case 2 -</b> `Validate Computer`

```
    input = "3 C C u1 O C C 3"

Number of computer per match allowed is 1 only. So if there are 2 computers as a player return 
      
    => "No 2 Computers allowed"
```

<b id="case3">Case 3 -</b> `Undo`

```  
As only human player can undo so once a player done with his/her move then there will be a question after every human move - 
        => Whether you want to undo y/n : 
Output will be according to the user preference.
    =========================================
        if undo == y:
            the last move is undo.
        else:
            next player turn.
    =========================================
```

<b id="case4">Case 4 -</b> `Validate Symbol`

```
Each player must be assign a valid and unique symbol.

     => Symbol C is for computer only.

Symbols must be validated. 
If there are 2 players and only one player has symbol if it is a computer assign a symbol or else warn to re enter the player name and symbols.

    => 203: "Player Symbols are not unique",
```

<b id="case5">Case 5 -</b> `Validate PlayerId`

```
Each player have a valid player Id/Name. 
If there are 2 players both players should have unique playerID.
    => 204: "Player Id's are not unique",

Player name/id should not be a single character (min 2 characters)

    => Total_Players playerID Symbol boardSize:
        eg. 2 u1 O u2 X 3 : 2 u1 O u X 3
    =========================================================
    Player name/id should not be a single character (min 2 characters mandatory)
    =========================================================

```

## Approach

```markdown
1. All/Maximum input cases are considered.
2. Getting user input
3. Validating the input from the user.
4. Validating only One Computer is allowed per game.
5. Creating board as per the user input.
6. Displaying board
7. Player or Computer Turn.
8. Take input from user to fill the board.
9. No over fill is allowed. (only empty box filling is allowed.)
10. Draw Check
11. Winner Check
12. Undo.
```

## Error Codes
```py
ErrorCodes = {
    200: "No error",
    201: "There's a player without Symbol. Please Check your input",
    202: "No 2 Computers allowed",
    203: "Player Symbols are not unique",
    204: "Player Id's are not unique",
}
```

`File Structure`
<pre style="font-size: 14px" id="file">
├── <b style="font-size: 1.2em; color: crimson"><a style="color:inherit;" href="#file"># tic_tac_toe </a></b>
   ├── <b style="color: #25f;">main.py - </b>main file
   ├── <b>play.py</b>
   ├── <b>createboard.py</b>
   ├── <b>displayboard.py</b>
   ├── <b>defineplayer.py</b>
   ├── <b>playerturn.py</b>
   ├── <b>computerturn.py</b>
   ├── <b>draw.py</b>
   ├── <b>winner.py</b>
   ├── <b>undo.py</b>
   ├── <b>errorcodes.py</b>
   ├── <b>README.md</b> <i>(this file)</i>
</pre>

```
Q. How to Run this program?
```

    Clone this repo.
           |
    Make sure python is installed in your machine. (-v: 3.11.4)
           |
    Open the folder in your Code Editor
           |
    In the terminal Type - python main.py

`By - KARNAIL SINGH CHOUDHARY`

[Scaler Challenge]('https://github.com/scaleracademy/Skill-ShowDown-System-Design-Challenge')