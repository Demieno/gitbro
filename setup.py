from setuptools import setup, find_packages

setup(
    name='gitbro',
    version='0.5.0',
    description='A bunch of handy commands to do things a bit faster using git command line (imho)',
    url='http://github.com/rafaelucena/gitbro',
    author='Rafael Boszko',
    author_email='rafael.boszko@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points=dict(
        console_scripts=[
            'gitbro=gitbro.mock.main:run',
            'gist=gitbro.gist.main:run',
            'gibr=gitbro.gibr.main:run',
            'gidf=gitbro.gidf.main:run',
            'giad=gitbro.giad.main:run',
        ]
    )
)

# gist - sketch done
# gibr - partially done - planned: return to last used branch, show merged, allow local alias listing
# gidf - mostly done - planned: generating patch, applying it and comparing branches/commits
# giad - sketch started
# gibk
# gicm
# gime
# gilg
# gicp - planned
# girs - planned
# gire - planned
