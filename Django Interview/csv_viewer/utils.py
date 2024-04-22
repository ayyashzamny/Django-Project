import csv
from .models import School, AssessmentArea, Award, Class, Student, Subject, Answer

def read_and_save_csv_to_db(csv_file):
    # Decode and extract data from the uploaded CSV file
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    
    for row in reader:
        # Extract the required columns from the row
        school_name = row['school_name']
        assessment_area_name = row['Assessment Areas']
        award_name = row['award']
        class_name = row['Class']
        student_fname = row['First Name']
        student_lname = row['Last Name']
        subject_name = row['Subject']
        subject_score = row['average_score']
        answer_value = row['Answers']

        # Create instances of your models with the extracted data
        school_instance = School.objects.create(name=school_name)
        assessment_area_instance = AssessmentArea.objects.create(name=assessment_area_name)
        award_instance = Award.objects.create(name=award_name)
        class_instance = Class.objects.create(name=class_name)
        student_instance = Student.objects.create(fullname=student_fname + ' ' + student_lname)
        subject_instance = Subject.objects.create(subject=subject_name, subject_score=subject_score)
        answer_instance = Answer.objects.create(answer=answer_value)
