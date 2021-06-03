# Communicating Over HTTPS Connection

HTTPS website ensures the following security layers:

1. **Encryption**: the plain text is converted to ciphertext and back.

2. **Authentication**: verifies that a person or thing is who they say they are.

3. **Data Integrity**: data can not be modified or corrupted during the transfer.


### How HTTPS Authentication works?

When a user visits a website he/she wants to be sure that this is an 
authentic website, and not a fake website mocked by eavesdroppers in order
to steal user login credentials. Authentication mechanism protects
users from the Man-In-The-Middle attack, and builds users trust.

HTTPS authentication relies on Public Key Infrastructure (PKI). PKI introduces
the concept of certificates. The Certificates are like passports for the Internet.
Certificates are issued by Certificate Authorities (CA) like Verisign or
Let's Encrypt. Certificate Authorities are considered a Trusted Third Parties (TTP) 
in PKI.

It is impractical for a browser to know about every single certificate
that have ever been issued, it is much more sensible to keep the information
about CAs, and all modern browsers come with lots of Certificate Authorities
automatically installed

It is a responsibility of the website owner to obtain a certificate.
The website certificate acquisition scenario looks more or less as follows:

1. Create a Certificate Signing Request (CSR).

2. Send the CSR to a Certificate Authority (Trusted Third Party).

3. The Certificate Authority is expected to verify the information provided.

4. If verification process went well, the CA signs the CSR.

5. The CA issues the verified Public Key (aka Certificate).


### How the Data Integrity mechanism works?

The encryption suite (TLS/SSL) uses a digest algorithm (SHA, SHA-1, SHA-2)
to compute a Hash-Based Message Authentication Code (HMAC). This message
is then used to check the integrity of the record.


### How HTTPS Encryption Works?

Encrypted data is intended to be kept secure from eavesdroppers. 
When the user is browsing a website, nobody can 'listen' the conversation, 
track activities across multiple pages, or steal their information.

When you are communicating over a secure website, the server
sets up a secure HTTPS connection relying on the following principles:

1. The browser requests information from the server.

2. The browser and the server exchange public keys.

3. The browser and the server generate a shared private key.

4. The browser and the server encrypt and decrypt messages using this
shared key through symmetric encryption.
   

### HTTPS Communication Demo with Python

The source code is located in the git repository:


Project structure:

    .
    ├── ca_certificates_for_client
    │   ├── ca_public_key.pem
    │   └── readme.md
    ├── certificates
    │   ├── site_private_key.pem
    │   └── site_public_key.pem
    ├── demo_client.py
    ├── demo_server.py
    ├── secret
    │   └── reminder.txt
    └── start_https_server.sh


In the directory named *ca_certificates_for_client* we have a sample CA certificate
**ca_public_key.pem**. It will be used to validate the server certificates.

In the directory *certificates* we have got server certificates, those certificates
will be used when serving site content over HTTPS. The private key of the 
server is stored in the file *site_private_key.pem*, and it is encryptied using
a secret passphrase, the passphrase can be found in *secret/reminder.txt*.

A file *demo_server.py* contains a simplified version of the server side code.

A file *demo_client.py* contains a simplified version of the client side code.

A file *start_https_server.sh* contains HTTPS server starting script. The demo
server runs on localhost:8080.

In order to start the HTTPS server on Linux go to directory 
Code/HTTPS_Website_Example, and issue the command:

    $ ./start_htpps_server.sh

