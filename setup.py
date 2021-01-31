from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name="libproton",
    version="3.0.1",
    url='https://github.com/PeterJCLaw/libproton',
    project_urls={
        'Issue tracker': 'https://github.com/PeterJCLaw/libproton/issues',
    },

    packages=find_packages(),
    description=description,
    author="Peter Law",
    author_email="PeterJCLaw@gmail.com",
    install_requires=[
        'PyYAML >=3.11, <5',
    ],
    license='MIT',
    tests_require=[
        'nose >=1.3, <2',
        'mock >=1.0.1, <2',
    ],
    test_suite='nose.collector',
    zip_safe=True,
)
