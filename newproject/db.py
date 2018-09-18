import json
import MySQLdb as mdb
import MySQLdb
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.conf import settings


def get_connection():
    defaultdb = settings.DATABASES['default']
    con = MySQLdb.connect(defaultdb['HOST'],
                      defaultdb['USER'],
                      defaultdb['PASSWORD'],
                      defaultdb['NAME'])
    return con

def _fix_in_clause(sql, *values):
    assert sql.count('%s') == len(values), (sql, values)
    placeholders = []
    new_values = []
    for value in values:
        if isinstance(value, (list, tuple)):
            placeholders.append(', '.join(['%s'] * len(value)))
            new_values.extend(value)
        else:
            placeholders.append('%s')
            new_values.append(value)
    sql = sql % tuple(placeholders)
    values = tuple(new_values)
    print(sql);
    print(values);
    return (sql, values)
'''
#class MySQLCursorDict(mdb.connector.cursor.MySQLCursor):
def _query(sql, rowdata, *args):
    connector = super(query, sql)._query(rowdata)
    print(query)
    print(values)
    con.execute(query, values)
    if rowdata:
        return dict(zip(sql.column_names, con))
        return con.fetchone()
    else:
        print("Hey welcome")
        rows = con.fetchall()
        return list(rows)


db = mdb.connect(host="",user="root",passwd="kumar5225",db="onlineindia",port="")

cursor = db.cursor(dictionary=_query) '''

def _query(sql, single_row_mode, *args):
    query, values = _fix_in_clause(sql, *args)
    conn = get_connection()
    with conn as cur:
        #conn = MySQLdb.connect(host="",user="root",passwd="kumar5225",db="onlineindia",port="")
        cur = conn.cursor(mdb.cursors.DictCursor)
        print(query)
        print(values)
        cur.execute(query, values)
        if single_row_mode:
            return cur.fetchone()
        else:
            print("hi welcome")
            rows = cur.fetchall()
            return list(rows)

def query(sql, *args):
    '''Examples
    query("Select .. where a=%s and b in (%s)", [1, (1, 2, 3)]))
    query("Select .. where a=%s and b in (%s)", [1, [1, 2, 3]]))
    query("Select .. where a=%s and b in (%s)", [1, ('a', 'b', 'c']]))
    '''
    return _query(sql, False, *args)


def query_for_object(sql, *args):
    return _query(sql, True, *args)

def query_as_json(sql, *args):
    objects = query(sql, *args)
    return json.dumps(objects, encoding="ISO-8859-1")
