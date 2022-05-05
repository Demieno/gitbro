import os

from gitbro.abc.ListResultsCaseIgnored import ListResultsCaseIgnored


class BashGitLogList:
    line: str = '{base} {action} {format} {target}'  # TODO: ":extras:"
    base: str = 'git'
    action: str = 'log {grep}'
    format: str = ''
    target: str = ''

    def __init__(self, args):
        self.args = args
        command = self.command()
        # TODO: colorful print - print('{0} {1} {2}'.format('\033[32mgit', self.action, 'option'))
        print(command)
        os.system(command)

    def command(self):
        if self.args.g:  # grep
            self.action = self.action.format(grep=f'-i --grep={self.args.g}')
        elif self.args.e:  # exclude
            self.action = self.action.format(grep=f'-i --grep={self.args.e} --invert-grep')
        elif self.args.compare:  # compare
            list_results = ListResultsCaseIgnored()

            found = 'master'
            if len(self.args.c) > 0:
                found = list_results.find_branch_by_partial(self.args.compare)

            self.action = self.action.format(grep='{0}..'.format(found))
        else:
            self.action = self.action.format(grep='')

        if self.args.pretty:  # pretty
            self.format = "--pretty=format:'%C(yellow)%h%Creset|%C(red)%ad%Creset|" \
                          "%C(yellow)%an%Creset:%s' --date=format:'%Y-%m-%d %H:%M:%S'"
        elif self.args.graph:  # traces
            self.format = '--graph'
        elif self.args.patch_with_stat:  # diff
            self.format = '--patch-with-stat'
        elif self.args.oneline:  # oneline
            self.format = '--oneline'

        if self.args.len:  # list
            self.target = f'-{self.args.len}'
        else:
            self.target = ''

        self.line = self.line.format(base=self.base, action=self.action, target=self.target, format=self.format)

        return self.line
