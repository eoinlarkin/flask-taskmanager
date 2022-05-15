from taskmanager import db

class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    task = db.relationship("Task", backref = "category", cascade="all, delete", lazy=True)

    # creating a unique category name with a length of 25 
    category_name = db.Column(db.String(25), unique=True, nullable=False) 

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self

class Task(db.Model):
    # schmea for the Task model:
    id = db.Column(db.Integer, primary_key = True)

    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False) 
    dub_date = db.Column(db.Date, nullable=False)

    # linking the tables on the category_id foreign key
    # the ondelete makes sure that when we delete the category, the underlying taskes are also deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"'{self.id} - Task:{self.task_name} | Urgent: {self.is_urgent}"