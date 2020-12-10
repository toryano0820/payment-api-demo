from flask import Flask, request, jsonify
from payment_methods import get_from_kwargs as get_payment_method
from payment_gateways import process_payment
from datetime import datetime
import traceback


app = Flask(__name__)


@app.route('/ProcessPayment', methods=['POST'])
def api_process_payment():
    try:
        params = request.json
        amount = params.pop('Amount')
        payment_method = get_payment_method(**params)

        return jsonify({
            'message': process_payment(amount, payment_method)
        }), 200
    except AttributeError:
        raise ValueError('invalid content type: expected JSON')
    except KeyError as ex:
        raise ValueError(f'required field missing: {ex.args[0]}')


@app.errorhandler(ValueError)
def error_400(ex):
    return jsonify({
        'error': 'bad request',
        'type': ex.__class__.__name__,
        'message': ex.args[0]
    }), 400


@app.errorhandler(Exception)
def error_500(ex):
    return jsonify({
        'error': 'internal server error',
        'type': ex.__class__.__name__,
        'message': ex.args[0]
    }), 500


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
