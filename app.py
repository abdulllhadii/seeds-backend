from flask import Flask, jsonify, request
from data import students, teachers

app = Flask(__name__)

@app.route('/courses/student/<student_id>', methods=['GET'])
def get_student_courses(student_id):
    courses = students.get(student_id)
    if courses is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"student": student_id, "courses": courses})

@app.route('/courses/teacher/<teacher_id>', methods=['GET'])
def get_teacher_courses(teacher_id):
    courses = teachers.get(teacher_id)
    if courses is None:
        return jsonify({"error": "Teacher not found"}), 404
    return jsonify({"teacher": teacher_id, "courses": courses})

if __name__ == '__main__':
    app.run(debug=True)
 