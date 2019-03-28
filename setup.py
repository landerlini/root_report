import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='root_report',  
     version='0.1.6',
     scripts=[] ,
     author="Lucio Anderlini",
     author_email="l.anderlini@gmail.com",
     description="Simple package to produce HTML reports out of PyROOT scripts",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/landerlini/root_report",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3.4",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
         "Operating System :: OS Independent",
     ],
 )

