# CSPB3308_Term-Project_Team1

# SQL_TESTING
In this milestone, we are designing our database, including the descriptions of our tables, fields within the tables, and our data access methods for each. In addition to this, we will include tests for the access methods. 

## User

**About Table**

Table Name: User Table Information

Table Description: A table to store key user information including their pin for online play and username/password

Fields: (include name and description of each)
    Field: Pin Code - this will be where the 4 digit pin code number for User is stored for online play
    Field: Username - this will be where the username for the individual is stored. No special characters.
    Field: Passcode - this will be where the passcode for the individual is stored. Must include one capital letter and one special character.
**Data Access Method**

Name: Function to check pin code - checkPin

Description: A function that validates the users pin code matches what is stored in the database

Parameters: username, pin code

Return Values: true if pin matches, false if pin doesn't match

List of tests to verify access methods:
Test 1: Ensures the pin is a 4 digit pin that matches pin stored in database
    Test 1 precondition: User must have valid 4 digit pin
    Test 1 steps: 
        1. User navigates to login page
        2. User provides valid username
        3. User provides valid passcode
        4. User provides valid 4 digit to access online play
    Test 1 Expected Result: User should access online play
    Test 1 Actual Result: User is able to access the online play dashboard to play the game against friends.
    Test 1 Status: Pass
    Test 1 post-condition: User pin code is validated in system for future use.

Name: Function to check username is valid

Description: A function that validates the username by an individual

Parameters: username

Return Values: true if username is valid, false if username is invalid

List of tests to verify access methods:
Test 1: Ensures the username is a valid username
    Test 1 precondition: User be on the login page to sign up for an account
    Test 1 steps: 
        1. User navigates to sign up page
        2. User enters username without special characters
        3. User creates account 
    Test 1 Expected Result: User should access the game
    Test 1 Actual Result: User is able to access the game
    Test 1 Status: Pass
    Test 1 post-condition: Username is valid for future login attempts

Name: Function to check password is valid which includes one capital letter and one special character

Description: A function that validates the password set by an individual

Parameters: password

Return Values: true if password is valid, false if password is invalid

List of tests to verify access methods:
Test 1: Ensures the password is a valid password
    Test 1 precondition: User be on the login page to sign up for an account
    Test 1 steps: 
        1. User navigates to sign up page
        2. User enters password with one capital letter and one special character
        3. User creates account
    Test 1 Expected Result: User should access the game
    Test 1 Actual Result: User is able to access the game
    Test 1 Status: Pass
    Test 1 post-condition: Password is valid for future login attempts
## Choices

**About Table**

Table Name: `Choices`

Table Description:
This table stores the full path of choices made by each user during a game session. Each entry is identified by the user’s ID.

Fields:

| Field Name | Description                               |
|------------|-------------------------------------------|
| `user_id`  | The ID of the user. This is primary key       |
| `full_path`| The complete list of all choices taken in order by the user. |

**Data Access Method**

Name: `get_choices_by_user`

Description:
Returns the full path of choices taken by a given user.

Parameters:
- `user_id` (INTEGER): The ID of the user whose choices is to be retrieved.

Return Values:
- A list of full path strings (TEXT) representing the choices made by that user.

List of tests to verify access methods:

**Use case name**: Fetch full path taken by a user

Description: Verify that the full path of choices made by a user is correctly returned from the database.

Pre-conditions: The user has played at least one session (either completed or aborted).

Test steps:
1. A user plays the game and either completes it or aborts it.
2. The application stores the full_path into the Choices table using the user’s user_id.
3. Call get_choices_by_user(user_id)
4. Returned path should matche what the user actually chose.

Expected result: All full_path records for the users are correctly returned.

Actual result: To be filled

Status: Pass/Fail

Post-conditions: N/A
## Global Statistics

**About Table**

Table Name: GlobalStatistics

Table Description:stores aggregated statistics for every user who has played our game, game outcomes and participation for all game users, used to track overall user activity, performance and statistics between every iteration of the game.

Fields: (include name and description of each)
numWin: (INTEGER, Default: 0)
The total number of wins recorded across all games and users.

numLose: (INTEGER, Default: 0)
The total number of losses recorded across all games and users.

winLoseRatio: (FLOAT, Default: 0.0)
The overall ratio of wins to losses (calculated as numWin / numLose, rounded to two decimals).

numPeoplePerChoice: (INTEGER, Default: 0)
The total number of people who have made each available choice

totalStepsTaken: (INTEGER, Default: 0)
The cumulative total of steps taken by all users in all games.

List of tests that are used to test the table:
TABLE TEST 1:
Update GlobalStatistics after a win

Description:
Ensure the GlobalStatistics table increments the win count and recalculates the win/lose ratio correctly after a user wins a game.

Pre-conditions (what needs to be true about the system before the test can be applied):

The database is running and GlobalStatistics table is initialized.

The initial values for numWin and numLose are known (e.g., numWin = 5, numLose = 2).

Test steps:

Note the current values of numWin, numLose, and winLoseRatio in the GlobalStatistics table.

Simulate or execute a user winning a game.

Query the GlobalStatistics table after the win.

Check that numWin has increased by one.

Check that winLoseRatio reflects the new values (numWin / numLose).

Expected result:

numWin increases by one.

winLoseRatio updates according to the new win and loss counts.

