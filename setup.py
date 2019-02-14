import setuptools

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name='geemusic',
    version='0.0.1',
    url='https://github.com/fergyfresh/geemusic',
    license='MIT License',
    author='Billy Ferguson',
    author_email='william.d.ferg@gmail.com',
    description='Using Google Play Music on the Amazon Alexa',
    long_description=__doc__,
    packages=['geemusic'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
    test_requires=[
        'mock',
        'requests',
        'unittest',
    ],
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
