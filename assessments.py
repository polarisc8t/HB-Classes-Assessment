"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   
   PAE - polymorphism, abstract, and encapsulated
   
   polymorphism - refers to the ability of an object to adapt the code to the type of the data it is processing
   abstract -  enforce that derived classes implement particular methods from the base class
   encapsulated - the mechanism for restricting the access to some of an object's components, this means that the internal representation of an object can't be seen from outside of the objects definition.

2. What is a class?
    A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

3. What is an instance attribute?
    An attribute defined in the instance, by assignment, is an instance attribute and is stored in the instance's name space

4. What is a method?
        a function which is a member of a class

5. What is an instance in object orientation?


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   In the class attribute case, there is just one object referred to. In the instance-attribute-set-at-instantiation, there can be multiple objects referred to.
   
   The difference is that the attribute on the class is shared by all instances. The attribute on an instance is unique to that instance.


"""


# Parts 2 through 5:
# Create your classes and class methods



class Student(object):
    """this is a class of student object"""

    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address







class Question(object):
    """Question class"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ ask and evaluate - question...

        """

        print self.question,
        answer = raw_input("> ")
        return self.correct_answer == answer






class Exam(object):
    """ class with exam object ."""

    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def add_question(self, question, correct_answer):

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)

    def administer(self):

        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return float(score)/len(self.questions)



