from setuptools import setup

with open('README') as f:
    long_description = f.read()

with open('VERSION') as f:
    version = f.readline().strip()

setup(
    name='ase-game',
    description='playing w/ setup.py',
    long_description=long_description,
    license='MIT',
    author='@wolfhesse',
    author_email='wolfgang.schuessel@gmail.com',
    url='asecms.base.wolfspool.at/py-ase-game-pg',
    version=version,
    packages=[
        'ase_game',
    ],
    scripts=[
        'scripts/eins.py',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT license',
    ],
    zip_safe=False,
    install_requires=['pytest'],
)
