import subprocess
import unittest
from Scripts.Public.Path import *


class Install(unittest.TestCase):
    def test_install(self):
        apk = Path().apk_path()
        command = "adb install " + apk
        install_popen = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.failUnless(install_popen.communicate()[1], b'')


if __name__ == '__main__':
    # print(Install().install())
    unittest.main()
