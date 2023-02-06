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

##Selecting information from table "team"
cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}".format(team[0]), "\nTeam Name: {}".format(team[1]), "\nMascot: {}\n".format(team[2]))

##Selecting information from table "player"
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

player = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for players in player:
    print("Player ID: {}".format(players[0]), "\nFirst Name: {}".format(players[1]), "\nLast Name: {}".format(players[2]), "\nTeam ID: {}\n".format(players[3]))

db.close()