import subprocess
import shlex
from DBHandler import DBHandler
import os

class Command:

    '''TODO
    setup environment variables
    setup root dir
    LOG Stdout/Stderr -> save to db with timestamp
    LOG time each build step takes
    cwd to pkg; make build dir;
    '''

    def __init__(self, dbHandler):
        self.dbHandler = dbHandler
        self.dbcursor = self.dbHandler.getCursor()
        self.dbconn = dbHandler.getConn()

    def pkgId(self, pkgName, pkgVersion, fileHash):
        self.dbcursor.execute("SELECT * FROM config WHERE pkgname = ? and pkgversion = ? and filehash = ?", (pkgName, pkgVersion, fileHash,))
        return

    def getCompileScripts(self, pkgId):
        self.dbcursor.execute("SELECT * FROM config WHERE PKGID = ?", (pkgId,))
        self.dbconn.commit()

        result = self.dbcursor.fetchone()
        self.preConfigureScript = result[3]
        self.configureScript = result[4]
        self.postConfigureScript = result[5]
        self.preMakeScript = result[6]
        self.makeScript = result[7]
        self.postMakeScript = result[8]
        self.preInstallScript = result[9]
        self.installScript = result[10]
        self.postInstallScript = result[11]

    def build(self):
        return

    def extractFile(self, fileName):
        return

    def createBuildDir(self, filePath):
        return

    def configure(self):
        #collect stdout; stderr in DB
        os.chdir('/home/daniel/Downloads/binutils-2.31.1')
        if (self.preConfigureScript != None):
            preConfigArgs = shlex.split(self.preConfigureScript)
            subprocess.call(preConfigArgs)
        if (self.configureScript != None):
            configArgs = shlex.split(self.configureScript)
            subprocess.call(configArgs)
        if (self.postConfigureScript != None):
            postConfigArgs = shlex.split(self.postConfigureScript)
            subprocess.call(postConfigArgs)

    def make(self):
        return

    def makeInstall(self):
        return


dbHandle = DBHandler('config.yaml')
dbHandle.parseConfigFile()
dbHandle.setupConn()

command = Command(dbHandle)
command.getCompileScripts(1)
command.configure()