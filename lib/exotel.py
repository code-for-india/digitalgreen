#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import requests
from django.conf import settings

from settings import sid, token


def survey(sid, token, url,
                              customerNo, callerid,videoId,
                              timelimit=None, timeout=None, calltype='trans'):
    # return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
    #     auth=(sid, token),
    #     data= {
    #         'From': agent_no,
    #         'To': customerNo,
    #         'CallerId': callerid,
    #         'TimeLimit': timelimit,
    #         'TimeOut': timeout,
    #         'CallType': calltype
    #     })

    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': customerNo,
            'CallerId': callerid,
            'TimeLimit': timelimit,
            'Url': url,
            'TimeOut': timeout,
            'CallType': calltype,
            'CustomField': videoId
        })

if __name__ == '__main__':
    r = survey(
        sid, token,
        # agent_no="9718935868",
        #customerNo="9718935868",
        customerNo="9972532929",
        callerid="08033013384",
        url='http://my.exotel.in/exoml/start/23637',
        timelimit="500",  # This is optional
        timeout="500",  # This is also optional
        calltype="trans",  # Can be "trans" for transactional and "promo" for promotional content
        videoId="395"
        )
    print r.status_code
    pprint(r.json())