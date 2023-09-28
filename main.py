import create_new_tracker
import add_existing_project
import compile_languages
import compile_projects


def main():
    option = input("Hello, please type the letter corresponding to the action you would like to perform.\n"
                   "A) Create New Project Tracker\n"
                   "B) Add to existing Project Tracker\n"
                   "C) Compile a list of all projects created\n"
                   "D) Compile a list of all programming languages used in the projects\n"
                   "E) Exit Program"
                   "Example: If you would like to select the second option, simply type B\n")

    # Create a dictionary of options to simplify conditional for which option user selects
    choices = {"A": create_new_tracker.create_tracker, "B": add_existing_project.add_project,
               "C": compile_projects.print_projects, "D": compile_languages.print_languages,
               "E": exit}

    if option.upper() in choices:
        choices[option.upper()]()

    while option.upper() not in choices:
        option = input("Please type the letter of one of the provided options.\n")

        if option.upper() in choices:
            choices[option.upper()]()


main()
