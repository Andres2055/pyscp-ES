import setuptools

with open('README.txt') as f:
    readme = f.read()

setuptools.setup(
    name='pyscp',
    version='1.0.18',
    description='API Python y utilidades para la página web lafundacionscp.com.',
    long_description=readme,
    url='https://github.com/Andres2055/pyscp/tree/Espanish',
    translator = 'Andrés C.',
    author='anqxyr',
    tranlator_email = 'andrecito104@hotmail.com',
    author_email='anqxyr@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4'],
    packages=['pyscp'],
    install_requires=[
        'arrow',
        'beautifulsoup4',
        'blessings',
        'lxml==3.3.3',
        'requests',
        'peewee==2.8.0',
        'logbook'],
)
