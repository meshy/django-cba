from setuptools import setup


version = '0.0.1a1'


setup(
    author='Charlie Denton',
    author_email='charlie@meshy.co.uk',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
    ],
    description='A class-based admin system for Django',
    include_package_data=True,
    install_requires=[],
    name='django-cba',
    packages=['cba'],
    url='https://github.com/meshy/django-cba/',
    version=version,
)
