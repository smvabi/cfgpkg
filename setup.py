import toml
from setuptools import setup,find_packages

def get_dependencies():
    # Load Pipfile
    with open('Pipfile') as f:
        pipfile = toml.load(f)

    # Extract dependencies from Pipfile
    dependencies = pipfile.get('packages', {})
    dev_dependencies = pipfile.get('dev-packages', {})
    tests = pipfile.get('tests', {})
    return dependencies, dev_dependencies, tests

setup(
    name="cfgpkg",
    version="0.0.1",
    author="AB-InBev",
    description="AB-InBev Insights Copilot Engine repo package",
    include_package_data=True,
    packages=find_packages(where='src', exclude=["tests"]),
    package_dir={'': 'src'},
    package_data={
        '': ['**/*.yml', '**/*.json'],
    },
    install_requires=[*get_dependencies()[0].keys()],
    platforms=["Windows", "Linux", "MacOS"],
    test_suite="pytest",
    python_requires=">=3.7",
)