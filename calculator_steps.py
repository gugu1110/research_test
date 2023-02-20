from behave import *
from airtest.core.api import *

# Set the path to the Windows Calculator executable on your system
CALCULATOR_PATH = r"C:\Windows\System32\calc.exe"

# Initialize Airtest
connect("Windows")

# Define the step definitions
@given("the Windows Calculator is open")
def step_impl(context):
    start_app("calc.exe")

@when('I press the "{button}" button')
def step_impl(context, button):
    touch(Template(r"templates/calc_button.png", record_pos=(0.12, -0.039), resolution=(1920, 1080)))
    touch(Template(r"templates/calc_{}.png".format(button), record_pos=(0.109, -0.037), resolution=(1920, 1080)))

@when('I press the "=" button')
def step_impl(context):
    touch(Template(r"templates/calc_button.png", record_pos=(0.12, -0.039), resolution=(1920, 1080)))
    touch(Template(r"templates/calc_equals.png", record_pos=(0.109, -0.037), resolution=(1920, 1080)))

@then('the result should be "{result}"')
def step_impl(context, result):
    assert exists(Template(r"templates/calc_{}.png".format(result), record_pos=(0.07, -0.039), resolution=(1920, 1080)))
