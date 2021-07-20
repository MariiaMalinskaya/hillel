from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/phones/create/')
# http://192.168.0.102:5000//phones/create/?contactName=test&phone=123456
def create_phone():
    contact_Name = request.args['contactName']
    phone_value = request.args['phone']

    con = sqlite3.connect('new.db')
    cur = con.cursor()
    sql_query = f'''
    INSERT INTO phones (contactName, phoneValue)
    VALUES ('{contact_Name}', '{phone_value}')
    '''

    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'create_phone'

@app.route('/phones/read/')
def read_phone():
    con = sqlite3.connect('new.db')
    cur = con.cursor()
    sql_query = '''
    SELECT * FROM phones;
    '''
    cur.execute(sql_query)
    result = cur.fetchall()
    # breakpoint()
    con.commit()
    con.close()
    return str(result)


@app.route('/phones/update/')
def update_phone():
    contact_Name = request.args['contactName']
    phone_value = request.args['phone']

    con = sqlite3.connect('new.db')
    cur = con.cursor()
    sql_query = f'''
        UPDATE phones
        SET contactName  = '{contact_Name}', phoneValue = '{phone_value}'
        WHERE phoneValue = '{phone_value}'
        '''

    cur.execute(sql_query)
    con.commit()
    con.close()
    return str('/phones/update')

@app.route('/phones/delete/')
def delete_phone():
    con = sqlite3.connect('new.db')

    cur = con.cursor()
    sql_query = '''
    DELETE FROM phones WHERE contactName  = '{contact_Name}' AND phoneValue = '{phone_value}'
    '''
    cur.execute(sql_query)
    con.commit()
    con.close()
    return 'delete_phone'


if __name__ == '__main__':
    # app.run(host = "192.168.0.102", port = 5000)
    app.run(host='0.0.0.0', debug=True)
