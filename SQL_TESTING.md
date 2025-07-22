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

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods: