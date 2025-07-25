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

Table Name:

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods:

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