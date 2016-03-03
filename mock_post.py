#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'

import json
import requests


class mock_post(object):
    def __init__(self):
        self.url = "http://127.0.0.1:5000/todo/post"

    def req_post(self):
        data = {
            "a": 1,
            "b": 2
        }
        r = requests.post(url=self.url, data=json.dumps(data))
        print r.headers
        print r.status_code
        # print json.loads(r.text)["ok"]
        print r.text

    def req_get(self):
        r = requests.get(url=self.url, params={"a": 1})
        print r.headers
        print r.status_code
        print r.text


if __name__ == "__main__":
    mp = mock_post()
    # mp.req_post()
    mp.req_get()
