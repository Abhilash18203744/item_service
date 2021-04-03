from setuptools import setup, find_packages
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(name="media_upload_app",
      version='1.0.0',
      description='APIs developed for media upload app.',
      author='Abhilash Kadhane',
      install_requires=install_requires,
      packages=find_packages())