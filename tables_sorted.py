import json


def get_json(file_path_and_name):
    with open(file_path_and_name, 'r') as fp:
        return json.load(fp)


gold_answer1 = './jsonData/golden_json/answer1.json'
gold_answer2 = './jsonData/golden_json/answer2.json'
gold_answer3 = './jsonData/golden_json/answer3.json'
gold_answer4 = './jsonData/golden_json/answer4.json'
gold_answer5 = './jsonData/golden_json/answer5.json'
gold_answer6 = './jsonData/golden_json/answer6.json'
gold_answer7 = './jsonData/golden_json/answer7.json'
gold_answer8 = './jsonData/golden_json/answer8.json'
gold_answer9 = './jsonData/golden_json/answer9.json'

test_answer1 = './jsonData/test_json/answer1.json'
test_answer2 = './jsonData/test_json/answer2.json'
test_answer3 = './jsonData/test_json/answer3.json'
test_answer4 = './jsonData/test_json/answer4.json'
test_answer5 = './jsonData/test_json/answer5.json'
test_answer6 = './jsonData/test_json/answer6.json'
test_answer7 = './jsonData/test_json/answer7.json'
test_answer8 = './jsonData/test_json/answer8.json'
test_answer9 = './jsonData/test_json/answer9.json'

# gold_answer = ['./jsonData/golden_json/answer1.json', './jsonData/golden_json/answer2.json',
#                './jsonData/golden_json/answer3.json', './jsonData/golden_json/answer4.json',
#                './jsonData/golden_json/answer5.json', './jsonData/golden_json/answer6.json',
#                './jsonData/golden_json/answer7.json', './jsonData/golden_json/answer8.json',
#                './jsonData/golden_json/answer9.json']
# test_answer = ['./jsonData/test_json/answer1.json', './jsonData/test_json/answer2.json',
#                './jsonData/test_json/answer3.json', './jsonData/test_json/answer4.json',
#                './jsonData/test_json/answer5.json', './jsonData/test_json/answer6.json',
#                './jsonData/test_json/answer7.json', './jsonData/test_json/answer8.json',
#                './jsonData/test_json/answer9.json']
# for i in gold_answer:
#     gold = get_json(gold_answer)
#
# for j in test_answer:
#     test = get_json(test_answer)

test = get_json(test_answer2)
gold = get_json(gold_answer2)

test_tables = test.get("tables", "")
gold_tables = gold.get("tables", "")
message = "JSON files with different tables %s %s"

if sorted(gold_tables) != sorted(test_tables):
    print(message % (test_answer2, gold_answer2))
