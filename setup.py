import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='root_report',  
     version='0.1',
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
         "License :: OSI Approved :: LGPL2.1 License",
         "Operating System :: OS Independent",
     ],
 )

