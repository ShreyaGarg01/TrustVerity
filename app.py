from flask import Flask, render_template, request, Markup
import numpy as np
import requests
from CountReviews.py import get_reviews

#  FLASK APP 
app = Flask(__name__)


# RENDER PREDICTION PAGE

@ app.route('/fraud-predict', methods=['POST'])
def fraud_prediction():

    if request.method == 'POST':
        idd = string(request.form['url'])
        # gotta extract exact id from url by python string formatting

        ans=get_reviews(idd)
        return render_template('fraud_prediction.html', answer=fans)



if __name__ == '__main__':
    app.run(debug = True)