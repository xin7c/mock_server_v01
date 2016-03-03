#!/usr/bin/python
# coding=utf-8
from flask import Flask, request, jsonify, make_response, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/todo/post', methods=['POST', 'GET'])
def todo_post():
    if request.method == 'POST':
        # print request.method
        # print request.headers
        print request.data
        return make_response(jsonify({'ok': 'Success'}), 200,
                             {"add_Headers": "add_Headers!", 'Server': 'Xc-Mock-Server'})

    elif request.method == 'GET':
        # print request.headers
        # print request.method
        # print request.data
        return "<title>试验田</title>" \
               "请来一发post请求! 你当前的方法为[%s], 数据为[%s]<hr/><b>%s<b>" % \
               (request.method, request.data, request.headers)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
