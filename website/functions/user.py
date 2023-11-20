'''@author: caiton1'''
from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
from flask_session import Session


# TODO: improve, some functions could be argued dont belong in this class
class UserData:
    """This object will handle part of the user data management, transformation and interaction with firebase"""
    def __init__(self):
        self.data = {

            'favorites': '',
            'meal_plan': '',
            'shopping_list': ''
        }
        self.email = ''
        self.password = ''
        self.recipe_list = {}
        self.title_list = {}
        self.links = {}
        self.user = {}

    # --------------------------Data Minipulation---------------------------#
    def user_recipies_to_links(self, db, token, attribute):
        """turns recipies stored in user database into a dictionary to display as links on html
        :param db reference to the database (firebase real time database)
        :param token user token, used to read right user in database
        :param attribute which attribute of the user to list
        :returns List of links
        """
        self.links = {}
        self.user = db.child('user').get()
        for favorite in self.user.val()[token][attribute]:
            self.links.update({
                favorite: {
                    'href': favorite.replace(' ', '+'),
                    'caption': favorite
                }
            })
        return self.links

    def recipe_to_links(self, db):
        """turns recipies stored in database into a dictionary to display as links
        :param db reference to database
        :returns List of recipe links
        """
        self.recipe_list = db.child('Recipes').get()
        self.title_list = {}

        for recipe in self.recipe_list:
            self.title_list.update({recipe.key(): {
                'href': recipe.key().replace(' ', '+'),
                'caption': recipe.key()
            }})
            
        return self.title_list

    def list_to_links(self, recipe_list):
        """turns a list of recipies into a list of recipe links
        :param recipe_list: a string list of recipies
        :returns A list of recipe links
        """
        self.title_list = {}
        for recipe in recipe_list:
            self.title_list.update({recipe: {
                'href': recipe.replace(' ', '+'),
                'caption': recipe
            }})
        return self.title_list

    # ---------------------------Data Retrieval-----------------------------#
    def get_recipe_data(self, db, selection):
        """gets data from a selected recipe
        :param db: reference to database
        :param selection: what recipe
        :returns selected recipe data
        """
        self.data = db.child('Recipes').child(selection).get()
        return self.data

    # TODO: not good approach for at full scale
    def get_recipes(self, db):
        """gets recipe (titles) in database to display
        :param db: reference to database
        :returns List of available recipies
        """
        self.data = db.child('Recipes').get()
        return self.data

    def get_user_data(self, db):
        """gets user data
        WARNING: exploitable approach if not used carefully (not that we store any important info on this database)
        Keyword arguments:
        :param db: reference to db
        :returns List of user IDs
        """
        self.user = db.child('user').get()
        return self.user

    #
    def login_info(self, form):
        """ gets login/signup form data from webpage, meant to simplify user management, not secure.
        :param form: reference to data that the form tag returns from HTML
        """
        self.email = form['email']
        self.password = form['pass']

    # ---------------------------User Management---------------------------- #

    def create_user(self, auth, db):
        """ creates user on authenticator and pushes user into database for persistent storage
        :param auth: reference to authenticator
        :param db: reference to database
        """
        self.user_token = auth.create_user_with_email_and_password(self.email, self.password)
        db.child('user').child(self.user_token['localId']).update(self.data)

    def login(self, auth):
        """ logs user in
        :param auth: reference to authenticator
        """
        self.user_token = auth.sign_in_with_email_and_password(self.email, self.password)

    def logoff(self):
        self.user_token = ''

