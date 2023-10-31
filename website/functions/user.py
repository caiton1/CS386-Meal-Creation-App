'''@author: caiton1'''
from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
from flask_session import Session


class UserData:
    def __init__(self):
        self.data = {

            'favorites': '',
            'meal_plan': ''
        }
        self.recipe_list = {}
        self.title_list = {}
        self.links = {}
        self.user = {}

    # --------------------------Data Minipulation---------------------------#

    # turns recipies stored in user database into a dictionary to display as links
    def user_recipies_to_links(self, db, token, list):
        self.links = {}
        self.user = db.child('user').get()
        for favorite in self.user.val()[token][list]:
            self.links.update({
                favorite: {
                    'href': favorite.replace(' ', '+'),
                    'caption': favorite
                }
            })
        return self.links

    # turns recipies stored in recipies into a dictionary to diplay as links
    def recipe_to_links(self, db):
        self.recipe_list = db.child('Recipes').get()
        self.title_list = {}

        for recipe in self.recipe_list:
            self.title_list.update({recipe.key(): {
                'href': recipe.key().replace(' ', '+'),
                'caption': recipe.key()
            }})

        return self.title_list

    # ---------------------------Data Retrieval-----------------------------#
    # gets data from a selected recipe
    def get_recipe_data(self, db, selection):
        self.data = db.child('Recipes').child(selection).get()
        return self.data

    def get_recipes(self, db):
        self.data = db.child('Recipes').get()
        return self.data

    # gets user data
    def get_user_data(self, db):
        self.user = db.child('user').get()
        return self.user

    # gets login/signup form data from webpage
    def forms(self, form):
        self.email = form['email']
        self.password = form['pass']

    # ---------------------------User Management---------------------------- #
    # creates user on authenticator and pushes user into database for persistant storage
    def create_user(self, auth, db):
        self.user_token = auth.create_user_with_email_and_password(self.email, self.password)
        db.child('user').child(self.user_token['localId']).update(self.data)

    # logs user in
    def login(self, auth):
        self.user_token = auth.sign_in_with_email_and_password(self.email, self.password)

    def logoff(self):
        self.user_token = ''
