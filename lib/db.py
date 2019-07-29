"""数据库操作"""
import sys
sys.path.append("..")    #提升包搜索路径到项目路径

import pymssql


from config import config as cf

#获取数据库连接
def get_conn():
    conn = pymssql.connect(cf.db_host,
                    cf.db_user,
                    cf.db_password,
                    cf.db)
    return conn
#查询数据库
def db_query(sql):
    conn=get_conn()
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    cf.logging.debug(sql)
    cf.logging.debug(result)
    return result
#修改数据库
def db_change(sql):
    conn=get_conn()
    cur=conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()





# if __name__=="__main__":
#     print (db_query("select DLDM,DLMM from sys_czry where DLDM='platAdmin'"))
#     db_change("delete from sys_czry where DLDM='test1'")