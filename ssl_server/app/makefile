req:
	@pip install -r requirements.txt
key_crt:
	cd keys
	openssl req -out keys/CSR.csr -new -newkey rsa:2048 -nodes -keyout keys/privateKey.key
	openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout keys/privateKey.key -out keys/certificate.crt
	openssl req -out keys/CSR.csr -key keys/privateKey.key -new
	openssl x509 -x509toreq -in keys/certificate.crt -out keys/CSR.csr -signkey keys/privateKey.key
	openssl rsa -in keys/privateKey.pem -out keys/newPrivateKey.pem
	cd ..
