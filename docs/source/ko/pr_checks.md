pytest transformers/test_modeling_bert.py::TestBertModel::test_forward_signature


pytest -k transformers/modeling_bert.py


pytest -k test_bert_model


pytest --order=alphabetic


pytest -n 4


pytest --data-dir /path/to/test/data


pytest --seed 42


pytest --gpu 0


pytest --precision float16


pytest --device cuda


pytest -v


pytest -q


pytest --cov transformers --cov-report xml


pytest --timeout 10


pytest --env TRANSFORMERS_CACHE=/path/to/cache


pytest --config=test_configuration.json


pytest -m slow


pytest -f my_fixture


pytest -p my_plugin


pytest --capture=no


pytest --capture=sys


pytest --doctest-modules


pytest --reruns 3


pytest --collect-only


sphinx-build -k -b html docs/ source/


sphinx-build -D html_theme='alabaster' docs/ source/


sphinx-build -D language='ja' docs/ source/


sphinx-build -b latex docs/ source/
