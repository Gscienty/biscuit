from flask import jsonify


def created():
    return jsonify({
        'status': 'success',
        'reason': 'Created'
    }), 201


def bad_request():
    return jsonify({
        'status': 'error',
        'reason': 'Bad Request'
    }), 400


def not_found():
    return jsonify({
        'status': 'error',
        'reason': 'Not Found'
    }), 404


def method_not_allowed():
    return jsonify({
        'status': 'error',
        'reason': 'Method Not Allowed'
    }), 405


def conflict():
    return jsonify({
        'status': 'error',
        'reason': 'Conflict'
    }), 409


def service_unavailable():
    return jsonify({
        'reason': 'Service Unavailable'
    }), 503
