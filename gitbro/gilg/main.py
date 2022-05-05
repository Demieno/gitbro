import pkg_resources

from gitbro.abc.ArgFormater import ArgumentParser
from gitbro.gilg.BashGitLogList import BashGitLogList


version = pkg_resources.require("gitbro")[0].version


class RunCommand:
    def __init__(self, args):
        self.args = args

    def run(self):
        BashGitLogList(self.args)


def run():
    parser = ArgumentParser(description="Show this help message and exit.",
                            allow_abbrev=False, add_help=False)
    parser.add_argument('-v', '--version', action='version',
                        version=f'%(prog)s {version}',
                        help="Show program's version number and exit.")
    parser.add_argument('-h', '--help', action='help',
                        help='Example: gilg -g help l 2 -> git log -i --grep=help  -5 ')
    parser.add_argument('-g', '-i --grep', help='grep')
    parser.add_argument('-e', '-i --grep --invert-grep', help='invert-grep')
    parser.add_argument('-c', '--compare', help='compare')
    parser.add_argument('-p', '--pretty', help="--pretty=format:'%C(yellow)%h%Creset'")
    parser.add_argument('-t', '--graph', help='graph')
    parser.add_argument('-d', '--patch-with-stat', help='patch-with-stat')
    parser.add_argument('-o', '--oneline', help='grep_regex')
    parser.add_argument('-l', '--len', help='len list log')
    args = parser.parse_args()

    print(args)  # ToDo: delete in prod
    gr = RunCommand(args)
    gr.run()


if __name__ == '__main__':
    run()
