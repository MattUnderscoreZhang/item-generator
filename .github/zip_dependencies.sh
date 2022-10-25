poetry export -f requirements.txt --without-hashes -o requirements.txt
poetry run pip install . -r requirements.txt -t package
cd package
find . -name "*.pyc" -delete
zip -r ../item_generator.zip .
cd ..
zip -g item_generator.zip lambda_function.py
