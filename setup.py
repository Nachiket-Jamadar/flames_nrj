from setuptools import setup, find_packages

setup(
	name='flames_nrj',
	version='0.4',
	description='flames_nrj library for python robot framework practice',
	author='Nachiket Jamadar',
	author_email='nachiketjam@gmail.com',
	platforms = 'any',
	packages=find_packages(),
	install_requires=[
		'robotframework',
	],
	include_package_data=True
)
