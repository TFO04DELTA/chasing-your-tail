from setuptools import setup, find_packages

setup(
    name="chasing-your-tail",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'kismet-rest>=2023.7.1',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'cyt=cyt.main:main',
            'cyt-gui=cyt.gui:main',
        ],
    },
    author="Original: matt0177, Restructured version",
    description="A Wi-Fi monitoring and analysis tool",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
)
