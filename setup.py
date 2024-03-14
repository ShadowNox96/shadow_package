from setuptools import setup
readme = open('./README.md', 'r')

setup(
name='shadow_package',
version='0.1',
author='Emanuel de la Cruz',
author_email='enviame@example.com',
description='Description of sample project',
packages=['shadow_package'],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
long_description= readme.read(), 
long_description_content_type='text/markdown',
url='https://github.com/ShadowNox96/shadow_package', 
download_url= 'https://github.com/ShadowNox96/shadow_package/tarball/0.1', 
include_package_data= True
)