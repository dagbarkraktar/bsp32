from flask import jsonify
from flask_restful import Resource
import fdb

from settings import Settings

class Ucases(Resource):

    def get(self, vncode):

        # connect
        db_dsn = Settings.DB_PATH + vncode + '.GDB'
        con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
        cur = con.cursor()

        # query string
        u1_query = "select u1c.id, u1c.full_number, u1c.short_number, u1c.year_reg, \
            u1c.main_law_article, u1c.law_article, \
            u1c.judge_id, gc.username, u1c.verdict_date, \
            u1doc.documentname, u1doc.documentid \
            from u1_case u1c \
            inner join groupcontent gc on u1c.judge_id = gc.groupcontentid \
            inner join u1_document u1doc on u1c.id = u1doc.case_id \
            where u1c.year_reg = 2018"

        cur.execute(u1_query)
        case_list = cur.fetchmany(100)

        # close all
        cur.close()
        con.close()

        #return 
        return jsonify({'ugcases': case_list})


class Gcases(Resource):

    def get(self, vncode):

        # connect
        db_dsn = Settings.DB_PATH + vncode + '.GDB'
        con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
        cur = con.cursor()

        # query string
        g1_query = "select g1c.id, g1c.case_full_number, g1c.year_reg, \
            gc.username, g1c.category_id, cc.name, \
            g1doc.documentname, g1doc.documentid \
            from g1_case g1c \
            inner join groupcontent gc on g1c.judge_id = gc.groupcontentid \
            inner join catalogcontent cc on g1c.category_id = cc.contentid \
            inner join g1_document g1doc on g1c.id = g1doc.case_id \
            where g1c.year_reg = 2018"

        cur.execute(g1_query)
        case_list = cur.fetchmany(100)

        # close all
        cur.close()
        con.close()

        #return 
        return jsonify({'grcases': case_list})

class Mcases(Resource):

    def get(self, vncode):

        # connect
        db_dsn = Settings.DB_PATH + vncode + '.GDB'
        con = fdb.connect(dsn=db_dsn, user=Settings.DB_USER_NAME, password=Settings.DB_USER_PASSW, charset='WIN1251')
        cur = con.cursor()

        # query string
        m_query = "select mc.id, mc.full_number, mc.reg_year, \
            gc.username, mc.main_law_article, mc.law_article, \
            mc.m_type, cc1.name, mc.m_sub_type, cc2.name, \
            mdoc.documentname, mdoc.documentid \
            from m_case mc \
            inner join groupcontent gc on mc.judge_id = gc.groupcontentid \
            inner join catalogcontent cc1 on mc.m_type = cc1.contentid \
            inner join catalogcontent cc2 on mc.m_sub_type = cc2.contentid \
            inner join m_document mdoc on mc.id = mdoc.case_id \
            where mc.reg_year = 2018"

        cur.execute(m_query)
        case_list = cur.fetchmany(100)

        # close all
        cur.close()
        con.close()

        #return 
        return jsonify({'mcases': case_list})