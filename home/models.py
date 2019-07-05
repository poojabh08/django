from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField('Student name',max_length=30,null=False)
    dept=(
        ('CSE','Computer Science'),
        ('MH','mech'),
        ('CV','Civil'),
    )
    # photo=models.ImageField(upload_to='media/',null=True)
    department=models.CharField('Department',choices=dept, blank=True,null=True,max_length=30)

    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name


'''def calc(Items):
    if Items=='Chocolate':
        return 25
    # elif Items=='Soap':
    #     return 30
    # elif Items=='powder':
    #     return 40
class Itemss(models.Model):
    customer=models.CharField('Name',max_length=30,null=True)
    var=(
        ('Ch','Chocolate'),
        ('sp','Soap'),
        ('pw','powder'),
    )
    Items=models.CharField('Items',choices=var,blank=True,null=True,max_length=30)
    price=models.CharField(calc(Items),max_length=20)
'''
class Section(models.Model):
    advisor=models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    Students=models.ManyToManyField('Student')
    Section=models.CharField('section',max_length=100,null=False)
    def __str__(self):
        return self.Section

class Teacher(models.Model):
    teacher=models.CharField('Teacher_name',max_length=100,null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher

'''class library(models.Model):
    sut=models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    books=(
        ('EE','Electrical'),
        ('EC','Electronics'),
        ('CS','Comp. Science'),
    )
    book_name=models.CharField('Book name',choices=books,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)'''
#class medical(models.Model):
class books(models.Model):
    book=models.CharField('book',max_length=100,null=True)
    def __str__(self):
        return self.book 
class library(models.Model):
    sut=models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)
    libraryname=models.CharField('library',null=True,max_length=100)
    books=models.ManyToManyField('books',null=True)
    def __str__(self):
        return self.libraryname



