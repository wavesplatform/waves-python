from setuptools import setup

setup(
    name='waves_python',
    version='1.0.8',
    packages=['waves_python', 'waves_python.api', 'waves_python.info', 'waves_python.util', 'waves_python.model',
              'waves_python.common', 'waves_python.common.crypto', 'waves_python.account', 'waves_python.transaction'],
    url='https://github.com/wavesplatform/waves-python',
    license='',
    install_requires=['requests',
                      'base58>=2.1.0',
                      'dataclasses-json>=0.5.7'
                      ],
    author='Dmitry Rozhaev',
    author_email='admin@waveslabs.com',
    description='Python library for interacting with the Waves blockchain.'
)
