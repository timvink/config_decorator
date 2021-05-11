from setuptools import setup, find_packages

# Read README in UTF-8
with open("README.md", "r", encoding="UTF-8") as f:
    long_description = ""
    for line in f:
        long_description += line


setup(
    name="demo-config-decorator",
    version="0.0.1",
    description="Demonstrate how to use a config in an ML package",
    url="https://github.com/timvink/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Vink",
    author_email="vinktim@gmail.com",
    include_package_data=True,
    license="MIT",
    install_requires=["PyYAML>=5.4.1"],
    packages=find_packages(include=['demo_config_decorator']),
)
