import json

from data_parser import Parser
from data import Data
from search import Search

# This class contains methods for interfacing with the other classes
class CLI:

    def __init__(self):
        self.parser = Parser()
        self.data = Data()
        self.search = None
        self.last_search = []

        self.settings = {
            "result_detail_level": "basic",
            "num_results": 20,
            "num_results_file": 50
        }

    def search_by_keyword(self, keyword):
        results = self.search.search_by_keyword(keyword)
        prev_state = self.settings["result_detail_level"]
        self.settings["result_detail_level"] = "full"
        self.print_course_results(results)
        self.settings["result_detail_level"] = prev_state

    def search_by_field(self, field, value):
        results = self.search.search_by_field(field, value)
        self.print_course_results(results)

    def parse(self):
        courses = self.parser.parse('c12.txt')
        self.data.set_courses(courses)
        self.search = Search(self.data)

    def add_bookmark(self, course_code):
        self.data.add_bookmark(course_code)

    def remove_bookmark(self, course_code):
        self.data.remove_bookmark(course_code)

    def run_bookmark_menu(self):
        """Sub-menu function for viewing and managing bookmarked courses."""

        print("Entered: Sub-Menu: Bookmarked Course Manager.")
        user_choice = -1

        while (user_choice != "4"):
            print("\nPlease select one of the following options...")
            print("1: Add a new course to be bookmarked.")
            print("2: Remove a course from bookmarked courses.")
            print("3: View all bookmarked courses.")
            print("4: Return to main menu.")
            user_choice = input("> ")
            print("")

            #OPTION ONE: Add course to be bookmarked
            if user_choice == "1":
                check = 0
                while (check == 0):

                    course_code = str(input("Please enter the course code of the course to add.\n> "))
                    print("")
                    if self.search.search_by_field('courseCode', course_code.upper()):
                        self.add_bookmark(course_code)
                        check = 1
                    elif course_code == "quit":
                        check = 1
                    else:
                        print("The course code you have selected is invalid. Please try again or enter quit to go back.\n")

            #OPTION TWO: Remove course from bookmarked courses
            elif user_choice == "2":
                check = 0
                while (check == 0):
                    course_code = str(input("Please enter the course code of the course to remove.\n> "))
                    print("")
                    if self.search.search_by_field('courseCode', course_code.upper()):
                        self.remove_bookmark(course_code)
                        check = 1
                    elif course_code == "quit":
                        check = 1
                    else:
                        print("The course code you have selected is invalid. Please try again or enter quit to go back.\n")

            #OPTION THREE: Display all bookmarked courses
            elif user_choice == "3":
                self.print_bookmarks()

            #OPTION FOUR: Return to main menu
            elif user_choice == "4":
                print("Returning to the main menu.")
                return

            #INVALID OPTION
            else:
                print("The option you have selected is invalid. Please try again.")

    def run_field_search_menu(self):
        """Sub-menu function for searching by a specific field."""

        SEMESTER_OPTIONS = {"1": "F", "2": "W", "3": "S", "4": "U"}
        WEIGHT_OPTIONS = {"1": "0.25", "2": "0.5", "3": "0.75", "4": "1.00"}

        print("Entered: Sub-Menu: Field Search.")
        user_choice = -1

        while user_choice != "6":
            print("\nPlease select one of the following options...")
            print("1: Search by course name.")
            print("2: Search by course code")
            print("3: Search by semester(s) offered.")
            print("4: Search by credit weight.")
            print("5: Search by department.")
            print("6: Return to main menu.")
            
            user_choice = str(input("> "))
            print("")

            #OPTION ONE: Search by course name
            if user_choice == "1":
                course_name = str(input("Please enter the name or part of the name of the course to search for.\n> "))
                print("")

                #Make sure the user actually provided a name to search with
                if len(course_name) > 3:
                    self.search_by_field('courseName', course_name)

                else:
                    print("The course name provided is too short. Please try again.")
                

            #OPTION TWO: Search by course code
            elif user_choice == "2":
                course_code = str(input("Please enter the course code to search for.\n"))

                if len(course_code) > 2:
                    self.search_by_field('courseCode', course_code)
                
                else:
                    print("The course code provided is too short. Please try again.")

            #OPTION THREE: Search by semester offered
            elif user_choice == "3":
                print("Please select a semester from one of the options below:")
                print("1: F (Fall semester offering)")
                print("2: W (Winter semester offering)")
                print("3: S (Summer semester offering)")
                print("4: U (Unassigned semester offering)")
                semester = str(input("> "))
                print("")

                #Verify that the user's selection is a valid option
                if semester in SEMESTER_OPTIONS:
                    self.search_by_field('semesterOffered', SEMESTER_OPTIONS[semester])

                else:
                    print("The option you have selected is invalid. Please try again.")

            #OPTION FOUR: Search by credit weight
            elif user_choice == "4":
                print ("Please select a credit weight from one of the options below:")
                print("1: 0.25")
                print("2: 0.50")
                print("3: 0.75")
                print("4: 1.00")
                print("5: Other")
                credit_weight = str(input("> "))
                print("")

                #Verify that the user's selection is a valid option
                if credit_weight in WEIGHT_OPTIONS:
                    self.search_by_field('weight', WEIGHT_OPTIONS[credit_weight])

                #Prompt the user if they selected an 'other' option
                elif credit_weight == "5":

                    credit_weight = str(input("Please enter the weight to search with\n> "))
                    self.search_by_field('weight', credit_weight)

                else:
                    print("The option you have selected is invalid. Please try again.")
                
            #OPTION FIVE: Search by course department
            elif user_choice == "5":
                course_department = input ("Please enter the name of the department to retrieve courses for.\n> ")
                print("")

                #Make sure the user actually provided a department to search with
                if len(course_department) > 3:
                    self.search_by_field('department', course_department)

                else:
                    print("The department name provided is too short. Please try again.")

            #OPTION SIX: Return to main menu
            elif user_choice == "6":
                print("Returning to the main menu.")
                return

            #INVALID OPTION
            else: 
                print("The option you have selected is invalid. Please try again.")

    def run_keyword_search_menu(self):
        """Sub-menu for searching by a specific keyword."""

        print("Entered: Sub-Menu: Keyword Search.")
        user_choice = -1

        while user_choice != "2":
            print("Please enter a keyword to search with.")
            print("Note: Keyword must be greater than three characters in length.")
            print("q: Return to main menu.\n")

            user_choice = str(input("> "))
            print("")

            #OPTION ONE: Search
            if user_choice != "q":
                #Validate that the keyword to search is of the proper minimum length
                if len(user_choice) > 3:
                    self.search_by_keyword(user_choice)
                
                else:
                    print("The keyword provided \'{}\' is too short. Please try again.\n".format(user_choice))

            #OPTION TWO: Exit sub-menu
            else:
                print("Returning to the main menu.")
                return
            
    def run_main_menu(self):
        """Function to run the main menu for navigating to sub-menus."""

        print("Welcome to the Guelph Course Query Program!")
        user_choice = -1

        while user_choice != "5":
            print("\nPlease select one of the following options...")
            print("1: Search for courses by a specific field.")
            print("2: Search for courses by keyword.")
            print("3: View or edit bookmarked courses.")
            print("4: Adjust query program settings.")
            print("5: Exit Program.")
            user_choice = str(input("> "))
            print("")

            #OPTION ONE: Navigate to field search sub-menu
            if user_choice == "1":
                self.run_field_search_menu()
            
            #OPTION TWO: Navigate to keyword search sub-menu
            elif user_choice == "2":
                self.run_keyword_search_menu()

            #OPTION THREE: Navigate to bookmark search sub-menu
            elif user_choice == "3":
                self.run_bookmark_menu()

            #OPTION FOUR: Navigate to settings sub-menu
            elif user_choice == "4":
                self.run_settings_menu()

            #OPTION FIVE: Save the user's settings to a file and exit the program
            elif user_choice == "5":
                self.save_settings_to_file()
                print("Thank you for using the Guelph Course Search Program. Goodbye!\n")
                return
            
            #INVALID OPTION
            else:
                print("The option you have selected is invalid. Please try again.")

    def run_settings_menu(self):
        """Sub-menu for adjusting CLI settings parameters"""

        print("Entered: Sub-Menu: Settings Configuration.")
        user_choice = -1

        while user_choice != "5":
            print("\nPlease select an option below: ")
            print("1: Adjust details level of course search results.")
            print("2: Adjust number of course search results for terminal output.")
            print("3: Adjust number of course search results for file writing.")
            print("4: View current setting configurations.")
            print("5: Return to main menu.")

            user_choice = str(input("> "))
            print("")

            #OPTION ONE: ADJUST DETAILS LEVEL
            if user_choice == "1":
                print("Please select a detail level option:")
                print("1: Basic - Returns course code and course name only.")
                print("2: Detailed - Returns course code, name, and description.")
                print("3: Full - Returns all course information.")

                detail_selection = str(input("> "))
                print("")

                #Validate the user selection before updating the settings
                if detail_selection == "1" or detail_selection == "2" or detail_selection == "3":

                    if detail_selection == "1":
                        self.settings["result_detail_level"] = "basic"

                    elif detail_selection == "2":
                        self.settings["result_detail_level"] = "detailed"

                    elif detail_selection == "3": 
                        self.settings["result_detail_level"] = "full"

                    print("The \'detail level\' setting has been updated successfully.")

                else:
                    print("The option you have selected is invalid. Please try again.")

            #OPTION TWO: ADJUST NUM TERMINAL OUTPUT RESULTS
            elif user_choice == "2":
                print("Please select the maximum number of course results to display in the terminal.")
                print("1: 10 results.")
                print("2: 20 results.")
                print("3: 50 results.")

                results_selection = str(input("> "))
                print("")

                #Validate the user selection before updating the setting
                if results_selection == "1" or results_selection == "2" or results_selection == "3":

                    if results_selection == "1":
                        self.settings["num_results"] = 10

                    elif results_selection == "2":
                        self.settings["num_results"] = 20

                    elif results_selection == "3":
                        self.settings["num_results"] = 50

                    print("The \'maximum number of results for terminal output\' setting has been updated successfully.")

                else:
                    print("The option you have selected is invalid. Please try again.")

            #OPTION THREE: ADJUST NUM FILE OUTPUT RESULTS
            elif user_choice == "3":
                print("Please select the maximum number of course results to write to a file.")
                print("1: 20 results.")
                print("2: 50 results.")
                print("3: 100 results.")
                print("4: All results.")
            
                results_selection = str(input("> "))
                print("")

                #Validate the user selection before updating the setting
                if results_selection == "1" or results_selection == "2" or results_selection == "3" or results_selection == "4":

                    if results_selection == "1":
                        self.settings["num_results_file"] = 20

                    elif results_selection == "2":
                        self.settings["num_results_file"] = 50

                    elif results_selection == "3":
                        self.settings["num_results_file"] = 100

                    elif results_selection == "4":
                        self.settings["num_results_file"] = 5000

                else:
                    print("The option you have selected is invalid. Please try again.")

            #OPTION FOUR: PRINT SETTINGS
            elif user_choice == "4":
                self.print_all_settings()

            #OPTION FOUR: RETURN TO MAIN MENU
            elif user_choice == "5":
                print("Returning to the main menu.")
                return

            #INVALID OPTION
            else:
                print("The option you have selected is invalid. Please try again.")
    
    def print_all_settings(self):
        """Function used to output all CLI settings configured by the user for course result searching and output."""

        print("-----Query Program Settings-----")
        for key, value in self.settings.items():
            print("{}: {}".format(key, value))

    def print_course_results(self, search_results):
        """Function used to return course results based on current CLI settings configured."""

        #Set the level of details to display
        detail_level = self.settings["result_detail_level"]

        #Set the number of results to be displayed
        num_results = min(len(search_results), self.settings["num_results"])

        print("\n-----Course Results Returned-----")
        print("Displaying {} of {} returned results.\n".format(num_results, len(search_results)))

        #Print each course's information based on the level of detail to output
        for i in range(0, num_results):
            print("Course Code: {}".format(search_results[i]["courseCode"]))
            print("Name: {}".format(search_results[i]["courseName"]))

            if detail_level == "detailed" or detail_level == "full":
                print("Description: {}".format(search_results[i]["description"]))

                if detail_level == "full":
                    print("Semester(s) Offered: {}".format(search_results[i]["semesterOffered"]))
                    print("Hour Breakdown: {}".format(search_results[i]["hourBreakdown"]))
                    print("Weight: {}".format(search_results[i]["weight"]))
                    print("Format: {}".format(search_results[i]["format"]))
                    print("Pre-requisite(s): {}".format(search_results[i]["prerequisite"]))
                    print("Equate: {}".format(search_results[i]["equate"]))
                    print("Restriction: {}".format(search_results[i]["restriction"]))
                    print("Department: {}".format(search_results[i]["department"]))
                
            print("")

        #If the query returned search results, offer to write them to a file as well
        if len(search_results) > 0:
            write_to_file = str(input("Would you like to write your course results to a file? Y/N\n> "))
            print("")

            #Call the method to write to a file if the user chooses to
            if write_to_file == "Y" or write_to_file == "y":
                self.write_results_to_file(search_results)


    def write_results_to_file(self, search_results):
        """Function used to write the course search results to a file."""

        detail_level = self.settings["result_detail_level"]

        #Set the number of results to be displayed
        num_results = min(len(search_results), self.settings["num_results_file"])

        valid_file = False

        #Prompt for a valid file name until the user provides one
        while valid_file == False:
            file_name = str(input("Please enter the name of the file to write results to. (No extension)\n> "))
            print("")

            if file_name == "":
                print("Please enter a valid file name.\n")

            else:
                valid_file = True

            #Make the file a .txt file
            file_name += ".txt"

        with open(file_name, "w") as fp:

            fp.write("-----Course Results Returned-----\n")
            fp.write("Fetched and wrote {} course results from your query.\n\n".format(num_results))

            #Write each course to the file
            for i in range(0, num_results):

                fp.write("Course Code: {}\n".format(search_results[i]["courseCode"]))        
                fp.write("Name: {}\n".format(search_results[i]["courseName"]))

                if detail_level == "detailed" or detail_level == "full":
                    fp.write("Description: {}\n".format(search_results[i]["description"]))

                    if detail_level == "full":
                        fp.writelines([
                            "Semester(s) Offered: {}\n".format(search_results[i]["semesterOffered"]),
                            "Hour Breakdown: {}\n".format(search_results[i]["hourBreakdown"]),
                            "Weight: {}\n".format(search_results[i]["weight"]),
                            "Format: {}\n".format(search_results[i]["format"]),
                            "Pre-requisite(s): {}\n".format(search_results[i]["prerequisite"]),
                            "Equate: {}\n".format(search_results[i]["equate"]),
                            "Restriction: {}\n".format(search_results[i]["restriction"]),
                            "Department: {}\n".format(search_results[i]["department"]),
                        ])

                fp.write("\n")

        print("The course search results were successfully written to {}.\n".format(file_name))


    def load_settings_from_file(self, test_mode=False):
        """Loads a 'settings.json' file with the user's saved CLI settings, if such a file exists."""
        
        settings_file_name = ""

        if test_mode == False:
            settings_file_name = "settings.json"
        else:
            settings_file_name = "test_settings.json"

        try:

            #Open the JSON file and read the contents into a dictionary
            settings_file = open(settings_file_name, "r")
            settings_dict = json.load(settings_file)

            #Check each key-value pair in the JSON and validate them before updating the CLI settings
            for k, v in settings_dict.items():

                if self.validate_settings_options(k, v) == True:
                    self.settings[k] = v

            settings_file.close()

        #If the file doesn't exist, don't modify the CLI settings
        except FileNotFoundError:
            pass

        #If the file contains bad data, don't modify or stop modifying the CLI settings
        except ValueError:
            pass

    def save_settings_to_file(self, test_mode=False):
        """Saves the current CLI settings configurations to a 'settings.json' file for future loading."""

        settings_file_name = ""

        if test_mode == False:
            settings_file_name = "settings.json"
        else:
            settings_file_name = "test_settings.json"

        #Write the settings dictionary as a JSON object
        with open(settings_file_name, "w") as settings_fp:

            settings_json = json.dumps(self.settings, indent=4)
            settings_fp.write(settings_json)

    def validate_settings_options(self, setting, value):
        """Validates a given setting key-value pair and returns True or False if the pair is valid for the CLI."""

        #Constant sets of options for each setting
        DETAIL_LEVEL_OPTIONS = ["basic", "detailed", "full"]
        NUM_RESULTS_CL = [10, 20, 50]
        NUM_RESULTS_FILE = [20, 50, 100, 5000]
        
        if setting == "result_detail_level":

            if value in DETAIL_LEVEL_OPTIONS:
                return True

            else: 
                return False

        elif setting == "num_results":

            if value in NUM_RESULTS_CL:
                return True
            
            else: 
                return False

        elif setting == "num_results_file":

            if value in NUM_RESULTS_FILE:
                return True

            else:
                return False

        else:
            return False

    def print_bookmarks(self):
        """Function used to return course results based on current CLI settings configured."""

        # Set the level of details to display
        detail_level = self.settings["result_detail_level"]

        print("\n-----Courses Bookmarked-----")
        print("You have {} bookmarks.\n".format(len(self.data.bookmarks)))

        # Print each course's information based on the level of detail to output
        for bookmarkCode in self.data.bookmarks:

            #Make sure the course for the course code was found in the data set
            if len(self.search.search_by_field("courseCode", bookmarkCode)) > 0:
                bookmark = self.search.search_by_field("courseCode", bookmarkCode)[0]
                print("Course Code: {}".format(bookmark["courseCode"]))
                print("Name: {}".format(bookmark["courseName"]))

                if detail_level == "detailed" or detail_level == "full":
                    print("Description: {}".format(bookmark["description"]))

                    if detail_level == "full":
                        print("Semester(s) Offered: {}".format(bookmark["semesterOffered"]))
                        print("Hour Breakdown: {}".format(bookmark["hourBreakdown"]))
                        print("Weight: {}".format(bookmark["weight"]))
                        print("Format: {}".format(bookmark["format"]))
                        print("Pre-requisite(s): {}".format(bookmark["prerequisite"]))
                        print("Equate: {}".format(bookmark["equate"]))
                        print("Restriction: {}".format(bookmark["restriction"]))
                        print("Department: {}".format(bookmark["department"]))

                print("")

            else:
                print("Skipping invalid course code.\n")

# UNCOMMENT IF YOU WANT TO RUN CLI MAIN MENU
if __name__ == '__main__':
    test_cli = CLI()
    test_cli.parse()
    test_cli.load_settings_from_file()
    test_cli.run_main_menu()
