# 

```
npm install @openapitools/openapi-generator-cli -g
openapi-generator-cli version

openapi-generator-cli version-manager set 5.1.0

openapi-generator-cli generate -i https://raw.githubusercontent.com/openapitools/openapi-generator/master/modules/openapi-generator/src/test/resources/3_0/petstore.yaml -g python-flask -o ./test_flask
```

openapi-generator-cli generate -i ./src/openapi/spec.yaml -g python-flask -o ./test_flask_base