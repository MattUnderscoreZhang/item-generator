poetry shell
poetry export -f requirements.txt --without-hashes -o requirements.txt
poetry run pip install . -r requirements.txt -t package_tmp
cd package_tmp
find . -name "*.pyc" -delete
zip -r ../item_generator.zip .
cd ..
