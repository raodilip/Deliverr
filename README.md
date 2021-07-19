# Deliverr

A take home test for the Software Engineer-Integrations role at Deliverr

Instructions to run :
Download the source code

Activate the environment (make sure you are in Deliverr Folder)  
 on windows : `\env\Scripts\activate`
on linux : `source env/bin/activate`

Now sync your database : `python manage.py migrate`
Lets Drop into Django Shell to Create some record : `python manage.py shell`

> > > from Catalog.models import Item
> > > from Catalog.serializers import ItemSerializer
> > > from rest_framework.renderers import JSONRenderer
> > > from rest_framework.parsers import JSONParser
> > > item = Item (sku = "sku1", title = "title1" , isDigital = True, color="red")
> > > item.save();
> > > item = ItemSerializer(item)
> > > item.data
> > > content = JSONRenderer().render(item.data)
> > > content
> > > import io

> > > stream = io.BytesIO(content)
> > > data = JSONParser().parse(stream)

> > serializer = ItemSerializer(data=data)
> > Item.is_valid()

> > > serializer.validated_data

> > > serializer.save()

Quit out of the shell: `quit()`

Run server :
`python manage.py runserver`

Enter `http://127.0.0.1:8000/prd_list/` in your browser ,you will see list of all item in catalog :
As you can see you can apply filters to title and isDigital properties

Enter `http://127.0.0.1:8000/prd_detail/1/` to view specific item.
