    window.onload = function() {
      const descQuery = 'query { databasesGetDocument ( databaseId:"usersdb", collectionId:"usersc", documentId:"663a4d0c0031f4e6edc0" ) {data} }';

      fetch('https://cloud.appwrite.io/v1/graphql', {
        method: 'POST',
        headers: {
          'X-Appwrite-Project': '6622dcf123e47665c626',
          'Content-Type': 'application/graphql',
        },
        body: descQuery,
        credentials: 'include'
      }).then(response => response.json())
        .then(data => {
          console.log(data);
          document.getElementById("about").textContent = JSON.parse(data.data.databasesGetDocument.data).about;
      });
    };

    document.getElementById("logout-form").addEventListener("submit", function(event) {
      event.preventDefault(); 

      const logoutQuery = `mutation { accountDeleteSessions {status} }`;

      fetch('https://cloud.appwrite.io/v1/graphql', {
        method: 'POST',
        headers: {
          'X-Appwrite-Project': '6622dcf123e47665c626',
          'Content-Type': 'application/graphql',
        },
        body: logoutQuery,
        credentials: 'include'
      }).then(r => {
        window.location.href = "/"; 
      });
    });
