from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
#========================================================================
# **uni ---> University
# Con--->Contacts;
# Add---> address
# **Loc---> Location
class University(models.Model):
    uni_Name = models.CharField(max_length = 200)
    uni_Location= models.CharField(max_length=200)
    uni_Con= models.IntegerField()
    uni_Add = models.CharField(max_length=200)
    uni_Desc = models.CharField(max_length= 20000) 

    def __str__(self):
        return self.uni_Name


#=============================================================================
#Desc ---->Description
# fac----> Faculty
# v---> vision
class Faculty(models.Model):
    Uni_Name = models.ForeignKey(University, null= True , on_delete=models.SET_NULL)
    fac_Name =models.CharField(max_length = 200)
    fac_Motto = models.CharField(max_length= 200)
    fac_v = models.CharField(max_length= 200)



    def __str__(self):
        return self.fac_Name
#==============================================================================
# dep ---> department
class Department (models.Model):
    fac_Name =models. ForeignKey(Faculty, null= True , on_delete=models.SET_NULL)
    dep_Name = models.CharField (max_length= 200)
    dep_Staff = models.IntegerField()
    def __str__(self):
        return self.dep_Name 

#=======================================
class Units(models.Model):
    course_Tittle = models.CharField(max_length= 200)
    course_Code  = models.CharField(max_length=200)
    semester = models.CharField(max_length=5)

    def __str__(self):
        return self.course_Code

#===================================================================
class Programme (models.Model):
    department = models.ForeignKey(Department, null= True , on_delete=models.SET_NULL)
    units = models.ForeignKey(Units, null= True , on_delete=models.SET_NULL)
    programme_Name = models.CharField (max_length= 200)
    
    def __str__(self):
        return self.programme_Name

        
#================================================
class Student(models.Model):
    # STATUS = (
    #     ('Pending', 'Confirmed'),
    #     ('Select', 'Remove'),
    #     )
    # units=models.ForeignKey(Units, null= True , on_delete=models.SET_NULL)
    user= user = models.OneToOneField(User, null=True, on_delete= CASCADE)
    programme = models.ForeignKey(Programme, null= True , on_delete=models.SET_NULL)
    student_Regno = models.CharField(max_length= 200, primary_key = True)
    student_Name = models.CharField(max_length = 200)
    student_Phone_Number = models.IntegerField()
    student_Email = models.EmailField(max_length= 254)
    #statu = models.CharField(max_length=200, null=True, choices = STATUS )
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.student_Regno

#=================================================
class Subject(models.Model):
    subject_Name = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.subject_Name

#============================================

class Zone(models.Model):
    zone_Name = models.CharField(max_length=200)
    zone_Description= models.CharField(max_length=200)
    zone_Id = models.CharField(max_length = 200, primary_key=True)


    def __str__(self):
        return self.zone_Name

#=========================================
class School(models.Model):
    zone_Id= models.ForeignKey(Zone, null= True , on_delete=models.SET_NULL)
    school_Name = models.CharField(max_length = 200)
    school_Id  = models.CharField(max_length=200, primary_key= True)
    subject = models.ManyToManyField(Subject)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.school_Name
#===========================================
class Placement (models.Model):
    STATUS = (
        ('Pending','Pending'),
        ( 'Aprove','Confirmed'),
        )
    student_Regno = models.ForeignKey(Student,null = True, on_delete= models.SET_NULL)
    school_Id = models.ForeignKey(School,null = True, on_delete= models.SET_NULL)
    placement_Id = models.CharField(max_length=200, primary_key= True)
    status = models.CharField(max_length=200, null=True, choices = STATUS )
    date = models.DateField(auto_now_add=True)
     