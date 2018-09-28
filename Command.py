import subprocess
from DBHandler import DBHandler

class Command:

    '''TODO
    setup environment variables
    setup root dir
    LOG Stdout/Stderr -> save to db with timestamp
    LOG time each build step takes
    '''

    def __init__(self, dbHandler):
        self.dbHandler = dbHandler
        self.dbcursor = self.dbHandler.getCursor()
        self.dbconn = dbHandler.getConn()

    def pkgId(self, pkgName, pkgVersion):
        return

    def getCompileScripts(self, pkgId):
        self.dbcursor.execute("SELECT * FROM config WHERE PKGID = ?", (pkgId,))
        self.dbconn.commit()

        result = self.dbcursor.fetchone()
        print(result)
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


dbHandle = DBHandler('config.yaml')
dbHandle.parseConfigFile()
dbHandle.setupConn()

command = Command(dbHandle)
command.getCompileScripts(1)