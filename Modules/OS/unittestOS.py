import unittest, os, subprocess
import psutil
from Modules.OS import changeVolume


class testOS(unittest.TestCase):

    def test_changeVolume(self):
        os.popen("python3 changeVolume.py 50")
        pipe = os.popen("amixer -D pulse sget Master | grep 'Right:'|awk -F'[][]' '{print $2}'")
        currVol = pipe.read()
        self.assertEqual(currVol,"50%\n")
        return 1

    @unittest.skip("Сменить окно - Не проверяется")
    def test_changeWindow(self):
        '''TODO: НУЖЕН ИЛИ НЕТ?'''

    def test_createDir(self):
        os.popen("rm -rf " + "unittestDir")
        os.popen("python3 createDir.py unittestDir")
        testDir = os.path.exists("unittestDir")
        os.popen("rm -rf " + "unittestDir")
        #self.assertEqual(testDir, True)
        self.assertIs(testDir, True)

    def test_createFile(self):
        os.popen("rm" + "unittestFile")
        os.popen("python3 createFile.py unittestFile")
        testFile = os.path.exists("unittestFile")
        os.popen("rm" + "unittestFile")
        #self.assertEqual(testFile, True)
        self.assertIs(testFile, True)

    def test_deleteDir(self):
        os.popen("python3 createDir.py unittestDir")
        os.popen("python3 deleteFileDir.py unittestDir")
        testDir = os.path.exists("unittestDir")
        #self.assertEqual(testDir,False)
        if(testDir == False):
            self.assertIs(testDir, False)

    def test_deleteFile(self):
        os.popen("python3 createFile.py unittestFile")
        os.popen("python3 deleteFileDir.py unittestFile")
        testFile = os.path.exists("unittestFile")
        #self.assertEqual(testFile, False)
        self.assertIs(testFile, False)

    def test_moveFile(self):
        os.popen("python3 createFile.py unittestFile")
        os.popen("python3 moveFile.py unittestFile ..")
        testFile = os.path.exists("../unittestFile")
        os.popen("rm -rf ../unittestFile")
        self.assertIs(testFile, True)

    def test_openFile(self):
        os.popen("python3 createFile.py unittestFile")
        os.popen("python3 openFile.py unittestFile")
        processes = list(psutil.process_iter())
        for i in processes:
            if "unittestFile" in str(i.name):
                self.assertIn("unittestFile",str(i.name))

    def test_openTerminal(self):
        os.popen("python3 openTerminal.py")
        processes = list(psutil.process_iter())

        for i in processes:
            if "gnome-terminal" in str(i.name):
                self.assertIn("gnome-terminal",str(i.name))

    @unittest.skip("Перезагрузка - Не проверяется")
    def test_reboot(self):
        '''TODO: НУЖЕН ИЛИ НЕТ?'''

    @unittest.skip("Выключить компьютер - Не проверяется")
    def test_powerOff(self):
        '''TODO: НУЖЕН ИЛИ НЕТ?'''

if __name__ == '__main__':
    unittest.main()
