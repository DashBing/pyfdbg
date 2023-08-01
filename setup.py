import setuptools
from src.pyfdbg.data import version_in as version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfdbg",
    version=version,  #版本
    author="DashBing",
    author_email="mcbbkf@outlook.com",
    description="一个简单且强大、易于使用的调试器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #scripts=[],
    #url="项目主页url",
    #project_urls={
    #    "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    #},  #额外链接
    classifiers=[
        "Development Status :: 1 - Planning",
        #"Development Status :: 2 - Pre-Alpha",
        #"Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        #"Development Status :: 7 - Inactive",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        #"Operating System :: Microsoft :: Windows",
        #"Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
    ],
    install_requires=["phap>=3.1.0"],  #依赖项定义
    entry_points = {
        'console_scripts': [
            'pyfdbg = pyfdbg:main',
        ],
    },  #scripts定义
    package_dir={"": "src"},  #包名和值的目录 有效包存放根目录
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",  #支持版本
    #platforms=["Windows"],  #支持系统
)
