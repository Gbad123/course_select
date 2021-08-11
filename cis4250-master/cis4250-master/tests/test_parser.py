import unittest
import sys
sys.path.append("..")

from cis4250.data_parser import Parser
from cis4250.cli import CLI

class TestParser(unittest.TestCase):

    #Test initial setting configurations of CLI
    def test_initial_settings(self):
        test_cli = CLI()

        self.assertEqual(test_cli.settings['result_detail_level'], 'basic')
        self.assertEqual(test_cli.settings['num_results'], 20)

    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_negative(self):
        list = Parser.parse(self, 'tests/c12Neg.txt')
        self.assertEqual(list,[])
    # test if parser populates data structure fields correctly
    def test_positive(self):
        list = Parser.parse(self, 'tests/c12_test.txt')

        self.assertEqual(list[0], {
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
        })
        self.assertEqual(list[1], {
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
        })
        self.assertEqual(list[2], {
            'courseCode': 'ACCT*2230',
            'courseName': 'Management Accounting',
            'semesterOffered': 'U',
            'hourBreakdown': '3-0',
            'weight': '0.50',
            'description': "This course emphasizes the use of accounting information to facilitate effective management decisions. Topics include cost determination, cost control and analysis, budgeting, profit-volume analysis and capital investment analysis.", 
            'format': '', 
            'prerequisite': 'ACCT*1220 or ACCT*2220', 
            'equate': 'AGEC*2230 , BUS*2230', 
            'restriction': 'This is a Priority Access Course. Enrolment may be restricted to particular programs or specializations. See department for more information.', 
            'department': 'Department of Management'
        })
        self.assertEqual(list[3], {
            'courseCode': 'ACCT*3230',
            'courseName': 'Intermediate Management Accounting',
            'semesterOffered': 'S,W',
            'hourBreakdown': '3-1.5',
            'weight': '0.50',
            'description': "This course continues the managerial decision making focus of ACCT*2230. Topics include process costing, transfer pricing, the decision making process, variances and performance measurement.", 
            'format': 'Also offered through Distance Education format.', 
            'prerequisite': 'ACCT*2230', 
            'equate': 'BUS*3230', 
            'restriction': 'Enrolment may be restricted to particular degrees or programs. See department for more information.', 
            'department': 'Department of Management'
        })
        self.assertEqual(list[4], {
            'courseCode': 'ACCT*3280',
            'courseName': 'Auditing I',
            'semesterOffered': 'S,F',
            'hourBreakdown': '3-10',
            'weight': '0.50',
            'description': "Auditing I is an examination of the principles and theory underlying the practice of auditing. Concepts of materiality and audit risk are examined and discussed. Sources and techniques for gathering auditing evidence will also be examined. Modern organizations rely on information systems, technology and internal controls to manage and monitor their operations and the impact of these systems on the quality of information produced and on the scope of audits are important elements of this course.", 
            'format': '', 
            'prerequisite': 'ACCT*3330', 
            'equate': '', 
            'restriction': '', 
            'department': 'Department of Management'
        })

if __name__ == '__main__':
    unittest.main()