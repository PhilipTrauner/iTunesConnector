from setuptools import setup
from sys import version

python_version = version[:3]
if python_version not in ("3.3", "3.4", "2.7"):
	print("ScriptingBridge (as of version 3.0.4) might not work with '%s'" % (python_version))

setup(
	name='iTunesConnector',
	version='4.2',
	packages=["iTunesConnector"],
	author="Philip Trauner",
	install_requires=["pyobjc-framework-ScriptingBridge>=3.0.4"],
	author_email="philip.trauner@aol.com",
	url="https://github.com/PhilipTrauner/iTunesConnector"
)
