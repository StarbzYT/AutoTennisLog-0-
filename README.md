# Auto Tennis Log[0]

---

## About

This application was made with Twilio and Openpyxl (_python modules_) The user can:

> - Send a  _**text message**_ with their tennis match result (_opponent_, _score_, _winner_).
> - This text message will automatically format and be inserted to an Excel _spreadsheet_.

---

### **Inspiration**

I see myself as an avid tennis fan. As a consistent competitor in city tournaments, I found it tedious to manually keep track of my matches/results. Openpyxl gave me the perfect idea. All I needed to do was send a message from my phone and all my "match-data" would be inserted to an Excel spreadsheet. Now, I can focus on playing the point, instead of worrying about the monotonous tasks afterwards.

---

## Potential Improvements

Once the information is inserted to the spreadsheet, the layout/format can still be more explicit and streamline.

There can be many more tests for this app to ensure all methods are working correctly. (testing is something I want to be better at)

---

## Install

```bash
pip install openpyxl
pip install twilio
```

---

## **Import**

```python
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from openpyxl import load_workbook
```

---

## **Run**

```bash
python message.py
```

---
