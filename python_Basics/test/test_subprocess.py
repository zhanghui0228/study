import subprocess

class Cmd(object):
    tag = 'linux cmd'
    def shell(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)


if __name__ == '__main__':
    cmd = Cmd()
    cmd.shell('df -h')