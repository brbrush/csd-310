import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

##Testing Connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config['user'], config['host'], config['database']))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB-ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

##Join and print function for later use
def printResult(process):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    player = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER " + process + " --")
    for players in player:
        print("Player ID: {}".format(players[0]), "\nFirst Name: {}".format(players[1]), "\nLast Name: {}".format(players[2]), "\nTeam Name: {}\n".format(players[3]))

cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (21, 'Smeagol', 'Shire Folk', 1);")

printResult("INSERT")

cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

printResult("UPDATE")

cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

printResult("DELETE")

db.close()