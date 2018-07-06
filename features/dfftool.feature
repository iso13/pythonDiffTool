Feature: difftool
  As an Engr
  I need to compare json feeds
  So I can determine if there are differences


  Scenario Outline: Compare json files for differences
    Given I compare the following files "<golden>" and "<test>"
    Then I generate an html report comparison

    Examples:
      | golden                               | test                               |
      | ./jsonData/golden_json/answer1.json  | ./jsonData/test_json/answer1.json  |
      | ./jsonData/golden_json/answer2.json  | ./jsonData/test_json/answer2.json  |
      | ./jsonData/golden_json/answer3.json  | ./jsonData/test_json/answer3.json  |
      | ./jsonData/golden_json/answer4.json  | ./jsonData/test_json/answer4.json  |
      | ./jsonData/golden_json/answer5.json  | ./jsonData/test_json/answer5.json  |
      | ./jsonData/golden_json/answer6.json  | ./jsonData/test_json/answer6.json  |
      | ./jsonData/golden_json/answer7.json  | ./jsonData/test_json/answer7.json  |
      | ./jsonData/golden_json/answer8.json  | ./jsonData/test_json/answer8.json  |
      | ./jsonData/golden_json/answer9.json  | ./jsonData/test_json/answer9.json  |
      | ./jsonData/golden_json/answer10.json | ./jsonData/test_json/answer10.json |





