from setuptools import find_packages, setup

setup(
	name='kiwrious_lib',
	packages=find_packages(include=['kiwrious_lib']),
	description='Python library for reading Kiwrious sensors',
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest==4.4.1'],
	test_suite='tests',
)
