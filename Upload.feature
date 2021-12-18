Feature: UploadFile

Scenario: Upload Picture
    Given  <picture> needed to be uploaded to <directory>
    When  I send POST request to DropBox <endpoint>
    Then  I see response "200 OK"
    Examples:
    |picture              |directory             |endpoint                                          |
    |/Desktop/Problem.png | /WebAPIi/Problem.png | https://content.dropboxapi.com/2/files/upload    |