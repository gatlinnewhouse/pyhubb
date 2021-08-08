Property = custom session field with values, like a Radio List:

![Editing a Radio List on Hubb site](/pics/sessionradiolistproperty.jpg)

This assumes you have already [authenticated](https://help.hubb.me/hc/en-us/articles/212113057-Getting-Started-Authorization-Token) and have a bearer token to make API calls with.

In order to add a property to a session you will need to make a POST call with REST to the API endpoint at [https://ngapi.hubb.me/api/v1/5725/PropertyValues](https://ngapi.hubb.me/swagger/ui/index#!/PropertyValues/PropertyValues_PostByVersionAndEventidAndPropertyvalue) (scroll down on the page for the documentation linked).

You include your bearer auth token in your POST call headers, and set the Accept header to `appliation/json`. You will then need to send to this a JSON in the body which looks something like this:

```json
{
    "SessionId": 123456,
    "PropertyMetadataId": 654321,
    "Value": "Multi1,Multi2"
}
```

`SessionId` is the 6 digit number corresponding to the session you want to add a property to. You can find this either through the URL for editing a session (where the SessionId is the last 6 digits in the URL after `/Details/` or through calls to the [Sessions endpoint](https://ngapi.hubb.me/swagger/ui/index#!/Sessions).

`PropertyMetadataId` is a 6 digit number corresponding to the property, *in general*, for sessions or users. PropertyMetadataIds are **not specific** ids that represent a property and value for a specific session or user---they are general ids for the property **in contrast to** id values used when Updating a Property/Custom Field using the PropertyValues endpoint. You can find the PropertyMetadataId by making a call on the [PropertyMetadata](https://ngapi.hubb.me/swagger/ui/index#!/PropertyMetadata) endpoint and looking for the Id value associated with the Custom Field, or Property, you wish to add.

`Value` is the attributes or options selected for your custom field. In the "Is there a Q&A?" example above, this would be set to "Yes" or "No". But when adding multiple values for a Multi Select List, the values are seperated by a comma within the quotation marks---like in the example JSON above. Values for properties can also be found through GET calls on the [PropertyMetadata](https://ngapi.hubb.me/swagger/ui/index#!/PropertyMetadata) endpoint.
