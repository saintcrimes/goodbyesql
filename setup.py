from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name='GoodbyeSQL',
    version='0.5.6',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy==2.0.43',
        'fastapi==0.135.1',
        'pydantic==2.12.5',
        'pydantic-settings==2.13.1'
        
    ],
    entry_points={
        "console_scripts":[
            "goodbyesql=goodbyesql.main:main"
        ]
    },
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/saintcrimes/goodbyesql",
    project_urls={
        "Source": "https://github.com/saintcrimes/goodbyesql",
        "Issues": "https://github.com/saintcrimes/goodbyesql/issues", 
    },
    license="MIT",
    classifiers=[

    ],
)