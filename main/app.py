from flask import Flask, render_template, request
# from .model import model
# from .model_input import exp


def create_app():
    '''Creates application page

    :returns:
    :rtype:
    '''

    APP = Flask(__name__)

    @APP.route('/')
    def form():
        '''

        :returns:
        :rtype:
        '''
        return render_template('base.html')

    @APP.route('/data', methods=['POST', 'GET'])
    def root():
        '''Takes user input and produces kickstarter outcome

        :returns: html page with input fields and model results
        :rtype: html page
        '''
        if request.method == 'GET':
            return "/data is accessed directly. Go to '/' to submit form"

        # if request.method == 'POST':
        #
        #     song_input = request.form.get('song')
        #
        #     user_input = exp(song_input)
        #
        # prob = model(user_input)
        #
        # return render_template('base.html', status=prob)

    return APP
