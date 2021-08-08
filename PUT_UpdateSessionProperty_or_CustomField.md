To update a session property or custom field you first need to figure out what the `PropertyValueId` for the session and property you want to update is---this id is unique for a specific session's specific property/custom field and making calls on it will not affect any custom fields or properties on other sessions.

To find the `PropertyValueId` you should run a GET call on the [Sessions](https://ngapi.hubb.me/swagger/ui/index#!/Sessions) endpoint while [expanding](https://help.hubb.me/hc/en-us/articles/360013379433-Querying-API-Data-OData-Parameters) on the `PropertyValues`. You can make this call to either the generic Sessions endpoint or to an endpoint for a specific session using its id at the end of the endpoint URL, e.g. [Sessions/123456](https://ngapi.hubb.me/swagger/ui/index#!/Sessions/Sessions_GetByVersionAndIdAndEventid).

----

Let's run through an example:

Say I make a call on the sessions endpoint and find out the session I want to edit, "Anotha' One", has the id `111111`. Then I will make a call on that specific session id while expanding on `PropertyValues` in order to get this result back:

```json
{
    "PropertyValues": [
        {
            "Id": 123456,
            "Value": "No",
            "PropertyMetadataId": 654321,
            "UserId": null,
            "SessionId": 111111,
            "StaffingLocationId": null,
            "OptionId": null,
            "LastModifiedById": -100
        }
    ],
    "Id": 111111,
    "Title": "Anotha' One",
    "Description": "Yeah that's right, anotha' one",
    "Mandatory": false,
    "Enabled": true,
    "CanBeEvaluated": false,
    "VideoLink": null,
    "Code": "MORE2",
    
    [... truncated for privacy and length ...]
    
}
```

In order to update that "No" value to a "Yes": I will then make a PUT call on the `PropertyValues` endpoint with the id `123456` like so `https://ngapi.hubb.me/api/v1/event_id/PropertyValues/123456` with the body `"Yes"`.
