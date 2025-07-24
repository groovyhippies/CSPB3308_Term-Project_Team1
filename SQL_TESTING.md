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

Table Description:

Fields: (include name and description of each)

**Data Access Method**

Name:

Description:

Parameters:

Return Values:

List of tests to verify access methods: