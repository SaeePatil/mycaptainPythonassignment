# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:14:47 2023

@author: hp
"""

def accept_student_data():
 students = []
 while True:
  name = input("Enter student name (or 'q' to quit): ")
 if name.lower() == 'q':
 
  roll_number = input("Enter roll number: ")
 marks = input("Enter marks: ")
 student = {'name': name, 'roll_number': roll_number, 'marks': marks}
 students.append(student)
 return students
def preprocess_student_data(students):
 preprocessed_students = []
 for student in students:
  preprocessed_student = {
 'name': student['name'].strip(),
 'roll_number': student['roll_number'].strip(),
 'marks': int(student['marks'])
 }
 preprocessed_students.append(preprocessed_student)
 return preprocessed_students
def write_student_data_to_file(students, filename):
 with open(filename, 'w') as file:
  for student in students:
   file.write(f"Name: {student['name']}\n")
  file.write(f"Roll Number: {student['roll_number']}\n")
  file.write(f"Marks: {student['marks']}\n")
  file.write('\n')
if __name__ == '__main__':
 student_data = accept_student_data()
 preprocessed_data = preprocess_student_data(student_data)
 filename = input("Enter filename to write the data: ")
 write_student_data_to_file(preprocessed_data, filename)
 print("Data written to the file successfully.")