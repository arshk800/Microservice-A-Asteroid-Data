This microservice runs on Flask and employs the use of NASA's NEOWs (Near Earth Object Web Service) API. The user inputs a start and end date in the format YYYY-MM-DD and receives a list of all the asteroids, along with its specific data. 

TO RUN THE FILES:
  1.Download the server.py and client.py files
  2.Install all the required dependencies (at the top of the files)
  3.Change the port number accordingly
  4.Run the files in seperate terminals
  

  Queries to the server are sent in the form of 'https://api.nasa.gov/neo/rest/v1/feed?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}&api_key=DEMO_KEY'
    Example: https://api.nasa.gov/neo/rest/v1/feed?start_date={2024-11-03}&end_date={2024-11-09}&api_key=DEMO_KEY
  
  Parameters = start_date (YYYY-MM-DD)
               = end_date (YYYY-MM-DD) (optional, defaults to start_date if not entered)
               = port number 

  Programmatically REQUEST example:
    <img width="556" alt="Screenshot 2024-11-17 at 1 58 51 AM" src="https://github.com/user-attachments/assets/0d9d3cc9-06d3-4282-81d1-22add399a4af">


  RECEIVE example:
    <img width="525" alt="Screenshot 2024-11-17 at 1 57 56 AM" src="https://github.com/user-attachments/assets/31c46211-3a2f-40dc-8ab7-f6981f88c618">

    

    

 
