from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

class Course(models.Model):
    name = models.CharField(max_length=255)
    minimum_grade_to_pass = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(20.0)
        ],
        help_text="the range for this field is from 0 to 20"
    )

    def __str__(self):
        return self.name


class CourseStep(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' in ' + self.course.name


class Student(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class CourseStudentRelationship(models.Model):
    semester = models.CharField(
        max_length=4,
        validators=[
            RegexValidator(
                regex='^[1-9]\d{3}$',
                message='Enter a 4-digit number between 1000 and 9999',
                code='invalid_four_digit_number'
            )
        ]
    )
    grade = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(20.0)
        ],
        help_text="the range for this field is from 0 to 20",
        blank=True, null=True,
    )
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['student', 'course', 'semester',]

    def __str__(self):
        return self.course.name + ', ' + self.student.full_name