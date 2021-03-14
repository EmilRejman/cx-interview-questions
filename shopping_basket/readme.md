## Documentation

Project created in python3.7 with the usage of pipenv.
To work with the repo install pipenv: `pip install pipenv`.

To get all development dependencies (e.g. to extend package or run tests) run `pipenv install --dev`.
Run `pipenv lock` to update pipenv.lock file.

Example `Basket Adapter` was added to the code (`class.basket.ListOfDictBasketAdapter`). Any adapter for Basket, Offers
or Catalogue could be added to your code making this package really flexible.

Files were auto formatted with black with line width set to 120, as this is default PyCharm line width,
and the most often used one in my projects. 

In the code there are comments how the code could be improved.

### tests

To run tests go into shopping basket project and run `pipenv run pytest` or, if already within pipenv shell 
(`pipenv shell`), run  `pytest`.

### usage

Import app package and use needed components as needed. Example was done in `example.py` file. To check it run:
`pipenv run python example.py`.

Setup should be created to distribute package as module in the future.
