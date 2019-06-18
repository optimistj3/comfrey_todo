from flask import Flask, request, url_for, redirect, session
from flaskext.mysql import MySQL
from passlib.hash import pbkdf2_sha256 as sha

import datetime
import jwt
import logging
import requests

@app.route("/api/item")
def item():

@app.route("/api/user")
def user():

@app.route("/api/list")
def lists():