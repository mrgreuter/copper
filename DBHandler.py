import sqlite3
import yaml

class DBHandler:

    def __init__(self, configFile):
        self.configFile = configFile
        return

    def setupConn(self):
        self.conn = sqlite3.connect(self.dbPath + self.dbFile)

    def getCursor(self):
        return self.conn.cursor()

    def getConn(self):
        return self.conn

    def testConn(self):
        return

    def parseConfigFile(self):
        with open(self.configFile) as cfg:
            try:
                yamlConfig = yaml.load(cfg)
                self.dbPath = yamlConfig['db']['dbPath']
                self.dbFile = yamlConfig['db']['dbFile']
                self.dbUser = yamlConfig['db']['dbUser']
                self.dbPass = yamlConfig['db']['dbPass']

            except yaml.YAMLError as exc:
                print(exc)