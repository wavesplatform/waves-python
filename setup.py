from setuptools import setup

setup(
    name='waves_python',
    version='1.0',
    packages=['src', 'src.api', 'src.info', 'src.util', 'src.model', 'src.common', 'src.common.crypto', 'src.account',
              'src.transaction'],
    url='https://github.com/wavesplatform/waves-python',
    license='',
    author='Dmitry Rozhaev',
    author_email='drozhaev@web3tech.ru',
    description='Python library for interacting with the Waves blockchain.'
)
