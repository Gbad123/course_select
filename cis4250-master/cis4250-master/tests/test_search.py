import unittest
import sys

sys.path.append("..")

from cis4250.search import Search
from cis4250.data import Data

class TestSearch(unittest.TestCase):
    data = Data()
    courseInfo = [
        {
            'courseCode': 'ACCT*1220',
            'courseName': 'Introductory Financial Accounting',
            'semesterOffered': 'F,W',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "This introductory course is designed to develop a foundational understanding of current accounting principles and their implication for published financial reports of business enterprises. It builds the base of knowledge and understanding required to succeed in more advanced study of accounting. The course approaches the subject from the point of view of the user of accounting information rather than that of a person who supplies the information.", 
            'format': 'Also offered through Distance Education format.', 
            'prerequisite': '', 
            'equate': '', 
            'restriction': 'ACCT*2220 , This is a Priority Access Course. Enrolment may be restricted to particular programs or specializations. See department for more information.', 
            'department': 'Department of Management'
        },
        {
            'courseCode': 'ACCT*1240',
            'courseName': 'Applied Financial Accounting',
            'semesterOffered': 'W',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "This course requires students to apply the fundamental principles emanating from accounting’s conceptual framework and undertake the practice of financial accounting. Students will become adept at performing the functions related to each step in the accounting cycle, up to and including the preparation of the financial statements and client reports. Students will also develop the skills necessary for assessing an organization’s system of internal controls and financial conditions.", 
            'format': '', 
            'prerequisite': 'ACCT*1220 or ACCT*2220', 
            'equate': '', 
            'restriction': 'ACCT*2240 , This is a Priority Access Course. Enrolment may be restricted to particular programs or specializations. See department for more information.', 
            'department': 'Department of Management'
        },
        {
            'courseCode': 'ACCT*2230',
            'courseName': 'Management Accounting',
            'semesterOffered': 'F,W',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "This course emphasizes the use of accounting information to facilitate effective management decisions. Topics include cost determination, cost control and analysis, budgeting, profit-volume analysis and capital investment analysis.", 
            'format': '', 
            'prerequisite': 'ACCT*1220 or ACCT*2220', 
            'equate': 'AGEC*2230 , BUS*2230', 
            'restriction': 'This is a Priority Access Course. Enrolment may be restricted to particular programs or specializations. See department for more information.', 
            'department': 'Department of Management'
        },
        {
            'courseCode': 'ACCT*3230',
            'courseName': 'Intermediate Management Accounting',
            'semesterOffered': 'S,W',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "This course continues the managerial decision making focus of ACCT*2230. Topics include process costing, transfer pricing, the decision making process, variances and performance measurement.", 
            'format': 'Also offered through Distance Education format.', 
            'prerequisite': 'ACCT*2230', 
            'equate': 'BUS*3230', 
            'restriction': 'Enrolment may be restricted to particular degrees or programs. See department for more information.', 
            'department': 'Department of Management'
        },
        {
            'courseCode': 'ACCT*3280',
            'courseName': 'Auditing I',
            'semesterOffered': 'S,F',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "Auditing I is an examination of the principles and theory underlying the practice of auditing. Concepts of materiality and audit risk are examined and discussed. Sources and techniques for gathering auditing evidence will also be examined. Modern organizations rely on information systems, technology and internal controls to manage and monitor their operations and the impact of these systems on the quality of information produced and on the scope of audits are important elements of this course.", 
            'format': '', 
            'prerequisite': 'ACCT*3330', 
            'equate': '', 
            'restriction': '', 
            'department': 'Department of Management'
        }
    ]
    data.set_courses(courseInfo)
    def test_search_by_field(self):
        mock_courses = [
            {
                'courseCode': 'CIS1500',
                'semesterOffered': 'W'
            },
            {
                'courseCode': 'CIS2500',
                'semesterOffered': 'F'
            },
            {
                'courseCode': 'CIS2520',
                'semesterOffered': 'F,W'
            }
        ]
        data = Data()
        data.set_courses(mock_courses)
        search = Search(data)

        results = search.search_by_field('semesterOffered', 'F')

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], {
            'courseCode': 'CIS2500',
            'semesterOffered': 'F'
        })
        self.assertEqual(results[1], {
            'courseCode': 'CIS2520',
            'semesterOffered': 'F,W'
        })


    def test_courseName(self):
        s = Search(self.data)
        self.assertEqual(1,len(s.search_by_keyword('Introductory Financial Accounting')))
        self.assertEqual(0,len(s.search_by_keyword('')))
 
    def test_semesterOffered(self):
        s = Search(self.data)
        self.assertEqual(1,len(s.search_by_keyword('S,F')))
    
    def test_hourBreakdown(self):
        s = Search(self.data)
        self.assertEqual(5,len(s.search_by_keyword('3-0')))

    def test_weight(self):
        s = Search(self.data)
        self.assertEqual(5,len(s.search_by_keyword('0.5')))
    
    def test_description(self):
        s = Search(self.data)
        self.assertEqual(1,len(s.search_by_keyword('fundamental')))

    def test_format(self):
        s = Search(self.data)
        self.assertEqual(2,len(s.search_by_keyword('Also offered through Distance Education format')))

    def test_prerequisite(self):
        s = Search(self.data)
        self.assertEqual(2,len(s.search_by_keyword('ACCT*1220 or ACCT*2220')))
    
    def test_equate(self):
        s = Search(self.data)
        self.assertEqual(2,len(s.search_by_keyword('ACCT*1220 or ACCT*2220')))

    def test_restriction(self):
        s = Search(self.data)
        self.assertEqual(4,len(s.search_by_keyword('Enrolment may be restricted')))

    def test_department(self):
        s = Search(self.data)
        self.assertEqual(5,len(s.search_by_keyword('Department of Management')))
    
    
if __name__ == '__main__':
    unittest.main()