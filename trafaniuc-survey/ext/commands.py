import click
from flask import Flask
from .database import db
from ..models.user import User
from ..models.survey import Survey, SurveyQuestion, SurveyQuestionOption, SurveyStatus, SurveyQuestionScheme


def create_db():
    collections = ['surveys', 'users']
    existing_collections = db.db.collection_names()
    for collection in collections:
        if not collection in existing_collections:
            db.db.create_collection(collection)


def populate_db():
    user = User(email='jonatastrafaniuc@gmail.com',
                name='Jonatas Dinelli Trafaniuc').get_doc()
    surveys = [
        Survey(owner='jonatastrafaniuc@gmail.com', title='Sistemas operacionais', status=SurveyStatus.draft, questions=[
            SurveyQuestion(text='Qual sistema operacional você utiliza?', scheme=SurveyQuestionScheme.exclusive, options=[
                SurveyQuestionOption(order=1, text='Windows'),
                SurveyQuestionOption(order=2, text='Linux'),
                SurveyQuestionOption(order=3, text='MacOS')
            ])
        ]).get_doc(),
        Survey(owner='jonatastrafaniuc@gmail.com', title='Sistemas operacionais Móveis', status=SurveyStatus.draft, questions=[
            SurveyQuestion(text='Qual sistema operacional você utiliza?', scheme=SurveyQuestionScheme.exclusive, options=[
                SurveyQuestionOption(order=1, text='iOS'),
                SurveyQuestionOption(order=2, text='Android')
            ])
        ]).get_doc()
    ]
    db.db.users.insert_one(user)
    db.db.surveys.insert_many(surveys)


def init_app(app: Flask):
    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(populate_db))
