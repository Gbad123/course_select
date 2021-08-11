class Search:
    """
    The Search Class needs to be initialized with the list of dictionaries.
    """
    def __init__(self, data):
        self.data = data

    """
    Function to search a list of dictionaries given a keyword 
    inputs:
     - Type: List
     - Description: a list which contains dictionary objects in the format of:{
         'courseCode': 'The course code',
         'courseName': 'The name of the course',
         'semesterOffered': 'What semesters the course is offered in',
         'hourBreakdown': 'How the house are divided between class and lab',
         'weight': 'How the course is weighted',
         'description': 'The description for the course',
         'format': 'The format that the course is offered in',
         'prerequisite': 'Any required courses'
         'equate': 'Any courses that equal this course for prerequisites'
         'restriction': 'Any courses that will prevent you from taking this course',
         'department': 'What department this course is in'
        }
    """

    def search_by_keyword(self, keyword):
        # The list which contains matches
        matches = []
        # check if keywords is greater than 2 characters, so we dont return massive list 
        if(len(keyword) <= 2):
            return matches
        # iterates over each item in the List
        for dictionary in self.data.courses:
            # check the fields in the dictionary to see if it contains the keyword
            if(keyword in dictionary['courseCode']):
                matches.append(dictionary)
            elif(keyword in dictionary['courseName']):
                matches.append(dictionary)
            elif(keyword in dictionary['semesterOffered']):
                matches.append(dictionary)
            elif(keyword in dictionary['hourBreakdown']):
                matches.append(dictionary)
            elif(keyword in dictionary['weight']):
                matches.append(dictionary)
            elif(keyword in dictionary['description']):
                matches.append(dictionary)
            elif(keyword in dictionary['format']):
                matches.append(dictionary)
            elif(keyword in dictionary['prerequisite']):
                matches.append(dictionary)
            elif(keyword in dictionary['equate']):
                matches.append(dictionary)
            elif(keyword in dictionary['restriction']):
                matches.append(dictionary)
            elif(keyword in dictionary['department']):
                matches.append(dictionary)
        return matches

    """
    Function to filter courses based on a field
    
    Inputs:
    field
        - Type: String
        - Description: the field to filter on
    value:
        - Type: String
        - Description: the value of the field to match

    Outputs:
    results
        - Type: []
        - Description: list of courses
    """
    def search_by_field(self, field, value):
        results = []
        for course in self.data.courses:
            if course.get(field, None) and value in course[field]:
                results.append(course)
        return results
