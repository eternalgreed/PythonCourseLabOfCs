import unittest

from main import Course, GradeBook, Student, TextReportPrinter


class GradeBookTest(unittest.TestCase):
    def test_adds_students_courses_and_grades(self) -> None:
        gradebook = GradeBook()
        student = Student(id=1, first_name="Anna", last_name="Ivanova")
        course = Course(title="Python")

        gradebook.add_student(student)
        gradebook.add_course(course)
        gradebook.add_grade(student_id=1, course_title="Python", grade=5)
        gradebook.add_grade(student_id=1, course_title="Python", grade=4)

        self.assertEqual(gradebook.student_average(1), 4.5)
        self.assertEqual(gradebook.course_average("Python"), 4.5)

    def test_returns_none_for_student_without_grades(self) -> None:
        gradebook = GradeBook()
        gradebook.add_student(Student(id=1, first_name="Oleg", last_name="Petrov"))

        self.assertIsNone(gradebook.student_average(1))

    def test_validates_grade_range(self) -> None:
        gradebook = GradeBook()
        gradebook.add_student(Student(id=1, first_name="Anna", last_name="Ivanova"))
        gradebook.add_course(Course(title="Python"))

        with self.assertRaises(ValueError):
            gradebook.add_grade(student_id=1, course_title="Python", grade=6)

    def test_builds_text_report(self) -> None:
        gradebook = GradeBook()
        gradebook.add_student(Student(id=1, first_name="Anna", last_name="Ivanova"))
        gradebook.add_course(Course(title="Python"))
        gradebook.add_grade(student_id=1, course_title="Python", grade=5)

        report = TextReportPrinter().build_report(gradebook)

        self.assertIn("Anna Ivanova", report)
        self.assertIn("Python: 5", report)
        self.assertIn("Average: 5.00", report)


if __name__ == "__main__":
    unittest.main()
