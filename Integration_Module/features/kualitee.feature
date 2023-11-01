Feature: Kualitee Setting Module
  Background: Pre-Steps
    Given I launch Chrome browser
    When I open Kualitee homepage
    And Enter username and password
    And click on login button
    And click on setting button

  Scenario: Login to kualitee Dashboard and Move to settings and role page is opened
    Then Manage Roles page will be open and checked

  Scenario: check create new role page is opened or not
    Then Manage Roles page will be open and checked
    And click create role button
    Then Create new role page will be open and checked

  Scenario: Proper Messaging for Required Fields if left Blank
    Then Manage Roles page will be open and checked
    And click create role button
    And click save button
    Then Check required fields message is prompted or not

  Scenario: Check the checkbox
    Then Manage Roles page will be open and checked
    And click create role button
    And click checkbox


  Scenario: click cancel button and check managed role page is opened
    Then Manage Roles page will be open and checked
    And click create role button
    And click cancel button
    Then Manage Roles page will be open and checked

  Scenario: add a new role and move to edit role page and verify
    Then Manage Roles page will be open and checked
    And click create role button
    And enter roleName "asdfwqsd" and Description "rewqwasder"
    And click save button
    Then verify edit role page is landed

  Scenario: Check the project drop down
    Then Manage Roles page will be open and checked
    And click create role button
    And click domain project dropdown
    Then Create new role page will be open and checked

  Scenario: Check ascending and descending order of columns
    Then Manage Roles page will be open and checked
    Then click table headers and observe change in data

  Scenario: Search test in roles
    Then Manage Roles page will be open and checked
    And Click search and enter "test" and observe change
