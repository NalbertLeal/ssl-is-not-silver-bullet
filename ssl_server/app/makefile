all:
	@echo ">> Choose a option:"
req:
	@pip install requirements
key_crt:
	@cd keys
	@openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key
	@openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt
	@openssl req -out CSR.csr -key privateKey.key -new
	@openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key
	@openssl rsa -in privateKey.pem -out newPrivateKey.pem
	@cd ..
