# app.py

from flask import Flask, request, render_template
import bot_functions as bf
import logging

import json
app = Flask(__name__, template_folder="views")


@app.route('/')  # create a route for / - just to test server is up.
def index():
    items = []
    return render_template(
        "main.html",
        items=items,
    )


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        items = request.form.get('messages')
        if items:
            items = json.loads(items)

            for item in items:
                bf.save_order(
                    candle_period=item['analysis']['config']['candle_period'] or '',
                    indicator=item['indicator'],
                    market=item['market'],
                    exchange=item['exchange'],
                    price=item['price_value']['close'] or 0,
                    type=item['status'],
                    last_status=item['last_status'],
                    cause="%s %s" % (item['indicator'], item['status'])
                )
        return 'Trade webhook trigger', 202
    else:
        return 'POST Method not supported', 405


app.run(host='0.0.0.0', port=3000)
