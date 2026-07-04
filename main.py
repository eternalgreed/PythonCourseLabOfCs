from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Protocol


@dataclass
class Student:
    id: int
    first_name: str
    last_name: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@dataclass
class Course:
    title: str
    grades_by_student: Dict[int, List[int]] = field(default_factory=dict)

    def add_grade(self, student_id: int, grade: int) -> None:
        if not 2 <= grade <= 5:
            raise ValueError("Grade must be between 2 and 5")

        self.grades_by_student.setdefault(student_id, []).append(grade)

    def student_grades(self, student_id: int) -> List[int]:
        return self.grades_by_student.get(student_id, []).copy()

    def average(self) -> Optional[float]:
        all_grades: List[int] = [
            grade
            for grades in self.grades_by_student.values()
            for grade in grades
        ]
        if not all_grades:
            return None

        return sum(all_grades) / len(all_grades)


class ReportPrinter(Protocol):
    def build_report(self, gradebook: "GradeBook") -> str:
        ...


class GradeBook:
    def __init__(self) -> None:
        self._students: Dict[int, Student] = {}
        self._courses: Dict[str, Course] = {}

    def add_student(self, student: Student) -> None:
        if student.id in self._students:
            raise ValueError(f"Student with id {student.id} already exists")

        self._students[student.id] = student

    def add_course(self, course: Course) -> None:
        if course.title in self._courses:
            raise ValueError(f"Course {course.title!r} already exists")

        self._courses[course.title] = course

    def add_grade(self, student_id: int, course_title: str, grade: int) -> None:
        student = self._students.get(student_id)
        if student is None:
            raise ValueError(f"Student with id {student_id} was not found")

        course = self._courses.get(course_title)
        if course is None:
            raise ValueError(f"Course {course_title!r} was not found")

        course.add_grade(student.id, grade)

    def student_average(self, student_id: int) -> Optional[float]:
        if student_id not in self._students:
            raise ValueError(f"Student with id {student_id} was not found")

        grades: List[int] = []
        for course in self._courses.values():
            grades.extend(course.student_grades(student_id))

        if not grades:
            return None

        return sum(grades) / len(grades)

    def course_average(self, course_title: str) -> Optional[float]:
        course = self._courses.get(course_title)
        if course is None:
            raise ValueError(f"Course {course_title!r} was not found")

        return course.average()

    def students(self) -> List[Student]:
        return list(self._students.values())

    def courses(self) -> List[Course]:
        return list(self._courses.values())


class TextReportPrinter:
    def build_report(self, gradebook: GradeBook) -> str:
        lines: List[str] = ["Student grade report", ""]

        for student in gradebook.students():
            average = gradebook.student_average(student.id)
            average_text = "no grades" if average is None else f"{average:.2f}"
            lines.append(f"{student.full_name}")
            lines.append(f"Average: {average_text}")

            for course in gradebook.courses():
                grades = course.student_grades(student.id)
                if grades:
                    grades_text = ", ".join(str(grade) for grade in grades)
                    lines.append(f"{course.title}: {grades_text}")

            lines.append("")

        return "\n".join(lines).strip()


def fill_demo_gradebook() -> GradeBook:
    gradebook = GradeBook()

    gradebook.add_student(Student(id=1, first_name="Anna", last_name="Ivanova"))
    gradebook.add_student(Student(id=2, first_name="Oleg", last_name="Petrov"))
    gradebook.add_student(Student(id=3, first_name="Maria", last_name="Sidorova"))

    gradebook.add_course(Course(title="Python"))
    gradebook.add_course(Course(title="Databases"))

    gradebook.add_grade(student_id=1, course_title="Python", grade=5)
    gradebook.add_grade(student_id=1, course_title="Python", grade=4)
    gradebook.add_grade(student_id=1, course_title="Databases", grade=5)
    gradebook.add_grade(student_id=2, course_title="Python", grade=3)
    gradebook.add_grade(student_id=2, course_title="Databases", grade=4)
    gradebook.add_grade(student_id=3, course_title="Python", grade=5)

    return gradebook


def print_report(printer: ReportPrinter, gradebook: GradeBook) -> None:
    print(printer.build_report(gradebook))


def main() -> None:
    gradebook = fill_demo_gradebook()
    printer = TextReportPrinter()
    print_report(printer, gradebook)


if __name__ == "__main__":
    main()
