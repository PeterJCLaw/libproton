from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(name = "libproton",
      version = "1.0",
      packages = find_packages(),
      description = description,
      author = "Peter Law",
      author_email = "PeterJCLaw@gmail.com",
      install_requires = ['nose >=1.3, <2',
                          'PyYAML >=3.11, <4',
                          'mock >=1.0.1, <2'],
      zip_safe = True
      )
