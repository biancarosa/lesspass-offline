install:
	cd lesspass/packages/lesspass-pure && yarn install

build:
	cd lesspass/packages/lesspass-pure && yarn build

upload:
	aws s3 sync lesspass/packages/lesspass-pure/dist s3://lesspass-offline.biancarosa.com.br