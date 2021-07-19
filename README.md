# Deliverr

Take home test for the Software Engineer-Integrations role at a Deliverr

Instructions to run :
Download the source code

Activate the environment (make sure you are in Deliverr Folder)  
 on windows : `\env\Scripts\activate`  
 on linux : `source env/bin/activate`

Now sync your database : `python manage.py migrate`  
Lets Drop into Django Shell to Create some record : `python manage.py shell`

`from Catalog.models import Item`  
`from Catalog.serializers import ItemSerializer`  
`from rest_framework.renderers import JSONRenderer`  
`from rest_framework.parsers import JSONParser`  
`item = Item (sku = "sku1", title = "title1" , isDigital = True, color="red")`  
`item.save();`

Quit out of the shell: `quit()`

Run server :  
`python manage.py runserver`

Enter `http://127.0.0.1:8000/prd_list/` in your browser to see list of all items in catalog :  
![GET request to retrieve all items](GetItems.PNG?raw=true)

As you can see you can apply filters to title and isDigital properties  
![Filter Some Items](FilterItems.PNG?raw=true)

Enter `http://127.0.0.1:8000/prd_detail/1/` to view/update specific item.  
![View Item](ItemDetail.PNG?raw=true)

Enter `http://127.0.0.1:8000/prd_listp/` in your browser ,to put/post an item in catalog :  
![Post Item](ItemPost.PNG?raw=true)
