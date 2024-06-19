from setuptools import setup, find_packages

setup(
    name="sql2csv-exporter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "python-dotenv",
    ],
    extras_require={
        "postgres": ["psycopg2"],
        "mysql": ["mysql-connector-python"],
        "sqlite": ["pysqlite3"],
    },
)
