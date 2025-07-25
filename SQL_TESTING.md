# CSPB3308_Term-Project_Team1

# SQL_TESTING
In this milestone, we are designing our database, including the descriptions of our tables, fields within the tables, and our data access methods for each. In addition to this, we will include tests for the access methods. 

## User

**About Table**

Table Name:

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods:

## Choices

**About Table**

Table Name:

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods:

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

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods: