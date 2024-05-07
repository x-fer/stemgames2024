    document.getElementById("register-form").addEventListener("submit", function(event) {
      event.preventDefault(); 
      const query = `mutation { accountCreateAnonymousSession { _id } }`;

      fetch('https://cloud.appwrite.io/v1/graphql', {
        method: 'POST',
        headers: {
          'X-Appwrite-Project': '6622dcf123e47665c626',
          'Content-Type': 'application/graphql',
        },
        body: query,
        credentials: 'include'
      })
        .then(response => response.json())
        .then(data => {
          if (data.errors) {
            document.getElementById("Register-error").textContent = data.errors[0].message;
          } else {
            if (data.data.accountCreateAnonymousSession._id) {
              window.location.href = "/dashboard.html"; // Redirect to dashboard upon successful Register
            } else {
              document.getElementById("Register-error").textContent = data.errors[0].message;
            }
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
