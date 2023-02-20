from behave import *
from airtest.core.api import *

# Initialize Airtest
connect("Windows")

# Define the step definitions
@given("a web browser is open")
def step_impl(context):
    start_app("chrome.exe")

@when('I navigate to "{url}"')
def step_impl(context, url):
    touch(Template(r"templates/chrome_address_bar.png", record_pos=(0.148, -0.417), resolution=(1920, 1080)))
    text(url + "\n")

@when('I enter "{query}" in the search bar')
def step_impl(context, query):
    touch(Template(r"templates/chrome_search_bar.png", record_pos=(0.26, -0.366), resolution=(1920, 1080)))
    text(query + "\n")

@then('I should see search results for "{query}"')
def step_impl(context, query):
    assert exists(Template(r"templates/chrome_search_results.png", record_pos=(0.025, -0.138), resolution=(1920, 1080)))
