[![YK logo](taskmanager/static/img/yodaKode-sml.png)](https://github.com/roeszler) 

## MINI PROJECT - Student Class Database (Unittest):
* GitHub: https://github.com/roeszler/unittest-student-class
* Live App via Heroku: 

## Summary:
This project applies Structured Query Language (SQL) to and from a test database following the Create, Read, Update, Delete (C.R.U.D) paradigm using primarily Python and a variety of plugins. 

It demonstrates the application of the highest layer of abstraction uses SQLAlchemy's full Object Relational Mapping (ORM) capabilities inc conjunction with the Flask framework with the Materialize CSS and Jinja template engines. This demonstrates the use of Python classes and objects, instead of using database tables and connections. 

Requirements include:
* click==8.1.3
* Flask==2.1.3
* Flask-SQLAlchemy==2.5.1
* psycopg2==2.9.3
* SQLAlchemy==1.4.39
* Werkzeug==2.1.2

and including:

* Jinja2==3.0.1
* MaterializeCss==1.0.0

### What is it?
The app is a simple 
### What does it do?

### How do you use it?


Using:
* Flask, (Thorin Site)
* SLQAlchemy ORM,  (PostgreSQL Databases)
* Materialize frontend CSS framework
  * Alternatives:
    * Bootstrap
    * Material Design Bootstrap
	* Do not mix the frameworks; they often use the same elements, IDs, and class names and will get confused


Outcomes:
* How to perform full CRUD functionality, which allows us to create, read, update, and delete items on our database. This will be done in the context of a Flask application with SLQAlchemy’s ORM.
* Create HTML-based user interfaces to demonstrate these CRUD calls in action.
* In the spirit of good user experience, we will style these interfaces using the Materialize frontend framework.

Install addons:
`$ pip3 install Flask-SQLAlchemy psycopg2`

Secrets:
`$ touch env.py`
etc...


a foreign key pointing to the specific category, which will be our category_id.
for the data-type we need to use db.ForeignKey so our database recognizes the relationship between our tables
point to the ID from our Category class, and therefore we need to use lowercase 'category.id' in quotes.

Since each of our tasks need a category selected, this is what's known as a one-to-many relationship.
One category can be applied to many different tasks, but one task cannot have many categories.
If we were to apply many categories to a single task, this would be known as a many-to-many relationship.
The ondelete="CASCADE" comes into play, and essentially means that once a category is deleted, it will 
perform a cascading effect and also delete any task linked to it.

`category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)`


[![one-to-many](taskmanager/static/img/1-one-to-many-relationship.png)](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DB101+2021_T1/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

[![delete-cat](taskmanager/static/img/2-delete-catagoy-error.png)](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DB101+2021_T1/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

[![ondelete-cascade](taskmanager/static/img/3-ondelete-CASCADE.png)](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DB101+2021_T1/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

