from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .utils import read_and_save_csv_to_db
from .models import School, AssessmentArea, Award, Class, Student, Subject, Answer
import plotly.graph_objs as go

def import_csv(request):
    if request.method == 'POST':
        # Check if the CSV file is uploaded
        if 'csv_file' not in request.FILES:
            return JsonResponse({'success': False, 'message': 'No CSV file uploaded.'}, status=400)
        
        # Get the uploaded CSV file from the request
        csv_file = request.FILES['csv_file']
        
        # Call the function to read and save specific CSV data to the database
        try:
            read_and_save_csv_to_db(csv_file)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error importing CSV: {str(e)}'}, status=500)
        
        # Add a success message
        messages.success(request, 'CSV data imported successfully.')
        
        # Return success response
        return JsonResponse({'success': True, 'message': 'CSV data imported successfully.'})
    else:
        # If the request method is not POST, render a template with an upload form
        return render(request, 'import_csv.html')

def visualize_data(request):
    # Retrieve data from models
    schools = School.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    awards = Award.objects.all()
    classes = Class.objects.all()
    students = Student.objects.all()
    subjects = Subject.objects.all()
    answers = Answer.objects.all()

    # Check if there is any data available
    if not any([schools, assessment_areas, awards, classes, students, subjects, answers]):
        return render(request, 'no_data.html')

    # Create traces for visualization
    school_trace = go.Bar(x=[school.name for school in schools], y=[school.id for school in schools], name='Schools')

    assessment_area_trace = go.Pie(labels=[area.name for area in assessment_areas], values=[area.id for area in assessment_areas], name='Assessment Areas')

    award_trace = go.Scatter(x=[award.name for award in awards], y=[award.id for award in awards], mode='markers', name='Awards')

    class_trace = go.Line(x=[cls.name for cls in classes], y=[cls.id for cls in classes], name='Classes')

    student_trace = go.Bar(x=[student.fullname for student in students], y=[student.id for student in students], name='Students')

    subject_trace = go.Histogram(x=[subject.subject_score for subject in subjects], name='Subjects')

    answer_trace = go.Box(y=[answer.id for answer in answers], name='Answers')

    # Create layout
    layout = go.Layout(title='Data Visualization')

    # Create subplots
    fig_school = go.Figure(data=[school_trace], layout=layout)
    fig_assessment_area = go.Figure(data=[assessment_area_trace], layout=layout)
    fig_award = go.Figure(data=[award_trace], layout=layout)
    fig_class = go.Figure(data=[class_trace], layout=layout)
    fig_student = go.Figure(data=[student_trace], layout=layout)
    fig_subject = go.Figure(data=[subject_trace], layout=layout)
    fig_answer = go.Figure(data=[answer_trace], layout=layout)

    # Convert figures to HTML strings
    plot_div_school = fig_school.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_assessment_area = fig_assessment_area.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_award = fig_award.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_class = fig_class.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_student = fig_student.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_subject = fig_subject.to_html(full_html=False, default_height=300, default_width=500)
    plot_div_answer = fig_answer.to_html(full_html=False, default_height=300, default_width=500)

    # Pass the HTML strings to the template
    context = {
        'plot_div_school': plot_div_school,
        'plot_div_assessment_area': plot_div_assessment_area,
        'plot_div_award': plot_div_award,
        'plot_div_class': plot_div_class,
        'plot_div_student': plot_div_student,
        'plot_div_subject': plot_div_subject,
        'plot_div_answer': plot_div_answer,
    }
    return render(request, 'visual_data.html', context)
