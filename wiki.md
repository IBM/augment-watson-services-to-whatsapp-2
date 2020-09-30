# Short Title

Augment Watson Visual Recognition with WhatsApp

# Long Title

Build a WhatsApp bot to classify food images with the help of Visual Recognition


# Author
* [Manoj Jahgirdar](https://www.linkedin.com/in/manoj-jahgirdar-6b5b33142/)
* [Rahul Reddy Ravipally](https://www.linkedin.com/in/rahul-reddy-ravipally/)
* [Srikanth Manne]()
* [Manjula Hosurmath](https://www.linkedin.com/in/manjula-g-hosurmath-0b47031)

# URLs

### Github repo

https://github.com/IBM/augment-watson-services-to-whatsapp-2

### Video Link

# Summary

In this Code Pattern, we will build a WhatsApp bot augmented with IBM Watson services that will be capable of classifying food images provided by the users in WhatsApp.

# Technologies

* [Python](https://developer.ibm.com/technologies/python)

* [JavaScript](https://developer.ibm.com/technologies/javascript/)

* [Artificial Intelligence](https://developer.ibm.com/technologies/artificial-intelligence/) 


# Description



# Flow

<!--add an image in this path-->
![architecture](doc/source/images/architecture.png)

1. User sends a message to WhatsApp.

2. The message is redirected to Twilio Programmable Messaging service.

3. Twilio Programmable Messaging service will further forward the message to the backend application hosted on IBM Cloud.

4. The backend application interacts with the Watson Visual Recognition service to get the response.

5. Watson Visual Recognition service does the necessary computation and returns a response accordingly.

6. The backend application processes the response and converts it to user readable format and forwards it Twilio.

7. Twilio forwards this message as a reply on WhatsApp.

8. The user will receive this as a response from Watson Visual Recognition service on WhatsApp.

# Instructions

> Find the detailed steps in the [README](https://github.com/IBM/augment-watson-services-to-whatsapp-2/blob/master/README.md) file.


1. Clone the repo

2. Create Watson services

3. Create serverless cloud functions

4. Deploy the Server Application on IBM Cloud Foundry, Create Twilio service & Configure credentials


# Components and services

* [Cloud Functions](https://developer.ibm.com/components/cloud-foundry/)

* [IBM Cloud](https://developer.ibm.com/components/cloud-ibm/)

* [Watson APIs](https://developer.ibm.com/components/watson-apis/)
