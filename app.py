# app.py

from flask import Flask, request, render_template
import bot_functions as bf
import logging

import json
app = Flask(__name__, template_folder="views")


@app.route('/')  # create a route for / - just to test server is up.
def index():
    items = bf.tradesDb.getAll()
    return render_template(
        "main.html",
        items=json.dumps(items),
    )


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        items = request.form.get('messages')
        if items:
            items = json.loads(items)

            for item in items:
                bf.save_order(
                    candle_period=item['analysis']['config']['candle_period'] if item['analysis']['config'] else '',
                    indicator=item['indicator'],
                    market=item['market'],
                    exchange=item['exchange'],
                    price=item['price_value']['close'] if item['price_value'] else 0,
                    type=item['status'],
                    last_status=item['last_status'],
                    cause="%s %s" % (item['indicator'], item['status'])
                )
        return 'Trade webhook trigger', 202
    else:
        return 'POST Method not supported', 405


app.run(host='0.0.0.0', port=3000, debug=True)
