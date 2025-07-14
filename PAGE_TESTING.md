# Game Page

## Description
This is the main interactive page for players to play the game.
It displays the current story node text and the choices the player can make.

---

### Layout Includes:
- A title (Adventure Game)
- Story Text
- Links for the players to make their choices.
---

### Mockup

    +--------------------------------------------------+
    |                [Adventure Game]                  |
    |                                                  |
    |  Story text: "You walk into a dark forest..."    |
    |                                                  |
    |  [Choice A: Enter the cave]                      |
    |  [Choice B: Climb the tree]                      |
    +--------------------------------------------------+

    
---

## Parameters

- `node_id` (passed as a URL parameter):  
  This is the current story node to render, e.g.  
  `/node/checkpoint1`

---

## Data Needed

From the story JSON file:
- The current node's `text`
- The list of `choices`
- Each choice's `target` node ID

---

## Link Destinations

Each choice links to another game page (another story node) using the format:  
`/node/<target_node_id>`

**Examples:**
- `/node/checkpoint11`
- `/node/checkpoint12`

---

## Tests

- The page loads correctly when a valid `node_id` is given  
- The correct story text shows up
- All choices appear as links  
- Clicking a choice navigates to the correct next node  
- An error message or redirect pops up if a bad `node_id` is provided  
