import subprocess
import yaml
from DBHandler import DBHandler

class Command:

    def __init__(self, configFile, dbHandler):
        self.configFile = configFile
        self.dbHandler = dbHandler

    def getCompileScripts(self, pkgId):
        #self.preConfigureScript =
        #self.configureScript =
        #self.postConfigureScript =
        #self.preMakeScript =
        #self.makeScript =
        #self.postMakeScript =
        #self.preInstallScript =
        #self.installScript =
        #self.postInstallScript =
        return

    def readRecipe(self, packageName=None, packageVersion=None):
        self.dbHandler.setupConn(self.dbFile, self.dbPath)
        cur = self.dbHandler.getCursor()
        #cur.execute("SELECT ? FROM Data where ?=?", (column, goal, constrain,))
        cur.execute('''insert into stocks (name, price) values ("hans", "44.4")''')
        self.dbHandler.getConn().commit()
        self.dbHandler.getConn().close()
        return

    def build(self):
        return


    def configure(self):
        return

    def make(self):
        return

    def makeInstall(self):
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


command = Command('config.yaml', DBHandler())
command.parseConfigFile()
command.readRecipe()
