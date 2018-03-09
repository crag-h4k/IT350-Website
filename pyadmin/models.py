from django.db import models

from django.db import models

class Account(models.Model):
	#pk
	accountID = models.AutoField(primary_key=True)
	password = models.CharField(max_length=50)
	creationDate = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
	#pk
	customerID = models.AutoField(primary_key=True)
	#fk
	accountID = models.ForeignKey(Account,to_field= 'accountID', on_delete=models.PROTECT)
	username = models.CharField(max_length=50, unique=True)
	#
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	email = models.EmailField()
	#
	starchPref = models.CharField(max_length=50, blank=True)
	proteinPref = models.CharField(max_length=50, blank=True)
	flavorPref =  models.CharField(max_length=50, blank=True)
	vegan =  models.BooleanField(default=False)
	vegetarian = models.BooleanField(default=False)
	glutenFree = models.BooleanField(default=False)
	#
	updated = models.DateTimeField(auto_now=True)
'''	def __str__(self):
		return self.userID + ": "self.lastName + " " + self.firstName
'''
class Shipping(models.Model):
	#pk/fk!
	customerID = models.ForeignKey(Customer, to_field='customerID', on_delete=models.PROTECT)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	phoneNum = models.CharField(max_length=12, blank=True)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=20)
	zipCode = models.PositiveIntegerField()

class Billing(models.Model):
	#pk
	billingID = models.AutoField(primary_key=True)
	#fk
	accountID = models.ForeignKey(Account, to_field='accountID', on_delete=models.PROTECT)
	#?fk, needs to be fk of CustomerActive?
	autoBillingOn = models.BooleanField(default=False)
	chargeInterval = models.PositiveIntegerField()
	chargeAmount = models.CharField(max_length=7)
	paypalEmailAccount = models.EmailField()

class Employee(models.Model):
	#pk
	empID = models.AutoField(primary_key=True)
	#fk
	accountID = models.ForeignKey(Account, to_field='accountID', on_delete=models.PROTECT)
	#I think the other classes for each role aren't really needed
	#I just need to figure out how to structure the recursive relationships of 
	#type of employee
	#the different roles include Fulfillment, Customer_Service, Sales, Chef, Web_Dev
	role = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	phone = models.CharField(max_length=12)
	#password field! 
	password = models.CharField(max_length=50)
	pay = models.PositiveIntegerField()

class Meal(models.Model):
	#pk
	mealID = models.AutoField(primary_key=True)
	#fk empID of the chef who prepared it
	empID  = models.ForeignKey(Employee, to_field='empID', on_delete=models.PROTECT)
	mealName = models.CharField(max_length=50, unique=True)
	flavor = models.CharField(max_length=50)
	protein = models.CharField(max_length=50)
	starch = models.CharField(max_length=50)

	vegan =  models.BooleanField()
	vegetarian = models.BooleanField()
	glutenFree = models.BooleanField()
	
class Order(models.Model):
	#pk
	orderID = models.AutoField(primary_key=True)
	#fk
	customerID = models.ForeignKey(Customer, to_field='customerID', on_delete=models.PROTECT)
	#fk for sales employee
	empID = models.ForeignKey(Employee, to_field='empID', on_delete=models.PROTECT)
	orderDate = models.DateTimeField(auto_now_add=True)
	#all meals are FKs and instances of class Meal
	''' NEED TO FIGURE OUT HOW TO MAKE INSTANCES OF A MODEL
	meal_1 = models.ForeignKey(Meal, to_field='mealName', on_delete=models.PROTECT)
	meal_2 = models.ForeignKey(Meal, to_field='mealName', on_delete=models.PROTECT)
	meal_3 = models.ForeignKey(Meal, to_field='mealName', on_delete=models.PROTECT)
'''
class Meal_Review(models.Model):
	#pk
	mealReviewID = models.AutoField(primary_key=True)
	#fk
	mealName = models.ForeignKey(Meal, to_field='mealName', on_delete=models.PROTECT)
	#fk
	userName = models.ForeignKey(Customer, to_field='username', on_delete=models.PROTECT) 
	reviewText = models.CharField(max_length=500)

class Meal_History(models.Model):
	#pk
	historyItemID = models.AutoField(primary_key=True)
	#fk
	mealName = models.ForeignKey(Meal, to_field='mealName', on_delete=models.PROTECT)
	#fk
	customerID = models.ForeignKey(Customer,to_field='customerID', on_delete=models.PROTECT)
	#fk
	mealReviewID = models.ForeignKey(Meal_Review, to_field='mealReviewID', on_delete=models.PROTECT)

'''
class Fulfillment(models.Model):
	userID = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
class Customer_Service(models.Model):
	userID = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
class Sales(models.Model):
	userID = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
class Chef(models.Model):
	userID = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
'''	

