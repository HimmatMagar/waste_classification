import setuptools

__version__ = '0.0.0.0'

REPO_NAME = "waste_classification"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "wasteClassification"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setuptools.setup(
      name="wasteClassification",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End DL Learning implementation for waste classification to predict wheather the things is recycle or organic",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=setuptools.find_packages(where='src')
)