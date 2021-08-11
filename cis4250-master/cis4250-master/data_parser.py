import re


class Parser:

    def __init__(self):
        pass

    """
    Function to parse the text file
    inputs:
    raw_data
     - Type: String
     - Description: the file name that we are going to be parsing
    
    outputs:
    list
     - Type: list of dictionaries
     - Description: our parsed text held in a list of dictionaries
     - Dictionary format: {
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
    def parse(self, raw_data):
        # Initializing our variables
        offering = ""
        prereq = ""
        equate = ""
        restrict = ""
        description = ""
        code = ""
        line2 = ""
        # Initializing the list
        list = []
        # Initializing our flags
        header = 0
        off = 0
        pre = 0
        equ = 0
        res = 0
        # Opening our file
        with open(raw_data, 'rt', encoding='utf-8') as myfile:
            # Running through it line by line
            for line in myfile:
                line = line.strip("\n")
                # Making sure that the line isn't empty
                if line:
                    # Matching the first line of a class
                    if re.search(
                            r"[A-Z]{2,4}\*\d{4}.+ (F,W,S|F,S,W|S,W,F|S,F,W|W,F,S|W,S,F|F,W|F,S|W,S|W,F|S,W|S,F|F|W|S|U|P1|P2|P3|P4) \((\d|V|\d\.\d)-(\d|V|\d\d|\d\.\d)\) \[\d\.\d\d\]",
                            line):
                        # Parsing the data in
                        code = re.search(r"[A-Z]{2,4}\*\d{4}", line).group()
                        name = re.search(r"(?<=[A-Z]\*\d{4}).*(?= [FSWU,P1234]{1,5} )", line).group().strip()
                        semester = re.search(r"(?<= )[FSWU,P1234]{1,5}(?= )", line).group()
                        hours = re.search(r"(?<= \()(\d|V|\d\.\d)-(\d|V|\d\d|\d\.\d)(?=\) )", line).group()
                        weight = re.search(r"(?<= \[)\d\.\d\d(?=\])", line).group()
                        # Telling the code to start reading in the description
                        header = 1
                        # Resetting the variables
                        offering = ""
                        prereq = ""
                        equate = ""
                        restrict = ""
                        description = ""
                    # Making sure that the header has been read
                    elif code:
                        # If we find the offering line read in the offering
                        if re.match(r"(Offering\(s\):)", line):
                            offering = re.findall(r"(?<=Offering\(s\): ).*", line)
                            offering = "".join(offering)
                            off = 1
                        # If we find the prerequisite line read in the prerequisite
                        elif re.match(r"(Prerequisite\(s\):)", line):
                            prereq = re.findall(r"(?<=Prerequisite\(s\): ).*", line)
                            prereq = "".join(prereq)
                            pre = 1
                        # If we find the equate line read in the equate
                        elif re.match(r"(Equate\(s\):)", line):
                            equate = re.findall(r"(?<=Equate\(s\): ).*", line)
                            equate = "".join(equate)
                            equ = 1
                        # If we find the restriction line read in the restriction
                        elif re.match(r"(Restriction\(s\):)", line):
                            restrict = re.findall(r"(?<=Restriction\(s\): ).*", line)
                            restrict = "".join(restrict)
                            res = 1
                        # If we find the department line read in the department and save the information
                        elif re.match(r"(Department\(s\):)", line):
                            dpmt = re.findall(r"(?<=Department\(s\): ).*", line)
                            dpmt = "".join(dpmt)
                            # Reset the flags
                            header = 0
                            off = 0
                            pre = 0
                            equ = 0
                            res = 0
                            # Save the information if description exists
                            if description:
                                dataStruct = {}
                                dataStruct["courseCode"] = code
                                dataStruct["courseName"] = name
                                dataStruct["semesterOffered"] = semester
                                dataStruct["hourBreakdown"] = hours
                                dataStruct["weight"] = weight
                                dataStruct["description"] = description
                                dataStruct["format"] = offering
                                dataStruct["prerequisite"] = prereq
                                dataStruct["equate"] = equate
                                dataStruct["restriction"] = restrict
                                dataStruct["department"] = dpmt
                                list.append(dataStruct)
                            # Reset the code variable so that we can make sure that the header is read in
                            code = ""
                        elif res == 1:  # Reading in Restrictions if it is more than one line
                            restrict = restrict + " " + line
                        elif equ == 1:  # Reading in Equates if it is more than one line
                            equate = equate + " " + line
                        elif pre == 1:  # Reading in Prerequisites if it is more than one line
                            prereq = prereq + " " + line
                        elif off == 1:  # Reading in offering if it is more than one line
                            offering = offering + " " + line
                        elif header == 1:  # Reading in the description
                            if not description:
                                description = line
                            else:
                                description = description + " " + line
                    elif re.search(r"[A-Z]{2,4}\*\d{4}", line):
                        line2 = line
                    elif line2:
                        line2 = line2 + " " + line
                        if re.search(
                                r"[A-Z]{2,4}\*\d{4}.+ (F,W,S|F,S,W|S,W,F|S,F,W|W,F,S|W,S,F|F,W|F,S|W,S|W,F|S,W|S,F|F|W|S|U|P1|P2|P3|P4) \((\d|V|\d\.\d)-(\d|V|\d\d|\d\.\d)\) \[\d\.\d\d\]",
                                line2):
                            # Parsing the data in
                            code = re.search(r"[A-Z]{2,4}\*\d{4}", line2).group()
                            name = re.search(r"(?<=[A-Z]\*\d{4}).*(?= [FSWU,P1234]{1,5} )", line2).group().strip()
                            semester = re.search(r"(?<= )[FSWU,P1234]{1,5}(?= )", line2).group()
                            hours = re.search(r"(?<= \()(\d|V|\d\.\d)-(\d|V|\d\d|\d\.\d)(?=\) )", line2).group()
                            weight = re.search(r"(?<= \[)\d\.\d\d(?=\])", line2).group()
                            # Telling the code to start reading in the description
                            header = 1
                            # Resetting the variables
                            offering = ""
                            prereq = ""
                            equate = ""
                            restrict = ""
                            description = ""
                        line2 = ""
        return list  # Return our completed list