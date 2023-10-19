from flask import Flask, request , jsonify
import requests
from json import loads

host='0.0.0.0'
host_request=''

em_manutencao=False

def create_app():
    app=Flask(__name__)

    @app.before_request
    def log_request_info():
        data=request.data
        url=request.url.replace(host,host_request)
        head=dict(request.headers)
        if em_manutencao:
            return jsonify({'response':False, 'mensg':'serviço em manutenção'})

        if request.method=="POST":
            data=request.data
            if data:
                data=loads(data)
            else:
                data={}
            print(data)
            r=requests.post(url,headers=head , json=data)
            print(r.text)
            return r.text
        
        elif request.method=='OPTIONS':
            r=requests.options(url,headers=head)
            print(r.text)
            return r.text
            
        elif request.method=='GET':
            r=requests.get(url,headers=head)
            return r.text

    return app


if __name__=='__main__':
    app=create_app()
    app.run(port=5001, host=host, debug=1)
