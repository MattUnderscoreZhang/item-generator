poetry export -f requirements.txt --without-hashes -o requirements.txt
poetry run pip install . -r requirements.txt -t package_tmp
cd package_tmp
find . -name "*.pyc" -delete
cd ..
mv item_generator/lambda_function.py .
zip -r item_generator.zip package_tmp/ lambda_function.py
