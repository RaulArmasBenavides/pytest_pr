Execute : 

<!-- py -m doctest -v mydoctestdemo.py -->

Utilizando pyenv 

Ejecutar 
pyenv exec python -m doctest -v mydoctestdemo.py
o solo :
python -m doctest -v mydoctestdemo.py 


Ejecutar 
pyenv exec pytest --doctest-modules mydoctestdemo.py
pytest --doctest-modules mydoctestdemo.py










 pipenv install --dev pytest pytest-cov coverage
 pipenv run pytest --doctest-modules --cov=. --cov-report=term-missing --cov-report=html