from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Faculty(Base):
    __tablename__ = "faculties"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    students = relationship("Student", back_populates="faculty")

    def __repr__(self):
        return f"<Faculty(id={self.id}, name='{self.name}')>"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculties.id"), nullable=True)

    faculty = relationship("Faculty", back_populates="students")
    grades = relationship("Grade", back_populates="student", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("last_name", "first_name", name="uq_student_name"),
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.last_name} {self.first_name}', faculty_id={self.faculty_id})>"

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_name = Column(String(100), nullable=False)
    score = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="grades")

    def __repr__(self):
        return f"<Grade(student_id={self.student_id}, course='{self.course_name}', score={self.score})>"