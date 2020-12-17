import random
from flask import Flask, jsonify, request
from jokes import jokesHisp, jokesAsian, jokesBlack, jokesCau
import string
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ('Hello World')
# Get Data Routes
def mask():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(13):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password
@app.route('/noMask')
def noMask():
    return 'We apologyze but no access without FaceMask :('
    

if __name__ == '__main__':
    app.run()