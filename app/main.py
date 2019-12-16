from flask import Flask
from flask_restful import Api

from resources.cases import Ucases
from resources.cases import Gcases
from resources.cases import Mcases
from resources.docs import Udocs
from resources.docs import Gdocs
from resources.docs import Mdocs

app = Flask(__name__)
api = Api(app)

api.add_resource(Ucases, '/bsp32/api/v1/<string:vncode>/ucases')
api.add_resource(Gcases, '/bsp32/api/v1/<string:vncode>/gcases')
api.add_resource(Mcases, '/bsp32/api/v1/<string:vncode>/mcases')
api.add_resource(Udocs, '/bsp32/api/v1/<string:vncode>/udocs/<string:doc_id>')
api.add_resource(Gdocs, '/bsp32/api/v1/<string:vncode>/gdocs/<string:doc_id>')
api.add_resource(Mdocs, '/bsp32/api/v1/<string:vncode>/mdocs/<string:doc_id>')

if __name__ == "__main__":
    app.run(host='', debug=False, port=2088)
