import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='FirstPipPackage',
     version='0.1',
     scripts=["FirstPipPackage"] , # Sinnud's first pip package
     author="Luke Du",
     author_email="sinnud@gmail.com",
     description="A PyARDM utility package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sinnud/FirstPipPackage",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
'''
command to create package:
python3 -B setup.py bdist_wheel
'''