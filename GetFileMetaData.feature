Feature: GetFileMetadata

Scenario: GetFileMetadata
    Given uploaded file
    When  I send POST request to DropBox <API>
    Then  I get response "200 OK"
    Examples:
        | directory        | API                                              | 
        | /WebAPIi/Problem | https://api.dropboxapi.com/2/sharing/get_file_metadata | 