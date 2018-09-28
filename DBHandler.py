import sqlite3

class DBHandler:

    def __init__(self):
        return

    def setupConn(self, dbFile, dbPath, dbUser=None, dbPass=None):
        self.conn = sqlite3.connect(dbPath + dbFile)

    def getCursor(self):
        return self.conn.cursor()

    def getConn(self):
        return self.conn

    def testConn(self):
        return