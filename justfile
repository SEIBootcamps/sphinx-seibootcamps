build: css sphinx

sphinx:
  @rm -rf examples/kitchen-sink/_build
  @poetry run sphinx-build -b html -d examples/kitchen-sink/_build/doctrees -n examples/kitchen-sink examples/kitchen-sink/_build/html

css:
  yarn run build

start:
  yarn start

version semver:
  poetry version {{semver}}
  yarn version --{{semver}}