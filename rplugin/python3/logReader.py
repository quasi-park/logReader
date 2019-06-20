import neovim
import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('ReadLog', nargs='*')
    def doReadSTFreeLog(self, args):
        lines = []
        self.vim.command('set errorformat+="[%#] %f:%l:%c %m"')
        with open(args[0], mode="r") as f:
            lines = f.readlines()
        warnings = ''.join(lines)
        self.vim.command('cexpr system("cat {}")'.format(args[0]))
        return
