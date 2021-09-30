# URL Prompts for Phantom 

This project aims to facilitate external approval and prompts for Splunk Phantom. You may be interested into this project if you're a playbook developer
who needs to send out prompts to users which do not have access to Splunk Phantom SOAR directly.

**urlprompt** is a dedicated application, separate from Splunk SOAR. It can be deployed either on the same host as Splunk SOAR or on a dedicated machine. 
urlprompt does not handle the transfer of the Prompt URL to the approver, it solely allows for the generation of web prompts. Any suitable SOAR asset can be used to submit the Prompt URL to the approver within the playbook eg. Slack, MS Teams or E-Mail.



![](./assets/diagrams/out/overview.png)

