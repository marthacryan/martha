from setuptools import setup

setup(
    name="martha",
    include_package_data=True,
    data_files=[
        (
            "martha",
            ["martha.json"]
        ),
    ]
)