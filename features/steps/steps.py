from behave import given, then
import difflib
import os


@given(u'I compare the following files "{gold_file}" and "{test_file}"')
def step_impl(context, gold_file, test_file):
    context.gold_file = gold_file
    context.test_file = test_file
    context.first_file_lines = open(context.gold_file).readlines()
    context.second_file_lines = open(context.test_file).readlines()


@then(u'I generate an html report comparison')
def i_generate_an_html_report_comparison(context):
    i = 1
    while os.path.exists('difference_report%s.html' % i):
        i += 1
    context.difference = difflib.HtmlDiff().make_file(context.first_file_lines, context.second_file_lines,
                                                      context.gold_file,
                                                      context.test_file)
    context.difference_report = open('difference_report%s.html' % i, 'w')
    context.difference_report.write(context.difference)
    context.difference_report.close()


# ToDo:
# parse only by specific key
# fail scenario if there are diffs found
# ignore order and pass scenario
# read in files from vs outline
# generate json report for scenarios
