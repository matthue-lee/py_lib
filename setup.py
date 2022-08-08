from setuptools import find_packages, setup

setup(
	name='Kiwriouslib',
	packages=find_packages(include=['Kiwriouslib']),
	description='Python library for reading Kiwrious sensors',
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest==4.4.1'],
	test_suite='tests',
)
