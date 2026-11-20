from flask import Flask, jsonify, render_template
# Create Flask application
app = Flask(__name__)
# Sample student data (No database)
students = [
{
"id": 1,
"name": "Rahul Patil",
"course": "FYBCA",
"city": "Kolhapur",
"email": "rahul@gmail.com"
},
{
"id": 2,
"name": "Priya Sharma",
"course": "FYBCA",
"city": "Pune",
"email": "priya@gmail.com"
},
{
"id": 3,
"name": "Amit Shah",
"course": "FYBCA",
"city": "Mumbai",
"email": "amit@gmail.com"
}
]
# Sample course data
courses = [
{"id": 1, "name": "BCA", "duration": "3 Years"},
{"id": 2, "name": "BBA", "duration": "3 Years"},
{"id": 3, "name": "BSc", "duration": "3 Years"}
]
# Sample faculty data
faculty = [
{"id": 1, "name": "Prof. Patil", "subject": "Python"},

{"id": 2, "name": "Prof. Sharma", "subject": "Database"},
{"id": 3, "name": "Prof. Joshi", "subject": "Web Technology"}
]

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# GET API: Display all students
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET API: Display individual student
@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({
        "message": "Student not found"
    }), 404

# GET API: Display all courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

# GET API: Display all faculty
@app.route('/api/faculty', methods=['GET'])
def get_faculty():
    return jsonify(faculty)

# Run application

if __name__ == '__main__':
    app.run(debug=True)