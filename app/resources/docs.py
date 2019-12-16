from flask import Response
from flask_restful import Resource
import fdb

from settings import Settings

class Udocs(Resource):

    def get(self, vncode, doc_id):

        con = None
        cur = None

        try:
            # connect
            db_dsn = Settings.DB_PATH + vncode + '.GDB'
            con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
            cur = con.cursor()

            # select one row
            blob_query = "select documentid, case_id, documenttext from u1_document where documentid=" + doc_id
            cur.execute(blob_query)
            row = cur.fetchone()
            if(row):
                # documenttext
                blob_document = row[2]
            else:
                # not found error
                print("UDOCS 404")
                return {"message": "Document not found!"}, 404

        except Exception as e:
            print("UDOCS 500")
            return {"message": "An error occurred!" + str(e)}, 500
            
        finally:
            print("UDOCS Cleanup...")
            # close all
            if cur:
                cur.close()
            if con:
                con.close()
        
        # return blob as msword document
        return Response(blob_document, mimetype='application/msword')


class Gdocs(Resource):

    def get(self, vncode, doc_id):

        try:
            # connect
            db_dsn = Settings.DB_PATH + vncode + '.GDB'
            con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
            cur = con.cursor()

            # select one row
            blob_query = "select documentid, case_id, documenttext from g1_document where documentid=" + doc_id
            cur.execute(blob_query)
            row = cur.fetchone()
            if(row):
                # documenttext
                blob_document = row[2]
            else:
                # not found error
                return {"message": "Document not found!"}, 404

        except Exception as e:
            return {"message": "An error occurred!" + str(e)}, 500

        finally:
            # close all
            cur.close()
            con.close()

        # return blob as msword document
        return Response(blob_document, mimetype='application/msword')


class Mdocs(Resource):

    def get(self, vncode, doc_id):

        try:
            # connect
            db_dsn = Settings.DB_PATH + vncode + '.GDB'
            con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
            cur = con.cursor()

            # select one row
            blob_query = "select documentid, case_id, documenttext from m_document where documentid=" + doc_id
            cur.execute(blob_query)
            row = cur.fetchone()
            if(row):
                # documenttext
                blob_document = row[2]
            else:
                # not found error
                return {"message": "Document not found!"}, 404

        except Exception as e:
            return {"message": "An error occurred!" + str(e)}, 500
            
        finally:
            # close all
            cur.close()
            con.close()
        
        # return blob as msword document
        return Response(blob_document, mimetype='application/msword')