<h1 align="center">PYMAIL</h1>
<p align="center">Send email from command line</p>
<p align="center">

## Install


```console
$ git clone https://github.com/amyth07/pymail.git
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

## Usage

```sh
$ pymail --from senderemail@yahoo.com --passwd SenderEmailPassword --to receiveremail@outlook.com --subject "My subject" --message "My message" --attach myattachmentfile
```

#### Examples

```sh
$ pymail --from senderemail@yahoo.com --passwd SenderEmailPassword --to receiveremail@outlook.com --subject "My subject" --message "My message"
Sending email without attachments

$ pymail --from senderemail@yahoo.com --passwd SenderEmailPassword --to receiveremail@outlook.com
Sending a naked email

$ pymail --from senderemail@yahoo.com --passwd SenderEmailPassword --to receiveremail@outlook.com --subject "My subject" --message "My message" --attach mya\
ttachmentfile
Sending email with message, subject & attachments
```

## Note
#### For gmail Users
If you are using gmail for sending the email then there is 1 extra step. You will first has reduce the security of the gmail Account. 
To reduce the security of your gmail account go to the link: https://myaccount.google.com/lesssecureapps The lessSecureAppUse Feature should be "ON".


## Contributing
Do you want to make this better? Open an issue and/or a PR on Github. Thanks!


