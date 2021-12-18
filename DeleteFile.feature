Feature: Delete File or directory


Scenario Outline: Delete File or directory
    Given <File_Directory>
    When I send POST requset to <endpoint>
    Then I get response "200 OK"
    Examples:
        | File_Directory       | endpoint                                      |
        | /WebAPIi/Problem.png | https://api.dropboxapi.com/2/files/delete_v2  | 