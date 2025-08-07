# CSPB3308_Term-Project_Team1

# Page_Testing
This Markdown will include a description for the pages we plan to implement for our project. 

## Home Page
**Page Title:** Home | Space Adventurers Prime game

**Page Description:** This page will be the main front page that will explain what the game is, some slight background and the link to start the game (Game Page)

**Parameters Needed:** homePageTitle, gameTitle, homePageBackgroundText, gamePageTitle, AboutPageTitle, 

<img width="755" height="1213" alt="Screenshot 2025-07-15 192746" src="https://github.com/user-attachments/assets/1f705604-a4db-411d-a1f4-491658321fa6" />

**Data Needed for Render:** The home page is the very first thing you see when attempting to play Space Adventurers Prime, there is no information needed to render this page, like there would be for example for each choice iteration.

**Link Destination:** Link to Game Page, Link to About page

## About Page
**Page Title:** About

**Page Description:** This page will include a brief description of what our game is about and why we decided to make this game. In addition, we will include each member of our team in the "Meet the Team" section
![Figma_Screenshot_About](images/figma_about.png)

**Parameters Needed:** Needs title, headline, subHeadline, aboutBodyText, teamHeadline, teamMembers, startButton, aboutButton, homeButton, backgroundImage, fontSetting

**Data Needed for Render:** I will need to include a header section that includes a button that takes us to the "about" and "home" page, as well as a button that "Start Game". 

**Link Destination:** unsure of the link yet, but about should include /about

## Game Page
**Page Title:** Game Page

**Page Description:**
This is the main interactive page for players to play the game.
It displays the current story node text and the choices the player can make.

![GAME_PAGE](images/Game_Page.png)

**Parameters Needed:**
- `node_id` (passed as a URL parameter):  
  This is the current story node to render, e.g.  
  `/node/checkpoint1`

---
**Data Needed for Render:**
From the story JSON file:
- The current node's `text`
- The list of `choices`
- Each choice's `target` node ID

**Link Destination:**
Each choice links to another game page (another story node) using the format:  
`/node/<target_node_id>`

**Examples:**
- `/node/checkpoint11`
- `/node/checkpoint12`

If the user wins or loses, it should redirect the user to the game win/lose page.

**Tests:**

- The page loads correctly when a valid `node_id` is given  
- The correct story text shows up
- All choices appear as links  
- Clicking a choice navigates to the correct next node  
- An error message or redirect pops up if a bad `node_id` is provided  

## Game_Win Page
**Page Title:** You Won!

**Page Description:** This page will be the final page a player sees when they select all the correct choices and win the game. See win_page.png in images folder.

**Parameters Needed:**  /won

**Data Needed for Render:**  Each individual user choices which will lead to this final page.

**Link Destination:** Unavailable as we work on this step. This page will link to allow the user to start the game again if they want to play a second round. 
![Win Page](images/win_page.png)

## Game_Lose Page
**Page Title:** You Died. or You Lost.

**Page Description:** This page will be the final page a user sees when they select an incorrect choice and die in the game. 
![Win Page](images/lose_page.png)

**Parameters Needed:**  /lost

**Data Needed for Render:** The specific choice that leads to the character's death. This will be one of the users previous choices.

**Link Destination:** Unavailable as we work on this step. This page will link to allow the user to start the game again if they want to play a second round. 

