from setuptools import setup, find_packages

setup(
    name='openai_manager',
    version='0.1.0-beta',
    description='A singleton manager for interfacing with the OpenAI API',
    author='ARC4D3',
    packages=find_packages(),
    install_requires=[
        'openai>=0.27.8',
        'configparser>=5.3.0',
        'mac_address_encryptor>=0.1.0-beta',  # Assuming shared is a package that includes Logger and MACAddressEncryptor
        'logger>=0.1.0-beta',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
