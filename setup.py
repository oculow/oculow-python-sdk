from distutils.core import setup

setup(
    name='Oculow',
    packages=['Oculow'],
    version='0.1.2',
    license='Apache Software License',
    description='Visual testing framework',  # Give a short description about library
    author='Diego Ferrand',
    author_email='potosin@live.com',
    url='https://github.com/oculow/oculow-python-sdk.git',
    download_url='https://github.com/oculow/oculow-python-sdk/archive/v0.1.2.zip',
    keywords=['VISUAL', 'TESTING', 'AI', 'EASY'],
    install_requires=[
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
