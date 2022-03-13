import mysql.connector

HOST = "localhost"
USER = "dobot"
PASSWD = "X6PNeNh5T0RhIrva"
DATABASE = "dobot"

def save_position(position):
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWD,
        database=DATABASE
    )
    cursor = db.cursor()

    sql = "SELECT max(`linenumber`) FROM `commands` WHERE `commands`.`name` = %s"
    parameters = (position["name"],)
    cursor.execute(sql, parameters)
    result = cursor.fetchone()
    if result[0] == None:
        linenumber = 1
    else:
        linenumber = int(result[0]) + 1

    sql = "INSERT INTO `commands` (`name`,`linenumber`,`x`,`y`,`z`,`r`) VALUES (%s, %s, %s, %s, %s, %s)"
    parameters = (position["name"], linenumber, position["x"], position["y"], position["z"], position["r"])
    cursor.execute(sql, parameters)
    db.commit()

def get_position(position):
    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWD,
        database=DATABASE
    )
    cursor = db.cursor(dictionary=True)

    sql = "SELECT * FROM `commands` WHERE `commands`.`name` = %s AND `commands`.`linenumber` = %s"
    parameters = (position["name"],position['linenumber'])
    cursor.execute(sql, parameters)
    result = cursor.fetchone()
    if result["id"] == None:
        return '{"result": "none"}'
    else:
        return '{"result": "position", "position": {"x": ' + str(result["x"]) + ', "y": ' + str(result["y"]) + ', "z": ' + str(result["z"]) + ', "r": ' + str(result["r"]) + '}}'
