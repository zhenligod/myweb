# _*_ coding:utf-8 _*_
import urllib2
import json
import os
import multiprocessing

# worker function


def worker(sign, lock):
    for i in range(0, 10000):
        # lock.acquire()
        data = {
            "data": {
                "type": "clazz",
                "attributes": {
                    "type": 1,
                    "title": "测试课堂-" + str(i) + "-" + str(os.getpid()),
                }
            }
        }

        file = open('token.txt')
        token = file.read()
        file.close()

        req_url = 'https://lxapi.lexiangla.net/cgi-bin/v1/classes?access_token='+token
        headers = {
            'Content-Type': 'application/json',
            'staffid': 'LX001'
        }
        request = urllib2.Request(
            url=req_url, headers=headers, data=json.dumps(data))
        response = urllib2.urlopen(request, timeout=5)

        print(response.read().decode('utf-8'))
        print(sign, os.getpid())
        # lock.release()


# Multi-process
record = []
lock = multiprocessing.Lock()


def main():
    for i in range(6):
        process = multiprocessing.Process(
            target=worker, args=('process', lock))
        process.start()
        record.append(process)

    for process in record:
        process.join()


if __name__ == '__main__':
    main()
