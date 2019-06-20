import neovim
import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('readLog')
    def doReadSTFreeLog(self, args):
        lines = []
        with open(args[0], mode="r") as f:
            lines = f.readlines()
        warnings = ''.join(lines)
        self.vim.command('set errorformat+="[%#] %f:%l:%c %m"')
        self.vim.command('cexpr "{}"'.format(warnings))
        return
