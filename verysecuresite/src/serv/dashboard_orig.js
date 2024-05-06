
    document.getElementById("logout-form").addEventListener("submit", function(event) {
      event.preventDefault(); 

      const query = `mutation { accountDeleteSessions {status} }`;

      fetch('https://cloud.appwrite.io/v1/graphql', {
        method: 'POST',
        headers: {
          'X-Appwrite-Project': '6622dcf123e47665c626',
          'Content-Type': 'application/graphql',
        },
        body: query,
        credentials: 'include'
      }).then(r => {
        window.location.href = "/"; 
      });
    });
