build: css sphinx

sphinx:
  @rm -rf examples/kitchen-sink/_build
  poetry run sphinx-build -b html -d examples/kitchen-sink/_build/doctrees -n examples/kitchen-sink examples/kitchen-sink/_build/html

css:
  npm run build

start:
  npm start