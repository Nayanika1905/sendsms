# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo

app = Flask(__name__, static_url_path='')


@app.route('/send_sms/')# methods=['POST'])
def outbound_sms():

    client = plivo.RestClient('auth_id', 'auth_token')
    try:
        resp = client.messages.create(
            src='', # Sender's phone number with country code
            dst='', # Receiver's phone Number with country code
            text='Hii Naina!!!You have got a missed call!!!!',
        )
        # print(response)
        return str(resp)
    except plivo.exceptions.PlivoRestError as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)
