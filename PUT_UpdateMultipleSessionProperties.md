In order to update multiple properties for a session you will need to make a PUT call to the [Sessions/BulkUpdate](https://ngapi.hubb.me/swagger/ui/index#!/Sessions/Sessions_BulkUpdateByVersionAndEventidAndRequest) endpoint.

You then need to include a JSON in the body of the call like the following:

```json
{
    "items": [
        {
            "Id": 123456,
            "PropertyValues": [
                {
                    "PropertyMetadataId": 80109,
                    "Value": "No"
                },
                {
                    "PropertyMetadataId": 82007,
                    "Value": "asgdfda,adfhaddfh"
                }
            ]
        }
    ]
}
```

`Id` will be the Id for the Session you wish to edit.

`PropertyMetadataId` will be the id for the property, in general, you want to change. This is the same id used when making [POST calls to add a Property to a session](https://github.com/gatlinnewhouse/pyhubb/blob/documentation/POST_AddPropertyToSession.md).

`Value` will be the desired value for the property.

Multiple sessions can be edited in one call by providing the session objects `{ "Id: 123456` [...] `},` with commas on the end of all but the last session object.
