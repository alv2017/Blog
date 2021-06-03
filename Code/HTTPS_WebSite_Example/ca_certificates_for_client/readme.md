This is a public certificate of Certificate Authority that
issued (signed) a certificate for the Server.

It is used to avoid SSL certification error:

SSLError(SSLCertVerificationError(1, \
    '[SSL: CERTIFICATE_VERIFY_FAILED] \
    certificate verify failed: unable to get local issuer \
    certificate (_ssl.c:1076)')))

It is saying more or less the following:

webserver gave me a certificate. I checked the issuer of the certificate it gave me, 
and according to all the Certificate Authorities I know about, that issuer is not one of them.

In order to avoid this error the client was given the info about CA (public certificate):
 
    response = requests.get(url, verify='ca_certificates_for_client/ca_public_key.pem')

If you were using a web browser, you would have Certificate Authorities public keys installed with the browser.
If the CA public key is unknown to the browser, you would have to accept the CA certificate as trusted, 
or, possibly, reject it.

