from Scripts.TestCases.Install.Install import *
class InstallVerify:
    def install_verify(self):
        install = Install().intall()
        if install.stderr == b"":
            return install.stdout
        else:
            return install.communicate()

if __name__ == '__main__':
    print(InstallVerify().install_verify())