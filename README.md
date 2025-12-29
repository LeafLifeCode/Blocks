# Introduction:
This simple games uses turtle module in python. The objects used include:
1. **Intractive objects**
  - Ball
  - Player
  - Blocks

2. **Drawing objects**
  -Score
  -Border

# Functions of objects:
1. **Player**
  Represents the paddle
  Moves horizontally
  Stores:
    - score
    - lives

3. **Ball**
   Moves continuously using velocity (bx, by)
   Bounces off:
     - Wall
     - Paddle
     - Blocks
   Resets position when it falls below the screen

3. **Blocks (Obj)**
Randomly placed bricks
Different types with varying durability:
  1-hit(Green)
  2-hit(Orange)
  3-hit blocks(Pink)
Disappear when durability reaches zero

4. **Border**
Draws the game boundary

5. **Score**
Displays:
  - Current score
  - Remaining lives
Handles:
  - Score updates
  - Life reduction
  - Game Over screen

# Controls:
|-----------------| --------------------------------------|
| Key             | Action                                |
|-----------------|---------------------------------------|
| **LeftArrow**   | Move paddle to the left               |
| **Right Arrow** | Move paddle to the right              |
| **Mouse Click** | Exit game after Game Over             |
|-----------------|---------------------------------------|

# Gameplay Process:
The game window initializes with borders, paddle, ball, and blocks.
1. Blocks are placed randomly without overlapping.
2. The ball starts moving automatically.
3. Player moves the paddle left or right to keep the ball in play.

**When the ball:**
  - Hits the paddle → it bounces upward
  - Hits a wall → it reflects
  - Hits a block → the block loses durability and score increases

**If the ball falls below the paddle:**
  - Player loses one life and it is updated on screen by Score.
  - Ball resets to the center

**If all the blocks are destroyed:**
  - Ball reset to center
  - Ball speed increases
  - Blocks reappear

**The game ends when:**
  - Player runs out of lives
  - A Game Over message is displayed
