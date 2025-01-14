import subprocess
import os
import re as regex

from gitbro.abc.ListResultsCaseIgnored import ListResultsCaseIgnored


class BashGitDiffStat:
    line: str = '{base} {action} {target}' # @todo - ":extras:"
    base: str = 'git'
    action: str = 'diff {head} --stat {cached}'
    target: str = ''

    def __init__(self, options: list = [], values: list = []) -> None:
        command = self.__map_command(options, values)

        # @todo - colorful print - print('{0} {1} {2}'.format('\033[32mgit', self.action, 'option'))
        print(command)
        os.system(command)

    def __map_command(self, options: list = [], values: list = []):
        if len(options) > 1 and options[1] == '-c':
            if len(values) > 0:
                self.action = self.action.format(cached='--cached', head='')
                self.target = self.__prepare_queued_diff_value(values[0])
            else:
                self.action = self.action.format(cached='--cached', head='HEAD')
        else:
            if len(values) > 0:
                self.action = self.action.format(cached='', head='')
                self.target = self.__prepare_common_diff_value(values[0])
            else:
                self.action = self.action.format(cached='', head='HEAD')

        self.line = self.line.format(base=self.base, action=self.action, target=self.target)

        return self.line

    def __prepare_common_diff_value(self, value):
        filesList = ListResultsCaseIgnored()
        value = filesList.find_changed_files_for_diff(value)

        return self.__prepare_value_wildcards(value)

    def __prepare_queued_diff_value(self, value):
        filesList = ListResultsCaseIgnored()
        value = filesList.find_queued_files_for_diff(value)

        return self.__prepare_value_wildcards(value)

    def __prepare_value_wildcards(self, value):
        target_value = ''
        if regex.search('\.\w?', value):
            target_value = '*{file_name}'.format(file_name=value)
        else:
            target_value = '*{file_name}*'.format(file_name=value)

        return target_value

    @staticmethod
    def go(options: list = [], values: list = []):
        BashGitDiffStat(options, values)
