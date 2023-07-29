from flask import Flask, request, render_template
import numpy as np
# import requests
import warnings

from CountReviews import get_reviews
warnings.filterwarnings("ignore")

#  FLASK APP 
app = Flask(__name__)


# RENDER PREDICTION PAGE

@ app.route('/')
def start():
    title = 'Home'
    # active_page = 'home'
    return render_template('index.html', title=title)


@ app.route('/home')
def home():
    title = 'Home'
    # active_page = 'home'
    return render_template('index.html', title=title)


@ app.route('/getresponse')
def getresponse():
    title = 'Check the apps'
    # active_page = 'home'
    return render_template('getresponse.html', title=title)

@ app.route('/result', methods=['GET', 'POST'])
def result():

    # if request.method == 'POST':
        url_id = str(request.form['url'])
        print(url_id)
        # gotta extract exact id from url by python string formatting
        if (len(url_id) == 0 or url_id.find('=') == -1): 
            return render_template('getresponse.html', answer="Enter a valid link!")
             
             

        finid = url_id[url_id.index('=') + 1 : ]
        if (finid.find('&') != -1):
            finid = finid[:finid.index('&')]
        print(finid)
        ans=get_reviews(finid)
        return render_template('getresponse.html', answer=ans)



if __name__ == '__main__':
    app.run(debug = True)