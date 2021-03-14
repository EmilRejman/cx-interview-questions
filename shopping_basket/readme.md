## Documentation

Install pipenv in your python3.7 env: `pip install pipenv`.

To get all development dependencies (e.g. to extend package or run tests)run `pipenv install --dev`.
Run `pipenv lock` to update pipenv.lock file.

Run `pipenv shell` to open shell. If pipenv was installed from withing venv, you could run pipenv
with `pipenv run <any command>` to run sth withing pipenv shell without opening it.

Example `Basket Adapter` was added to the code (`class.basket.ListOfDictBasketAdapter`). Any adapter for Basket, Offers
or Catalogue could be added to your code making this package really flexible.

Files were auto formatted with black with line width set to 120, as this is default PyCharm line width,
and most often used one in my projects. 

In the code there are comments how the code could be improved.

### tests

To run tests run go into shopping basket project and `pipenv run pytest` or, if already within pipenv shell, `pytest`.

### usage

Import app package and use needed components as needed. Example: `pipenv run python example.py`.

Setup should be created to distribute package as module in the future.
