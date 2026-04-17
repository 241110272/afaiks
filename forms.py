from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 128)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 200)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=1000)])
    deadline = DateField('Deadline', validators=[Optional()], format='%Y-%m-%d')
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    status = SelectField('Status', choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    category = StringField('Category', validators=[Optional(), Length(max=100)])
    tags = StringField('Tags', validators=[Optional(), Length(max=200)])
    assignee = SelectField('Assign to', coerce=int, choices=[], validators=[Optional()])
    submit = SubmitField('Save Task')

class FilterForm(FlaskForm):
    search = StringField('Search', validators=[Optional(), Length(max=200)])
    category = StringField('Category', validators=[Optional(), Length(max=100)])
    priority = SelectField('Priority', choices=[('', 'All'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    status = SelectField('Status', choices=[('', 'All'), ('Pending', 'Pending'), ('Completed', 'Completed')])
    submit = SubmitField('Filter')
