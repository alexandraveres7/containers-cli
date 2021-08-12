from setuptools import setup

setup(
    name='containers-cli',
    version='0.1',
    py_modules=['containers_cli'],
    install_requires=['Click'],
    entry_points={
      'console_scripts': [
        'containers_cli = containers_cli:cli',
      ],
    },
)