No other fields are unintentionally changed.

Actual result (when you are testing this, how can you tell it worked):

numWin is one more than before; winLoseRatio is correct.

All values are consistent with expectations.

Status (Pass/Fail, when this test was performed):
Pass

Notes:

Also check that no database errors occur and that stepsTaken and numLose are unchanged by a win event.

You may repeat for loss events or other stat changes for completeness.

Post-conditions:

GlobalStatistics table reflects the correct, updated number of wins and win/lose ratio. The table’s data integrity is preserved after the change.

TABLE TEST 2:

Use case name:
Accurately aggregate steps and choices in GlobalStatistics after a game

Description:
Verify that, after each game is finished, the GlobalStatistics table correctly increments the total steps taken by the number of choices made in that game, and that the count for each choice made is accurately reflected.

Pre-conditions (what needs to be true about the system before the test can be applied):

The database is running and the GlobalStatistics table is initialized.

The starting value of stepsTaken and numPeoplePerChoice are known.

The set of possible choices for the game is defined.

The game is instrumented to record each choice made during a run.

Test steps:

Note and record the initial value of stepsTaken and numPeoplePerChoice in GlobalStatistics.

Play and finish a game, making N distinct choices (e.g., 5 steps/choices in the run).

After finishing, query GlobalStatistics.

Check that stepsTaken has increased by exactly N (the number of choices made in the game).

For each possible choice, verify that numPeoplePerChoice is incremented correctly based on the choices made in this run.

Repeat with a new game of a different number of steps and a different pattern of choices, and verify again.

Expected result:

stepsTaken increases by the exact number of choices made in the completed run.

For each choice made in the game, numPeoplePerChoice is incremented by one (or by however many times that choice was made).

No other unrelated fields are changed.

Actual result (when you are testing this, how can you tell it worked):

The difference in stepsTaken matches the number of choices in the last completed game.

Each increment to numPeoplePerChoice matches the actual choices made.

If N=5 choices were made, stepsTaken increases by 5.

Status (Pass/Fail, when this test was performed):
Pass

Notes:

Test with multiple games, various patterns and numbers of choices for robustness.

If there is a mapping from choices to a subtable or another structure, verify that as well.

Investigate any mismatches immediately as a bug in logging, data entry, or aggregation logic.

Post-conditions (what must be true about the system when the test has completed successfully):

stepsTaken reflects the total number of steps taken in all completed games.

numPeoplePerChoice accurately records the total selections for each choice across all runs.

Data integrity is preserved for all fields.

**Data Access Method**

Name: showGlobalStats()

Description:This method lists all the aggregated statistics for the individual user, as well as the comparison to the overall statistics for the whole game, across everyone who has played.

Parameters:
none

Return Values:
numWin (int)

numLose (int)

winLoseRatio (float)

numPeoplePerChoice (int)

stepsTaken (int)

List of tests to verify access methods:
ACCESS METHOD TEST 1:
Use case name:
Display global statistics after a win

Description:
After a user wins a game, the system should automatically display the latest global statistics on the post-game screen.

Pre-conditions (what needs to be true about the system before the test can be applied):

At least one user has completed and won a game.

The GlobalStatistics table contains up-to-date stats.

Test steps: 

Complete a game run and achieve a win.

Observe the post-game screen after the win.

Verify that the global statistics section is present and visible. 

Compare the displayed global stats (win count, loss count, win/lose ratio, steps taken, etc.) with the values in the database.

(Optional) Repeat with another win and confirm stats update appropriately.

Expected result:

After the user wins a game, the post-game screen automatically displays the current global statistics.

Actual result (when you are testing this, how can you tell it worked):

The post-game screen appears, and the statistics shown match those stored in the GlobalStatistics table.

Status (Pass/Fail, when this test was performed):
Pass

Notes:

If the stats are not displayed, or show outdated/incorrect values, mark as Fail.

Test can be repeated for edge cases (e.g., after first ever win, after first ever loss, etc.).

Post-conditions:
The user sees the most up-to-date global stats after a win.
The database remains accurate and in sync with the display.
3425

## Personal Data

**About Table**

Table Name: 
personal_data

Table Description: 
This table will include each individual user's statistics. 

Fields: (include name and description of each)

| Field Name | Description                               |
|------------|-------------------------------------------|
| `user_id`  | Primary Key. User ID.      |
| `user_num_win`| Aggregate data for wins |
| `user_num_lose`  | Aggregate data for lose |
| `user_ratio`| Ratio between user's win vs lose (percentage) |
| `user_paths`| Number of choices user took |

**Data Access Method**

Name: 
`display_user_stats`

Description:
- Displays user statistics when they click on the user stat button

Parameters:
- Each player should have a unique user_id which will associate them to their user data. 

Return Values: 
- Returns values in every field of the table.

List of tests to verify access methods:

Use case name:
- Fetch and display user data when user clicks on button

Description:
- Display user's game statistics

Pre-conditions:
- User must have played the game at least once
- User must have typed in their pin

Test steps:
1. Play the game
2. Click on "stats" button
3. View stats on win or lose page

Expected Results:
- See all stats for only the user (not global)

Status: 
- Pass/Fail

Post conditions:
- There aren't really post conditions here. User aggregate data should be stored in database as user is playing the game and when they win or lose.